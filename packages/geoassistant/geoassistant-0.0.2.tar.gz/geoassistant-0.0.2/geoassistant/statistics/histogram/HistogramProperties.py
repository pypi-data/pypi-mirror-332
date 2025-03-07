from typing import Optional, Union, Any, List

import numpy as np
from matplotlib import pyplot as plt


class HistogramProperties(object):

    def __init__(self):
        self.figure: Optional[plt.Figure] = None
        self.ax: Optional[plt.Axes] = None

        self.label: Optional[str] = None

        self.data: Optional[Union[np.ndarray, List[Any]]] = None
        self.bins: Optional[int] = None

        self.is_relative: Optional[bool] = False

        self.color: Optional[str] = None

    def setLabel(self, label: str) -> None:
        self.label = label

    def setData(self, data: Union[np.ndarray, List[Any]]) -> None:
        self.data = data

    def setBins(self, bins: Union[np.ndarray, List[Any]]) -> None:
        self.bins = bins

    def setIsRelative(self, is_relative: bool) -> None:
        self.is_relative = is_relative

    def setColor(self, color: str) -> None:
        self.color = color

    def getFigure(self) -> Optional[plt.Figure]:
        return self.figure

    def getAx(self) -> Optional[plt.Axes]:
        return self.ax

    def isRelative(self) -> bool:
        return self.is_relative
