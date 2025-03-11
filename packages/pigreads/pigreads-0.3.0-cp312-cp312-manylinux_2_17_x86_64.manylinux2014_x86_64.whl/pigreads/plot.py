"""
Plots and movies
----------------
"""

from __future__ import annotations

import multiprocessing
import subprocess
import time
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Any

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FFMpegWriter
from matplotlib.axes import Axes
from matplotlib.colorbar import Colorbar
from matplotlib.image import AxesImage

from pigreads import Models
from pigreads.progress import PROGRESS_ITERS
from pigreads.schema import Simulation


def get_iz_iv(
    sim: Simulation,
    models: Models,
    variable: str | int | None,
    index_z: int | None,
) -> tuple[int, int]:
    """
    Interpret z index and variable index from command line arguments.

    :param sim: simulation object
    :param models: models object
    :param variable: variable name or index
    :param index_z: index in z direction
    :return: tuple of z index and variable index
    """

    iz: int = sim.Nz // 2 if index_z is None else index_z
    iv: int

    try:
        iv = int(variable or 0)

        if iv < 0 or models.Nv <= iv:
            message = "Invalid variable index"
            raise ValueError(message)

    except ValueError:
        iv = 0 if variable is None else sim.varidx(models)[str(variable)]

    if iz < 0 or iz >= sim.Nz:
        message = "Invalid z index"
        raise ValueError(message)

    return iz, iv


def imshow_defaults(
    array: np.ndarray[Any, Any] | None = None,
    sim: Simulation | None = None,
    **kwargs: Any,
) -> dict[str, Any]:
    """
    Set default imshow arguments.

    :param array: array to display
    :param sim: simulation object
    :param kwargs: additional arguments
    :return: dictionary of arguments for
             :py:func:`matplotlib.pyplot.imshow`
    """

    if "origin" not in kwargs:
        kwargs["origin"] = "lower"

    if "interpolation" not in kwargs:
        kwargs["interpolation"] = "none"

    if array is not None:
        if "vmin" not in kwargs:
            kwargs["vmin"] = np.nanmin(array)

        if "vmax" not in kwargs:
            kwargs["vmax"] = np.nanmax(array)

    if sim is not None and "extent" not in kwargs:
        kwargs["extent"] = (
            -0.5 * sim.dx,
            (sim.Nx + 0.5) * sim.dx,
            -0.5 * sim.dy,
            (sim.Ny + 0.5) * sim.dy,
        )

    return kwargs


def plot_frame(
    ax: Axes,
    frame: np.ndarray[Any, Any],
    xlabel: str = "x",
    ylabel: str = "y",
    vlabel: str = "",
    title: str = "",
    **kwargs: Any,
) -> tuple[AxesImage, Colorbar]:
    """
    Display a frame as an image.

    :param ax: axes object
    :param xlabel: x-axis label
    :param ylabel: y-axis label
    :param vlabel: colorbar label
    :param title: title of the plot
    :param frame: frame to display
    :param kwargs: passed to :py:func:`matplotlib.pyplot.imshow`

    :return: image and colorbar objects
    """
    assert frame.ndim == 2
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    im = ax.imshow(frame, **imshow_defaults(array=frame, **kwargs))
    cbar = plt.colorbar(im)
    cbar.set_label(vlabel)
    return im, cbar


def movie(
    path: str,
    frames: np.ndarray[Any, Any],
    dpi: int = 180,
    fps: int = 15,
    tlables: list[str] | None = None,
    progress: str = "none",
    progress_dict: dict[str, int] | None = None,
    parallel: int = 1,
    **kwargs: Any,
) -> None:
    """
    Render a chunk of frames to a movie file, with optional parallelization.

    :param path: path to write the movie file to
    :param frames: array of frames
    :param dpi: dots per inch
    :param fps: frames per second
    :param tlables: list of time labels
    :param progress: progress bar type
    :param progress_dict: dictionary to store progress
    :param parallel: number of processes (default 1, 0 to use all CPUs)
    :param kwargs: passed to :py:func:`plot_frame`
    """
    assert frames.ndim == 3

    if parallel == 1:
        fig, ax = plt.subplots(dpi=dpi)
        writer = FFMpegWriter(fps=fps)
        tlables = [f"{i}" for i, _ in enumerate(frames)] if tlables is None else tlables
        im, _ = plot_frame(ax, frames[0], **imshow_defaults(array=frames, **kwargs))

        prog = PROGRESS_ITERS[progress]
        with writer.saving(fig, path, fig.dpi):
            for (i, frame), tlabel in zip(enumerate(prog(frames)), tlables):
                ax.set_title(tlabel)
                im.set_data(frame)
                writer.grab_frame()
                if progress_dict is not None:
                    progress_dict[path] = i + 1
        return

    Np = multiprocessing.cpu_count() if parallel == 0 else parallel  # pylint: disable=invalid-name
    Nfr = len(frames)  # pylint: disable=invalid-name
    Nfrp = (Nfr + Np - 1) // Np  # pylint: disable=invalid-name
    chunks = [slice(i, min(i + Nfrp, Nfr)) for i in range(0, Nfr, Nfrp)]

    with TemporaryDirectory() as temp:
        with multiprocessing.Manager() as manager:
            paths = [str(Path(temp) / f"{i}.mp4") for i, _ in enumerate(chunks)]
            assert progress_dict is None
            progress_dict_ = manager.dict({path: 0 for path in paths})
            tasks = [
                [
                    {
                        "path": path,
                        "frames": frames[chunk],
                        "tlables": tlables[chunk] if tlables else None,
                        "progress_dict": progress_dict_,
                        "parallel": 1,
                        **kwargs,
                    }
                ]
                for path, chunk in zip(paths, chunks)
                if chunk.start < chunk.stop
            ]

            progress_proc = multiprocessing.Process(
                target=movie_progress_updater,
                args=(progress, Nfr, progress_dict_),
            )
            progress_proc.start()

            with multiprocessing.Pool(processes=Np) as pool:
                pool.starmap_async(movie_wrapper, tasks).get()

            progress_proc.join()

        pathlist = Path(temp) / "files.txt"
        with pathlist.open("w") as f:
            for p in paths:
                f.write(f"file '{p}'\n")

        proc = subprocess.Popen(  # pylint: disable=consider-using-with
            [
                "ffmpeg",
                "-y",
                "-f",
                "concat",
                "-safe",
                "0",
                "-i",
                pathlist,
                "-c",
                "copy",
                str(path),
            ],
            stderr=subprocess.PIPE,
        )

        _, stderr = proc.communicate()
        if proc.returncode != 0:
            raise RuntimeError(stderr.decode())


def movie_wrapper(kwargs: dict[str, Any]) -> None:
    """
    Wrapper for movie to allow for multiprocessing.

    :param kwargs: keyword arguments for :py:func:`movie`
    """
    return movie(**kwargs)


def movie_progress_updater(
    progress: str, total: int, progress_dict: dict[str, int]
) -> None:
    """
    Update the progress bar for a movie.

    :param progress: progress bar type
    :param total: total number of frames
    :param progress_dict: dictionary to store progress
    """
    prog = PROGRESS_ITERS[progress]
    for i in prog(range(total)):
        while sum(progress_dict.values()) < i:
            time.sleep(0.1)


class LiveView:
    """
    Live view for a simulation.

    Plot a single variable at a fixed z index in an interactive window or save
    it to a file.

    :param sim: simulation object
    :param variable: variable name or index
    :param index_z: index in z direction
    :param dpi: dots per inch
    :param path: file path
    :param click_radius: radius of click region
    :param click_value: value to add continuously while clicking
    :param style: style sheet,
                  passed to :py:func:`matplotlib.style.use`,
                  for example ``dark background``
    :param kwargs: additional arguments to pass to :py:func:`plot_frame` and
                   :py:func:`matplotlib.pyplot.imshow`

    :ivar sim: simulation object
    :ivar fig: figure object
    :ivar ax: axes object
    :ivar models: models object
    :ivar iz: index in z direction
    :ivar iv: index of variable
    :ivar click_radius: radius of click region
    :ivar click_value: value to add continuously while clicking
    :ivar click_location: location of last click
    :ivar mouse_pressed: flag indicating whether the mouse is pressed
    :ivar kwargs: additional arguments
    :ivar path: file path
    :ivar im: image object
    :ivar cbar: colorbar object
    """

    def __init__(
        self,
        sim: Simulation,
        variable: str | int | None = None,
        index_z: int | None = None,
        dpi: int | None = None,
        path: Path | str | None = None,
        click_radius: float | None = None,
        click_value: float | None = None,
        style: str | None = None,
        **kwargs: Any,
    ) -> None:
        if style is not None:
            plt.style.use(style)

        self.sim = sim
        self.kwargs = kwargs
        self.fig, self.ax = plt.subplots(dpi=dpi)
        plt.tight_layout()
        self.models = sim.prepare_models()
        self.iz, self.iv = get_iz_iv(sim, self.models, variable, index_z)
        self.kwargs = {
            "vlabel": list(self.models[0]["variables"])[self.iv],
            **imshow_defaults(sim=sim, **kwargs),
        }
        self.path = path
        self.im: AxesImage | None = None
        self.cbar: Colorbar | None = None
        self.fig.show()

        self.click_radius = click_radius
        self.click_value = click_value
        self.click_location: tuple[int, int] | None = None
        self.click_location_prev: tuple[int, int] | None = None
        self.mouse_pressed = False

        self.fig.canvas.mpl_connect("button_press_event", self.on_press)
        self.fig.canvas.mpl_connect("motion_notify_event", self.on_motion)
        self.fig.canvas.mpl_connect("button_release_event", self.on_release)

    def on_press(self, event: Any) -> None:
        """
        Handle mouse button press: store click location and set press flag.
        """
        if (
            self.click_radius is None
            or self.click_value is None
            or event.inaxes != self.ax
            or event.xdata is None
            or event.ydata is None
        ):
            return
        self.click_location = (event.ydata, event.xdata)
        self.mouse_pressed = True

    def on_motion(self, event: Any) -> None:
        """
        Handle mouse motion: draw a thick line between previous and current locations.
        """
        if (
            self.click_radius is None
            or self.click_value is None
            or not self.mouse_pressed
            or event.inaxes != self.ax
            or event.xdata is None
            or event.ydata is None
        ):
            return
        self.click_location = (event.ydata, event.xdata)

    def on_release(self, _: Any) -> None:
        """
        Handle mouse button release: clear press flag.
        """
        if self.click_radius is None or self.click_value is None:
            return
        self.mouse_pressed = False
        self.click_location = None
        self.click_location_prev = None

    def draw_thick_line(self, frame: np.ndarray[Any, Any]) -> None:
        """
        Draw a thick line between the previous and new locations with the given radius.
        """
        if (
            self.click_radius is None
            or self.click_value is None
            or self.click_location is None
        ):
            return

        y1, x1 = self.click_location
        y2, x2 = self.click_location

        if self.click_location_prev is not None:
            y2, x2 = self.click_location_prev

        dx, dy = x2 - x1, y2 - y1

        y, x = np.meshgrid(
            self.sim.dy * np.arange(self.sim.Ny),
            self.sim.dx * np.arange(self.sim.Nx),
            indexing="ij",
        )

        distance = np.abs(+dy * x - dx * y + x2 * y1 - y2 * x1) / np.linalg.norm(
            (dy, dx), axis=0
        )

        t = ((x - x1) * dx + (y - y1) * dy) / (dx**2 + dy**2)

        mask = (distance <= self.click_radius) & (t >= 0) & (t <= 1)

        for y_, x_ in [(y1, x1), (y2, x2)]:
            mask[np.linalg.norm([y - y_, x - x_], axis=0) <= self.click_radius] = True

        frame[mask] += self.click_value
        self.click_location_prev = self.click_location

    def update(self, states: np.ndarray[Any, Any], ifr: int) -> None:
        """
        Update the live view.

        :param states: array of states with shape (Nfr, Nz, Ny, Nx, Nv)
        :param ifr: index of frame
        """

        frame = states[ifr, self.iz, :, :, self.iv]

        self.draw_thick_line(frame)

        if self.im is None:
            self.im, self.cbar = plot_frame(
                self.ax, frame, **imshow_defaults(array=frame, **self.kwargs)
            )

        else:
            assert self.cbar is not None
            vmin, vmax = self.im.get_clim()
            vmin = self.kwargs.get("vmin", np.nanmin([vmin, np.nanmin(frame)]))
            vmax = self.kwargs.get("vmax", np.nanmax([vmax, np.nanmax(frame)]))
            self.im.set_data(frame)
            self.im.set_clim(vmin, vmax)
            self.cbar.mappable.set_clim(vmin, vmax)
            self.cbar.update_normal(self.im)

        self.ax.set_title(
            f"frame {ifr}/{self.sim.Nfr}, t = {ifr * self.sim.Nt * self.sim.dt:.2f}"
        )
        if self.path is None:
            self.fig.canvas.draw_idle()
            self.fig.canvas.flush_events()
        else:
            self.fig.savefig(str(self.path))
