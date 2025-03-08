from dataclasses import dataclass

from datetime import datetime

from os import PathLike
from typing import Literal, TypedDict, Annotated
import numpy as np
import numpy.typing as npt

import logging

logger = logging.getLogger(name="readerDAS")


@dataclass
class Parameters:
    position_step_m: float
    time_step_s: float
    position_start_m: float
    start_time: datetime
    scans_per_block: int
    settings: dict


class SectionInfo(TypedDict):
    name: str
    start_m: float
    stop_m: float
    position_samples: int


@dataclass
class SliceFile:
    file_index: int
    file_name: str | PathLike
    first_sample: int
    last_sample: int


DataType = Literal["magnitude", "phase"]
Energy = Annotated[npt.ArrayLike, "Energy. 2d array (times, position)."]
AxisTime = Annotated[npt.ArrayLike, "Time axis, UTC"]


@dataclass
class Data:
    """Classe dei dati caricati."""

    files: list[str | PathLike]
    section: str
    type: DataType
    data: npt.ArrayLike
    parameters: Parameters
    axis_time_utc: npt.ArrayLike
    axis_position_m: npt.ArrayLike
    remove_steps: bool = False

    @property
    def shape(self) -> list[int]:
        """Dimensioni del data caricato. (tempo, posizione)"""
        return np.shape(self.data)

    def __post_init__(self):
        if self.remove_steps:
            self._remove_block_steps()

    def _remove_block_steps(self):
        """Rimozione dei gradini tra ogni blocco, nella fase."""
        if self.type == "phase":
            logger.debug(
                f"Removing step of phase every {self.parameters.scans_per_block} samples..."
            )
            block_size = self.parameters.scans_per_block
            fine_blocchi = self.data[block_size - 1 :: block_size, :][:-1, :]
            fine_blocchi = np.insert(fine_blocchi, 0, 0, axis=0)
            inizio_blocchi = self.data[::block_size, :]

            delta_blocchi = fine_blocchi - inizio_blocchi
            delta_blocchi_cum = np.cumsum(delta_blocchi, axis=0)
            matrix_offset = np.repeat(delta_blocchi_cum, block_size, axis=0)
            self.data = self.data + matrix_offset

    def filter_by_position(self, position_m: float) -> tuple[npt.ArrayLike, float, int]:
        if (
            position_m < self.axis_position_m[0]
            or position_m > self.axis_position_m[-1]
        ):
            raise ValueError

        position_index = np.abs(self.axis_position_m - position_m).argmin()
        return (
            self.data[:, position_index],
            self.axis_position_m[position_index],
            position_index,
        )

    def energy(self, window_s: float = 0.512) -> tuple[Energy, AxisTime]:
        """
        Calcolo dell'energia del dato caricato, come somma dei quadrati lungo l'asse temporale.

        :param float window_s: finestra, in secondi, su cui è calcolata l'energia a blocchi.
        :return: energia e asse temporale, utc.
        :rtype: Energy, AxisTime
        """
        window_samples = int(window_s / self.parameters.time_step_s)
        n_segments = int(np.floor(self.shape[0] / window_samples))

        reshaped = self.data[: n_segments * window_samples, :].reshape(
            n_segments, window_samples, self.shape[1]
        )
        median = np.median(reshaped, axis=1)
        median_removed = reshaped - median[:, np.newaxis, :]
        energy = np.sum(np.square(np.abs(median_removed)), axis=1) / window_samples

        axis_time_utc_energy = self.axis_time_utc[::window_samples]

        return energy, axis_time_utc_energy

    def __str__(self) -> str:
        description = (
            f"data type: '{self.type}' from section: {self.section} - shape: {self.shape}"
            + f"\nfrom {self.parameters.position_start_m:.2f}m to {self.parameters.position_start_m+self.shape[1]*self.parameters.position_step_m:.2f}m"
            + f"\nfrom {self.axis_time_utc[0]} to {self.axis_time_utc[-1]}"
        )
        return description
