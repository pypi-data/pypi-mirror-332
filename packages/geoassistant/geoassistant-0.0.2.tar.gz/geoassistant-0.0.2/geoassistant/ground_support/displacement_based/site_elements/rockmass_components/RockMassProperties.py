from typing import Optional, Literal, Dict


class RockMassProperties(object):

    def __init__(self):

        self.density: Optional[float] = None  # [kg/m3]
        self.UCS: Optional[float] = None  # [MPa]
        self.n: Optional[Literal[2, 3, 6]] = None  # 2 blocky, 3 moderately jointed, 6 massive competent

        self.shear_wave_velocity: Optional[float] = None  # known as "cs" or "vs" [km/s]

        self.perras_diederichs_model: Dict[str, float] = {'a': 0.58, 'b': 0.65, 'Ci': 0.43}  # Used in delta_df

    def setDensity(self, density: float) -> None:
        self.density = density

    def setUCS(self, UCS: float) -> None:
        self.UCS = UCS

    def setN(self, n: Literal[2, 3, 6]) -> None:
        self.n = n

    def setShearWaveVelocity(self, shear_wave_velocity: float) -> None:
        self.shear_wave_velocity = shear_wave_velocity

    def getDensity(self) -> Optional[float]:
        return self.density

    def getUCS(self) -> Optional[float]:
        return self.UCS

    def getN(self) -> Optional[Literal[2, 3, 6]]:
        return self.n

    def getShearWaveVelocity(self) -> Optional[float]:
        return self.shear_wave_velocity

    def getPerrasDiederichsModel(self) -> Dict[str, float]:
        return self.perras_diederichs_model
