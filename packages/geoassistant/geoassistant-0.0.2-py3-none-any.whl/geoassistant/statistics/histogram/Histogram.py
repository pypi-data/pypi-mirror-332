from abc import ABC, abstractmethod
from typing import Optional, Union, List, Any

import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter, PercentFormatter

from geoassistant.shared.BaseObject import BaseObject
from geoassistant.statistics.histogram.HistogramProperties import HistogramProperties


class Histogram(BaseObject, HistogramProperties, ABC):
    """
    Custom histogram handler.
    Steps: Initiate, load data, plot, show
    """
    def __init__(self, name: Optional[str]):
        super().__init__(name=name)

        self._initiate()

    @abstractmethod
    def createPlot(self) -> None: ...

    def _initiate(self):
        self.figure = plt.figure()
        self.ax = self.figure.add_subplot()
        self._setupAxesLabels()

    def _setupAxesLabels(self) -> None:
        self.ax.set_xlabel('Values')
        self.ax.set_ylabel('Frecuency')

        formatter = FuncFormatter(lambda x, pos: f'{int(x):,}')
        self.ax.yaxis.set_major_formatter(formatter)

    def show(self) -> None:
        self.createPlot()

        self.figure.tight_layout()
        if self.figure:
            plt.show()

    def save(self, savepath: str) -> None:
        self.createPlot()

        plt.savefig(savepath, bbox_inches="tight", dpi=110)
        self.close()

    def close(self) -> None:
        plt.close(self.figure)
