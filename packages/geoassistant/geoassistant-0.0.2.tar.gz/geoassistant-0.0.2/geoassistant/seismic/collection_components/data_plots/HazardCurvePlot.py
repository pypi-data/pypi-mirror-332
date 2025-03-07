from typing import TYPE_CHECKING, Optional

import matplotlib.pyplot as plt
import numpy as np

if TYPE_CHECKING:
    from geoassistant.seismic.SeismicEventsCollection import SeismicEventsCollection


class HazardCurvePlot(object):

    def __init__(self, collection: 'SeismicEventsCollection'):
        self.collection: 'SeismicEventsCollection' = collection

        self.max_logP: Optional[float] = None
        self.max_P: Optional[float] = None

        self.min_magnitude = -1.5
        self.max_magnitude = 10 ** (2.3)

        self.a = 2.498
        self.b = 1.017

        self.alpha = 10 ** self.a
        self.beta = 10 ** self.b

        self.days = 269

        self.alpha_per_year = self.alpha * (365.25 / self.days)

        self.magnitudes, self.rates = self.getAnnualRateOfExceedance()

    def getAnnualRateOfExceedance(self):
        magnitudes = np.arange(self.min_magnitude, 3.1, step=0.1)
        magnitudes2 = 10 ** magnitudes

        rates = self.alpha_per_year * ((magnitudes2 ** (-self.beta)) - (self.max_magnitude ** (-self.beta)))

        return magnitudes, rates

    def plot(self) -> None:

        fig = plt.figure()
        ax: plt.Axes = fig.add_subplot(111)

        regions_parameters = {
            "Almost Certain": {'color': 'brown', 'y_limits': [2, 10], 'y_center': 3.5},
            "Likely": {'color': 'red', 'y_limits': [1, 2], 'y_center': 1.25},
            "Possible": {'color': 'orange', 'y_limits': [0.1, 1], 'y_center': 0.25},
            "Unlikely": {'color': 'green', 'y_limits': [1e-2, 0.1], 'y_center': 0.025},
            "Rare": {'color': 'lime', 'y_limits': [1e-3, 1e-2], 'y_center': 0.0025},
        }

        for region_id, r_parameters in regions_parameters.items():
            ax.axhspan(ymin=r_parameters['y_limits'][0], ymax=r_parameters['y_limits'][1],
                       facecolor=r_parameters['color'],
                       alpha=0.5,
                       edgecolor="none",
                       zorder=-1)

            ax.text(x=0, y=r_parameters['y_center'], s=region_id, ha='center')

        ax.plot(self.magnitudes, self.rates, c='black', zorder=20)

        ax.set_yscale('log')

        ax.set_ylim(1e-3, 10)
        ax.set_xlim(-1.5, 3)

        ax.set_ylabel('Annual rate of exceedance')
        ax.set_xlabel('Local Magnitude')

        ax.grid()

        plt.show()

