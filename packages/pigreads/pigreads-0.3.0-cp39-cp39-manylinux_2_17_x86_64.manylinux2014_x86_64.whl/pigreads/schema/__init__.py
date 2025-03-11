"""
Schema describing simulation configuration
------------------------------------------

This submodule provides a Pydantic schema defining a simulation. The schema is
used to read and write simulation configuration files in JSON or YAML format.

See :py:class:`Simulation` for the main schema.
"""

from __future__ import annotations

from collections.abc import Callable
from pathlib import Path
from typing import Any, Literal, Union
from warnings import warn

import numpy as np
from pydantic import BaseModel, ConfigDict, Field, model_validator

from pigreads import Models, diffusivity_matrix, prepare_array, run
from pigreads import weights as calc_weights
from pigreads.schema.setter import Setter, SetterFile, normalise_list_of_setters


class ModelEntry(BaseModel):
    """
    A model defining the reaction term in the reaction-diffusion equation.

    :see: :py:class:`pigreads.Models`
    """

    name: str
    "name of the model"
    parameters: dict[str, float] = Field(default_factory=dict)
    "parameters of the model"
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalise(cls, values: Any) -> Any:
        """
        Normalise the model entry.

        If the entry is a string, it is converted to a dictionary with an empty
        parameter set. If the entry is a dictionary with a single key, the key
        is used as the model name.

        :param values: any data to try to interpret
        :return: normalised data
        """

        if not isinstance(values, dict):
            return values

        name = values.get("name")
        if "name" in values:
            del values["name"]

        parameters = values.get("parameters", {})
        if "parameters" in values:
            del values["parameters"]

        if name is None:
            if len(values) != 1:
                return values

            name, parameters = next(iter(values.items()))
            return {"name": name, "parameters": parameters or {}}

        parameters = {**parameters, **values}

        return {"name": name, "parameters": parameters or {}}


class DiffusivityFile(BaseModel):
    """
    Diffusivity matrix read from a file.

    The file should contain a 4D array with the diffusivity values. The array
    should have shape ``(Nz, Ny, Nx, 6)`` where the last dimension corresponds to
    the six independent components of the diffusivity matrix.

    :see: :py:func:`pigreads.diffusivity_matrix` and :py:mod:`numpy.lib.format`
    """

    file: Path
    "path to the file containing the diffusivity matrix"
    model_config = ConfigDict(extra="forbid")

    def __call__(self) -> np.ndarray[Any, Any]:
        """
        Read the diffusivity matrix from the file.

        :return: diffusivity matrix
        """
        array: np.ndarray[Any, Any] = np.load(self.file)
        assert array.ndim == 4, "Diffusivity matrix should be 4D"
        assert array.shape[-1] == 6, "Diffusivity matrix should have 6 components"
        return array


class DiffusivityParams(BaseModel):
    """
    Diffusivity matrix defined by parameters.

    The parameters are passed on to :py:func:`pigreads.diffusivity_matrix`.
    """

    f: list[int] | None = None
    "main direction of diffusion"
    n: list[int] | None = None
    "direction of weakest diffusion"
    Df: float
    "diffusivity in the direction of the fibres"
    Ds: float | None = None
    "diffusivity in the fibre sheets"
    Dn: float | None = None
    "diffusivity in the direction normal to the fibre sheets"
    model_config = ConfigDict(extra="forbid")

    def __call__(self) -> np.ndarray[Any, Any]:
        """
        Create the diffusivity matrix from the parameters.

        :return: diffusivity matrix
        """
        return diffusivity_matrix(**dict(self))


Diffusivity = Union[DiffusivityFile, DiffusivityParams]
"""
The diffusivity matrix is a command to define the diffusivity matrix in the
simulation.

One of:

- :py:class:`DiffusivityFile`
- :py:class:`DiffusivityParams`
"""


class SignalStep(BaseModel):
    """
    Within a time interval, increase the value of variables by a given amounts.

    The start and duration of the signal are given in time units of the
    simulation. The variables are given as a dictionary with the variable names
    as keys and the amount to increase the variable by as values::

        start: 100 # ms
        duration: 10 # ms
        variables:
          u: 1
          v: 2

    The interval is defined mathematically as
    :math:`t \\in [\\text{start}, \\text{start} + \\text{duration})`.
    """

    start: float = 0
    "starting time of the signal"
    duration: float = 0
    "duration of the signal"
    variables: dict[str, float] = Field(default_factory=dict)
    "variables to modify and the amount to modify them by"
    model_config = ConfigDict(extra="forbid")

    def __call__(
        self,
        signal: np.ndarray[Any, Any],
        times: np.ndarray[Any, Any],
        varidx: dict[str, int],
    ) -> np.ndarray[Any, Any]:
        """
        Modify the signal array.

        The signal array is modified in place to increase the values of the
        variables by the given amounts within the time interval.

        :param signal: signal array to modify
        :param times: times of the signal steps
        :param varidx: mapping of variable names to indices in the signal array,
                       see :py:meth:`Simulation.varidx`
        :return: modified signal array
        """
        mask = (self.start <= times) * (times < self.start + self.duration)
        for varname, value in dict(self.variables).items():
            signal[mask, varidx[varname]] += value
        return signal


class Stimulus(BaseModel):
    """
    A stimulus is a combination of a shape and a signal.

    The shape is defined by a list of :py:class:`pigreads.schema.setter.Setter` objects and defines
    where the stimulus is applied. The signal is defined by a list of
    :py:class:`SignalStep` objects and defines how the stimulus changes over
    time.
    """

    shape: list[Setter] = Field(default_factory=list)
    "shape of the stimulus"
    signal: list[SignalStep] = Field(default_factory=list)
    "signal of the stimulus"
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalise_setters(cls, values: Any) -> Any:
        """
        Normalise the setters in the shape.

        See :py:func:`pigreads.schema.setter.normalise_list_of_setters` for details.
        """

        shape = values.get("shape")
        if shape is not None:
            values["shape"] = normalise_list_of_setters(shape)
        return values


def is_dict_of_dicts(d: dict[Any, Any], excluded_keys: list[Any] | None = None) -> bool:
    """
    Check if a value of a dictionary is also a dictionary.

    :param d: dictionary to check
    :param excluded_keys: Ignore values who's key is in excluded_keys.
    :return: True if it is a dictionary of dictionaries
    """
    return next(
        (
            True
            for k, v in d.items()
            if k not in (excluded_keys or []) and isinstance(v, dict)
        ),
        False,
    )


class Simulation(BaseModel):
    """
    Definition of a simulation.

    The simulation is defined on a three dimensional cuboid with :py:attr:`Nz`,
    :py:attr:`Ny`, and :py:attr:`Nx` grid points in the z, y, and x directions
    respectively. The grid points are separated by :py:attr:`dz`, :py:attr:`dy`,
    and :py:attr:`dx` units in the z, y, and x directions. The simulation is
    run for :py:attr:`Nfr` frames with :py:attr:`Nt` time steps per frame.
    Each time step is :py:attr:`dt` units long.

    The simulation definion contains a list of :py:class:`ModelEntry` objects
    (:py:attr:`models`) which define the reaction terms in the
    reaction-diffusion equation. See also :py:class:`pigreads.Models`.

    The diffusivity matrix is defined by a :py:class:`Diffusivity` object.

    The inhomogeneity (:py:attr:`inhom`) of the medium, i.e. which parts of the
    simulation are active and which model to use where is defined by a list of
    :py:class:`pigreads.schema.setter.Setter` objects.

    The initial state of the simulation is defined by a dictionary of
    :py:class:`pigreads.schema.setter.Setter` objects. The keys of the
    dictionary are the variable names and the values are lists of setters.

    A stimulus protocol is defined by a list of :py:class:`Stimulus` objects.

    The flag :py:attr:`double_precision` can be set to `True` to use double
    precision floating point numbers in the simulation.

    The required key :py:attr:`pigreads` is used to identify the simulation
    file format.

    The simulation can be run by calling the :py:meth:`run` method.

    Example::

        pigreads: 1
        Nfr: 100
        Nt: 200
        Nz: 1
        Ny: 200
        Nx: 200
        dt: 0.025
        dz: 1
        dy: 0.1
        dx: 0.1
        inhom:
        - spherical:
            outside: 0
        diffusivity: 0.03
        models:
        - marcotte2017dynamical:
            diffusivity_u: 1.0
            diffusivity_v: 0.05
        init:
            u:
                slices:
                    value: 1
                    axis: -1
                    end: 10
            v:
                slices:
                    value: 2
                    start: 100
                    axis: -2

    Read this and run a simulation like this::

        from pigreads.schema import Simulation
        data = yaml.safe_load(yaml_string)
        sim = Simulation(**data)
        sim.run(path="result.npy")

    Or use the CLI:

        $ pigreads run config.yaml result.npy

    """

    pigreads: Literal[1]
    "identifier for the simulation file format"

    Nfr: int = Field(..., ge=1)
    "number of frames"
    Nt: int = Field(..., ge=1)
    "number of time steps per frame"
    Nz: int = Field(..., ge=1)
    "number of grid points in z direction"
    Ny: int = Field(..., ge=1)
    "number of grid points in y direction"
    Nx: int = Field(..., ge=1)
    "number of grid points in x direction"

    dt: float = Field(..., gt=0)
    "time step"
    dz: float = Field(..., gt=0)
    "grid spacing in z direction"
    dy: float = Field(..., gt=0)
    "grid spacing in y direction"
    dx: float = Field(..., gt=0)
    "grid spacing in x direction"

    models: list[ModelEntry]
    """
    Definition of the models to use in the simulation.

    The models define the reaction terms in the reaction-diffusion equation.

    :see: :py:class:`pigreads.Models`, :py:meth:`prepare_models`
    """

    diffusivity: Diffusivity
    """
    Definition of the diffusivity matrix.

    :see: :py:func:`pigreads.diffusivity_matrix`
    """

    inhom: list[Setter] = Field(default_factory=list)
    """
    Definition of the inhomogeneity of the medium.

    It defines which parts of the simulation are active and which model to
    use where.

    :see: :py:class:`pigreads.schema.setter.Setter`, :py:meth:`prepare_inhom`,
          :py:func:`pigreads.weights`
    """

    init: dict[str, list[Setter]] | SetterFile = Field(
        default_factory=dict,  # type: ignore[arg-type]
    )
    """
    Definition of the initial state of the simulation.

    The initial state is defined by a dictionary of variable names and lists
    of setters.

    :see: :py:class:`pigreads.schema.setter.Setter`, :py:meth:`prepare_states`
    """

    stim: list[Stimulus] = Field(default_factory=list)
    """
    Definition of the stimulus protocol.

    The stimulus protocol is defined by a list of :py:class:`Stimulus` objects.

    :see: :py:class:`Stimulus`, :py:meth:`prepare_stim`
    """

    double_precision: bool = False
    "flag to use single or double precision floating point numbers"

    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalise_models(cls, values: Any) -> Any:
        """
        Normalise the models.

        Normally, the models are given as a list of :py:class:`ModelEntry`.

        Alternatively, if the models are given as a string, it is converted to
        a list with a single model entry. If the models are given as a
        dictionary, it is converted to a list of model entries. If the models
        are given as a list of strings, they are converted to a list of model
        entries with empty parameter sets.

        :param values: any data to try to interpret
        :return: normalised data
        """
        models = values.get("models")
        if models is None:
            return values
        if isinstance(models, dict):
            if is_dict_of_dicts(models, excluded_keys=["name", "parameters"]):
                models = [
                    ModelEntry(name=k, parameters=v or {}) for k, v in models.items()
                ]
            else:
                models = [ModelEntry(**models)]
        elif isinstance(models, str):
            models = [ModelEntry(name=models, parameters={})]
        elif isinstance(models, list):
            models = [
                ModelEntry(**model)
                if isinstance(model, dict)
                else ModelEntry(name=model, parameters={})
                for model in models
            ]
        values["models"] = models
        return values

    @model_validator(mode="before")
    @classmethod
    def normalise_diffusivity(cls, values: Any) -> Any:
        """
        Normalise the diffusivity.

        Normally, the diffusivity is given as an instance of :py:class:`Diffusivity`.

        Alternatively, if the diffusivity is given as a string, read the
        diffusivity matrix from the file. If the diffusivity is given as a
        float, set the diffusivity matrix to a constant value.

        :param values: any data to try to interpret
        :return: normalised data
        """

        diffusivity = values.get("diffusivity")
        if isinstance(diffusivity, str):
            diffusivity = {"file": diffusivity}
        elif isinstance(diffusivity, float) or isinstance(diffusivity, int):  # noqa: SIM101  # pylint: disable=consider-merging-isinstance
            diffusivity = {"Df": diffusivity}
        values["diffusivity"] = diffusivity
        return values

    @model_validator(mode="before")
    @classmethod
    def normalise_setters(cls, values: Any) -> Any:
        """
        Normalise the setters.

        The inhomogeneity, initial state, and stimulus are given as lists of
        :py:class:`pigreads.schema.setter.Setter` objects.

        The setters are normalised using
        :py:func:`pigreads.schema.setter.normalise_list_of_setters`.

        :param values: any data to try to interpret
        :return: normalised data
        """
        inhom = values.get("inhom")
        if inhom is not None:
            values["inhom"] = normalise_list_of_setters(inhom)

        init = values.get("init")
        if init is not None:
            if isinstance(init, dict):
                for varname, setters in init.items():
                    if isinstance(setters, dict):
                        init[varname] = normalise_list_of_setters(setters)
                    elif isinstance(setters, float) or isinstance(setters, int):  # noqa: SIM101  # pylint: disable=consider-merging-isinstance
                        init[varname] = normalise_list_of_setters(
                            {"slices": {"axis": -1, "value": setters}}
                        )
                    elif isinstance(setters, str):
                        init[varname] = normalise_list_of_setters({"file": setters})
            else:
                assert isinstance(init, str) or isinstance(init, Path)  # noqa: SIM101  # pylint: disable=consider-merging-isinstance
                values["init"] = SetterFile(file=Path(init))

        return values

    @staticmethod
    def varidx(models: Models) -> dict[str, int]:
        """
        Create a dictionary mapping variable names to indices.

        The indices are used to access the variables in the state array.

        :param models: models object
        :return: mapping of variable names to indices
        """
        return {varname: i for i, varname in enumerate(models[0]["variables"])}

    def prepare_space(
        self,
    ) -> tuple[np.ndarray[Any, Any], np.ndarray[Any, Any], np.ndarray[Any, Any]]:
        """
        Get arrays with the coordinates of the grid points.

        The arrays are returned as a tuple of three arrays with the z, y, and x
        coordinates of the grid points.

        :return: z, y, x arrays
        :see: :py:func:`numpy.meshgrid`
        """
        z, y, x = np.meshgrid(
            self.dz * np.arange(self.Nz),
            self.dy * np.arange(self.Ny),
            self.dx * np.arange(self.Nx),
            indexing="ij",
        )
        return z, y, x

    def prepare_inhom(self) -> np.ndarray[Any, Any]:
        """
        Get the inhomogeneity array.

        The inhomogeneity array is created by applying the setters in the
        :py:attr:`inhom` list to an array of ones with the shape of the grid.

        The inhomogeneity array is used to define the active parts of the
        simulation and which model to use where.

        :return: inhomogeneity array
        """

        inhom: np.ndarray[Any, Any] = np.ones((self.Nz, self.Ny, self.Nx), dtype=int)
        for setter in self.inhom:
            inhom = setter(inhom, self)
        return inhom

    def prepare_models(self) -> Models:
        """
        Create a models object from the model entries.

        The model entries are used to create the models object which is used to
        run the simulation.

        :return: models object
        """

        models = Models()
        for model in self.models:
            models.add(model.name, **model.parameters)
        return models

    def prepare_states(
        self,
        models: Models,
        varidx: dict[str, int],
        inhom: np.ndarray[Any, Any],
        path: Path | str | None = None,
    ) -> np.ndarray[Any, Any]:
        """
        Prepare the state array.

        The state array is created as a five dimensional array with the shape
        ``(Nfr, Nz, Ny, Nx, Nv)`` where ``Nv`` is the number of variables in the
        model, see also :py:func:`pigreads.Models.Nv`.

        This array is created in three steps:

        1. Create a new array with the correct shape and dtype using
           :py:meth:`pigreads.prepare_array`.
        2. Set the first frame of the array to the resting state of the model,
           see :py:func:`pigreads.Models.resting_states`.
        3. Apply the initial state setters to the first frame of the array.

        The array is returned as a memory map if a path is given, otherwise as a
        normal numpy array.

        :param models: models object
        :param varidx: mapping of variable names to indices in the state array
        :param inhom: inhomogeneity array
        :param path: path to memory map the state array to
        :return: state array
        """

        states = prepare_array(
            shape=(self.Nfr, self.Nz, self.Ny, self.Nx, len(varidx)),
            path=path,
            dtype=np.float32,
        )
        states[0] = models.resting_states(inhom, Nframes=1)

        if isinstance(self.init, SetterFile):
            states[0] = self.init(states[0], self)

        else:
            assert isinstance(self.init, dict)
            for varname, setters in dict(self.init).items():
                for setter in setters:
                    idx = varidx[varname]
                    states[0, ..., idx] = setter(states[0, ..., idx], self)

        return states

    def prepare_stim(
        self, varidx: dict[str, int]
    ) -> tuple[np.ndarray[Any, Any], np.ndarray[Any, Any]]:
        """
        Prepare the stimulus signal and shape.

        The stimulus signal is created as a three dimensional array with the
        shape ``((Nfr - 1)*Nt, Ns, Nv)`` where ``Ns`` is the number of

        stimuli in the simulation and ``Nv`` is the number of variables in the
        model, see also :py:func:`pigreads.Models.Nv`.
        This array is first set to zero and then modified by the signal steps
        in the stimulus objects, see :py:class:`SignalStep` and :py:class:`Stimulus`.

        The stimulus shape is created as a four dimensional array with the
        shape ``(Ns, Nz, Ny, Nx)`` where ``Ns`` is the number of stimuli in the
        simulation. This array is first set to zero and then modified by the
        shape setters in the stimulus objects, see
        :py:class:`pigreads.schema.setter.Setter` and :py:class:`Stimulus`.

        The stimulus signal and shape are returned as a tuple.

        :param varidx: mapping of variable names to indices in the state array
        :return: stimulus signal and shape
        """

        Nt: int = (self.Nfr - 1) * self.Nt  # pylint: disable=invalid-name
        Ns: int = len(self.stim)  # pylint: disable=invalid-name
        Nv: int = len(varidx)  # pylint: disable=invalid-name

        stim_signal = np.zeros((Nt, Ns, Nv))
        times = self.dt * np.arange(Nt)
        for i, stimulus in enumerate(self.stim):
            for step in stimulus.signal:
                stim_signal[:, i, :] = step(stim_signal[:, i, :], times, varidx)

        stim_shape = np.zeros((Ns, self.Nz, self.Ny, self.Nx), dtype=float)
        for i, stimulus in enumerate(self.stim):
            for setter in stimulus.shape:
                stim_shape[i] = setter(stim_shape[i], self)

        return stim_signal, stim_shape

    def run(
        self,
        path: Path | str | None = None,
        start_frame: int = 0,
        progress: Callable[[Any], Any] = lambda x: x,
        callback: Callable[[np.ndarray[Any, Any], int], None] | None = None,
    ) -> np.ndarray[Any, Any]:
        """
        Run the simulation.

        :param start_frame: The frame to start the simulation at, default is 0.
        :param path: The path to save the state array to, default is ``None``,
                     see :py:meth:`pigreads.prepare_array`.
        :param progress: A function to show progress, default is no progress updates.
        :param callback: A function to call after each frame, default is no callback.
        :return: The results in the state array with the shape ``(Nfr, Nz, Ny, Nx, Nv)``.

        The simulation calls the following methods to prepare the simulation:

        - :py:meth:`prepare_inhom`
        - :py:meth:`prepare_models`
        - :py:meth:`prepare_states`
        - :py:meth:`prepare_stim`
        - :py:meth:`pigreads.weights`

        The simulation is then run frame by frame using the :py:func:`pigreads.run` function.
        The results are saved to the state array and returned.

        :see: :py:func:`pigreads.run`
        """

        inhom = self.prepare_inhom()
        models = self.prepare_models()
        varidx = self.varidx(models)
        states = self.prepare_states(models, varidx, inhom, path=path)
        stim_signal, stim_shape = self.prepare_stim(varidx)
        weights = calc_weights(
            self.dz, self.dy, self.dx, inhom, diffusivity=self.diffusivity()
        )

        if callback is not None:
            callback(states, 0)

        for ifr in progress(range(start_frame, states.shape[0] - 1)):
            states[ifr + 1] = run(
                models,
                inhom,
                weights,
                states[ifr],
                stim_signal[ifr * self.Nt : (ifr + 1) * self.Nt],
                stim_shape,
                Nt=self.Nt,
                dt=self.dt,
                double_precision=self.double_precision,
            )

            if callback is not None:
                callback(states, ifr + 1)

            if np.any(np.isfinite(states[ifr]) > np.isfinite(states[ifr + 1])):
                warn(
                    f"New non-finite values found at frame {ifr + 1}!",
                    RuntimeWarning,
                    stacklevel=2,
                )

        return states
