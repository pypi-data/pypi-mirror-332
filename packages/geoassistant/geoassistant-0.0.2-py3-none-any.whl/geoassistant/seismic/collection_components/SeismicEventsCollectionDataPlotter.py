from typing import TYPE_CHECKING, List, Dict, Tuple

import numpy as np
from matplotlib import pylab as py

from geoassistant.seismic.collection_components.data_plots.GutenbergRitcherPlot import GutenbergRitcherPlot
from geoassistant.seismic.collection_components.data_plots.HazardCurvePlot import HazardCurvePlot

if TYPE_CHECKING:
    from geoassistant.seismic.SeismicEventsCollection import SeismicEventsCollection


class SeismicEventsCollectionDataPlotter(object):

    def __init__(self, collection: 'SeismicEventsCollection'):
        super().__init__()

        self.collection: 'SeismicEventsCollection' = collection

    def plotGR(self, interval: float) -> None:
        GutenbergRitcherPlot(collection=self.collection, interval=interval)

    def plotHazardCurve(self) -> None:
        HazardCurvePlot(collection=self.collection).plot()
