from typing import Dict, Optional, List, Union, Any

import numpy as np
from matplotlib.ticker import PercentFormatter

from geoassistant.statistics.histogram.Histogram import Histogram


class CategoricHistogram(Histogram):

    def __init__(self, name: Optional[str] = None):
        super().__init__(name=name)

        self.categories: Optional[List[Any]] = None

        self.categories_colors: Optional[Dict[Any, str]] = None

    def setCategories(self, categories: List[Union[int, float, str]]) -> None:
        self.categories = categories

    def createPlot(self) -> None:

        if self.categories is None:
            self.categories = list(set(self.data))
            if len(self.categories) > 30:
                raise ValueError(f"Too many categories for an histograms ({len(self.categories)})")

        if isinstance(self.data, list):
            counts = [self.data.count(cat) for cat in self.categories]
        else:
            counts = [np.count_nonzero(self.data == cat) for cat in self.categories]

        categories_txts = [str(v) for v in self.categories]

        if self.is_relative:
            percs = [float(c) / len(self.data) for c in counts]
            self.ax.bar(categories_txts, percs, color=self.categories_colors, label=self.label)
            self.ax.yaxis.set_major_formatter(PercentFormatter(1, decimals=0))
        else:
            self.ax.bar(categories_txts, counts, color=self.categories_colors, label=self.label)

        if self.label is not None:
            self.ax.legend()

