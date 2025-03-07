from typing import TYPE_CHECKING, Dict, Tuple, List, Optional

import numpy as np
import matplotlib.pyplot as plt

from geoassistant.seismic.SeismicEventsBins import SeismicEventsBins

if TYPE_CHECKING:
    from geoassistant.seismic.SeismicEventsCollection import SeismicEventsCollection


class GutenbergRitcherPlot(object):

    def __init__(self, collection: 'SeismicEventsCollection', interval: float = 0.1):
        self.collection: 'SeismicEventsCollection' = collection

        self.interval: float = interval
        self.num_years: int = 1

        self.annual_num_eq = len(self.collection) / self.num_years

        self.min_mag = self.collection.getMinimumLocalMagnitude()
        self.max_mag = self.collection.getMaximumLocalMagnitude()
        self.avg_mag = self.collection.getAverageLocalMagnitude()

        self.bins_collection = SeismicEventsBins.createBinsByLocalMagnitude(seismic_collection=self.collection, interval=self.interval)
        self.bins = self.bins_collection.getBinsArray()
        self.freq = self.bins_collection.getFrequenciesArray()

        cum_hist = self.freq[::-1].cumsum()
        self.new_cum_annual_rate = [i + 1e-20 for i in (cum_hist / self.num_years)]
        self.log_cum_sum = np.log10(self.new_cum_annual_rate)

        ls_solution = self.calculateLeastSquaresSolution()
        self.log_ls_fit, self.ls_bounded = self.calculateLeastSquaresArrays(solution=ls_solution)

        # mle_solution = self.calculateMaximumLikelihoodEstimatorSolution()
        # self.log_mle_fit, self.mle_bounded = self.calculateMaximumLikelihoodEstimatorArrays(solution=mle_solution)

        self.log_fit_data = self.getBaseArray()

        # self.plot()

    def calculateLeastSquaresSolution(self) -> Dict[str, float]:
        b, a = np.polyfit(self.bins_collection.getMidValuesArray(), self.log_cum_sum[::-1], 1)
        alpha = np.log(10) * a
        beta = - np.log(10) * b

        print('Least Squares: b value', -1. * b, 'a value', a)

        return {'a': a, 'b': -b, 'alpha': alpha, 'beta': beta}

    def calculateMaximumLikelihoodEstimatorSolution(self) -> Dict[str, float]:
        b = np.log10(np.exp(1)) / (self.avg_mag - self.min_mag)
        beta = np.log(10) * b

        print('Maximum Likelihood: b value', b)

        return {'b': b, 'beta': beta}

    def calculateLeastSquaresArrays(self, solution: Dict[str, float]) -> Tuple[List, np.ndarray]:
        yintercept = self.log_cum_sum[-1] + solution['b'] * self.min_mag
        ls_fit = yintercept - solution['b'] * self.bins
        log_ls_fit = 10 ** ls_fit

        ls_bounded = self.getBoundedArray(solution=solution)

        return log_ls_fit, ls_bounded

    def getLeastSquaresValueAtFrequency(self, solution: Dict[str, float], frequency: float) -> float:
        # Gutenber-Ritcher: log10(N) = a - b * M
        return (solution['a'] - frequency) / solution['b']

    def createLeastSquaresExtendedArrays(self, solution: Dict[str, float]) -> Tuple[np.ndarray, np.ndarray]:
        # x_value_1 = self.getLeastSquaresValueAtFrequency(solution=solution, frequency=10)
        # x_value_2 = self.getLeastSquaresValueAtFrequency(solution=solution, frequency=-1)

        centers = np.array([-5, 5.])
        frequencies = 10 ** (solution['a'] - solution['b'] * centers)

        return centers, frequencies

    def calculateMaximumLikelihoodEstimatorArrays(self, solution: Dict[str, float]) -> Tuple[List, np.ndarray]:
        mle_fit = - (solution['b'] * self.bins) + (solution['b'] * self.min_mag) + np.log10(self.annual_num_eq)
        log_mle_fit = 10 ** mle_fit

        mle_bounded = self.getBoundedArray(solution=solution)

        return log_mle_fit, mle_bounded

    def getBoundedArray(self, solution: Dict[str, float]) -> Tuple[np.ndarray, np.ndarray]:

        min_mag = self.bins_collection[0].getMidValue()
        max_mag = self.bins_collection[-1].getMidValue()

        max_mag = self.getLeastSquaresValueAtFrequency(solution=solution, frequency=0)

        constant = np.exp(- solution['beta'] * (max_mag - self.min_mag))

        magnitudes = self.bins_collection.getMidValuesArray()
        magnitudes = np.array(list(magnitudes) + [magnitudes[-1] + i*self.interval for i in range(20)])

        # numer = np.exp(- solution['beta'] * (self.bins_collection.getMidValuesArray() - min_mag)) - constant

        numer = np.exp(- solution['beta'] * (magnitudes - min_mag)) - constant
        denom = 1. - constant

        bounded_array = self.annual_num_eq * (numer / denom)
        return magnitudes, bounded_array

    def getBaseArray(self) -> List:
        # Compare b-value of 1
        fit_data = - self.bins + self.min_mag + np.log10(self.annual_num_eq)
        log_fit_data = 10 ** fit_data

        return log_fit_data

    def plot(self) -> None:
        fig = plt.figure()
        ax = fig.add_subplot(111)

        solution = self.calculateLeastSquaresSolution()

        ax.scatter(self.bins_collection.getMidValuesArray(), self.new_cum_annual_rate[::-1],
                   c='gray', s=25, label='Catalogue', edgecolors="black", linewidth=0.5, zorder=10)

        centers, frequencies = self.createLeastSquaresExtendedArrays(solution=solution)

        # ax.plot(self.bins, self.log_ls_fit, c='r', label='Least Squares')
        ax.plot(centers, frequencies, c='b', ls='-')

        magnitudes, ls_bounded = self.getBoundedArray(solution=solution)
        ax.plot(magnitudes, ls_bounded, c='b', linestyle='--')
        # ax.plot(self.bins_collection.getMidValuesArray(), self.ls_bounded, c='r', linestyle='--', label='Least Squares Bounded')

        # ax.plot(self.bins, self.log_mle_fit, c='g', label='Maximum Likelihood')
        # magnitudes, ls_bounded = self.getBoundedArray(solution=self.calculateMaximumLikelihoodEstimatorSolution())
        # ax.plot(magnitudes, ls_bounded, c='g', linestyle='--', label='Maximum Likelihood Bounded')
        #
        # ax.plot(self.bins, self.log_fit_data, c='b', label='b = 1')

        for i, b in enumerate(self.bins[:-1]):
            mid_bin = (b + self.bins[i+1]) / 2.
            ax.plot([mid_bin, mid_bin], [0, self.freq[i]], c='gray', lw=0.75)
            ax.scatter(mid_bin, self.freq[i], marker='o', c='gray', s=2)

        mid_x = self.bins[0] + (self.max_mag + 0.5 - self.bins[0]) / 4.
        magnitudes = np.sort(self.collection.getEventsMagnitudes())
        calculated_max_magnitude = self.getLeastSquaresValueAtFrequency(solution=solution, frequency=np.log10(1))

        ax.scatter(calculated_max_magnitude, 1, marker='X', zorder=10,
                   edgecolors='blue', linewidths=0.5)

        txt = r"$M_{\!L \ \text{max0/-1/-2}} = $" + f"{self.max_mag} / {magnitudes[-2]} / {magnitudes[-3]}" + '\n'
        txt += r"$M_{\!L \ \text{max1}} = $" + f"{round(calculated_max_magnitude, 1)}" + '\n'
        txt += r"$\Delta t = $" + f"{self.collection.getTimeInterval().days} days" + '\n'

        ax.text(x=mid_x, y=5e3, s=txt, ha='left')

        ax.set_yscale('log')
        ax.legend()

        ax.set_ylim([0.1, 1e5])
        ax.set_xlim([self.bins[0], self.max_mag + 0.5])

        ax.set_ylabel('Cumulative Nr. Seismic Events')
        ax.set_xlabel('Local Magnitude')

        ax.grid(alpha=0.3)

        plt.show()
