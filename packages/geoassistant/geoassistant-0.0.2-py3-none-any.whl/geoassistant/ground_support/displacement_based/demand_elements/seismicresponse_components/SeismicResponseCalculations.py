from typing import Optional, TYPE_CHECKING

import numpy as np

if TYPE_CHECKING:
    from geoassistant.ground_support.displacement_based.demand_elements.SeismicResponse import SeismicResponse


class SeismicResponseCalculations(object):

    def __init__(self, seismic_response: 'SeismicResponse'):
        self.seismic_response: 'SeismicResponse' = seismic_response

        self.peak_ground_acceleration: Optional[float] = None  # PGA [m/s2]

        self.DTSI: Optional[float] = None  # Dynamic Tangential Stress Increment
        self.stress_level_change: Optional[float] = None  # delta_SL (no units)

    def getPeakGroundAcceleration(self) -> Optional[float]:
        return self.peak_ground_acceleration

    def getDTSI(self) -> Optional[float]:
        return self.DTSI

    def getStressLevelChange(self) -> Optional[float]:
        return self.stress_level_change

    def calculatePeakGroundAcceleration(self) -> None:
        se = self.seismic_response.getSeismicEvent()

        f_units = se.getFrequency().getUnits()
        if f_units != 'Hz':
            raise ValueError("TO IMPLEMENT")

        f = se.getFrequency().getValue()

        self.peak_ground_acceleration = 2 * np.pi * f * self.seismic_response.getPeakGroundVelocity()

    def calculateDTSI(self) -> None:
        rm = self.seismic_response.getSite().getRockMass()

        cs = rm.getShearWaveVelocity()
        density = rm.getDensity()

        self.DTSI = 4 * cs * density * self.seismic_response.getPeakGroundVelocity() / 1000

    def calculateStressLevelChange(self) -> None:
        rm = self.seismic_response.getSite().getRockMass()

        self.stress_level_change = self.DTSI / rm.getUCS()

    def checkParametersCalculation(self) -> None:
        fields = [
            self.seismic_response.getSite(),
            self.seismic_response.getSeismicEvent(),
            self.seismic_response.getPeakGroundVelocity(),
        ]

        if None in fields:
            return

        self.calculatePeakGroundAcceleration()
        self.calculateDTSI()
        self.calculateStressLevelChange()