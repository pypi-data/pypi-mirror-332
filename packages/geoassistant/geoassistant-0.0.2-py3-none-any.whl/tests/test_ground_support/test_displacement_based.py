import os
import unittest

from geoassistant import Bolt, BoltSet, BoltSystem, SurfaceSupport, SupportSystem, SeismicEvent, SeismicResponse, Site, \
    Excavation, RockMass, StressState, DemandSystem, Strainburst, PreviousDisplacement, CapacityPlot, BulkingFactors, \
    SafetyFactors, MontecarloSimulation


class TestDisplacementBasedGroundSupport(unittest.TestCase):

    def setUp(self):
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.resources_dir = os.path.join(self.base_dir, 'resources')

    def test_01(self):

        b = Bolt.loadFromBaseCatalog(bolt_id="Debonded Posimix")
        b.setDisplacementSplitFactor(displacement_split_factor=0.5)

        b2 = Bolt.loadFromBaseCatalog(bolt_id="Secura R27")
        b2.setDisplacementSplitFactor(displacement_split_factor=0.5)

        bs = BoltSet(name=b.getName())
        bs.setBolt(bolt=b)
        bs.setBoltSpacing(bolt_spacing=1.5)
        bs.setRingSpacing(ring_spacing=1.5)

        bs2 = BoltSet(name=b2.getName())
        bs2.setBolt(bolt=b2)
        bs2.setBoltSpacing(bolt_spacing=1.3)
        bs2.setRingSpacing(ring_spacing=1.3)

        bsys = BoltSystem(name="Bolt System")
        bsys.addBoltSet(bs)
        bsys.addBoltSet(bs2)

        sfc = SurfaceSupport.loadFromBaseCatalog(surface_support_id="Minax Mesh")

        ssys = SupportSystem(name="DBS-10")
        ssys.setBoltSystem(bolt_system=bsys)
        ssys.setSurfaceSupport(surface_support=sfc)

        ex = Excavation()
        ex.setWidth(width=6.8)
        ex.setHeight(height=9.2)
        ex.setWidestIntersectionSpan(widest_intersection_span=18.2)
        # ex.setWidth(width=5.0)
        # ex.setHeight(height=5.5)
        # ex.setWidestIntersectionSpan(widest_intersection_span=10.)
        ex.setInitialDamageDepth(initial_damage_depth=0.)

        rm = RockMass()
        rm.setN(n=3)
        rm.setUCS(UCS=156)
        rm.setDensity(density=2750)
        rm.setShearWaveVelocity(shear_wave_velocity=2.8)

        ss = StressState()
        ss.setStressLevel(stress_level=0.623)

        site = Site()
        site.setExcavation(excavation=ex)
        site.setRockMass(rock_mass=rm)
        site.setStressState(stress_state=ss)

        # se = SeismicEvent()
        # se.setFrequency(value=7, units="Hz")
        #
        # sr = SeismicResponse()
        # sr.setSite(site)
        # sr.setSeismicEvent(seismic_event=se)
        # sr.setPeakGroundVelocity(peak_ground_velocity=1.2)
        #
        # sb = Strainburst()
        # sb.setStrainburstDepth(strainburst_depth=0.662)
        # sb.setRuptureTime(rupture_time=25.08)
        #
        # pd = PreviousDisplacement()
        # pd.setD0(d0=36.19)
        #
        # bf = BulkingFactors()
        # bf.setStaticBulkingFactor(static_bulking_factor=0.02)
        # bf.setDynamicBulkingFactor(dynamic_bulking_factor=0.059)
        #
        # ds = DemandSystem()
        # ds.setSite(site=site)
        # ds.setSeismicResponse(seismic_response=sr)
        # ds.setStrainburst(strainburst=sb)
        # ds.setPreviousDisplacement(previous_displacement=pd)
        # ds.setBulkingFactors(bulking_factors=bf)
        #
        # ds.calculations.calculateEnergyDemandCurve()

        # cap_plot = CapacityPlot()
        # cap_plot.addSupportSystem(ssys)
        # cap_plot.addDemandSystem(demand_system=ds)
        # cap_plot.plot(capacity_type='remnant')

        # bsys.plotCapacityCurve()

        # sfs = SafetyFactors(support_system=ssys, demand_system=ds)

        ms = MontecarloSimulation(support_system=ssys, site=site)
        ms.calculateMontecarloResults()

        # print(f"Static elongated FS: {sfs.getElongatedStaticSafetyFactor()}")
        # print(f"Static intersection FS: {sfs.getIntersectionStaticSafetyFactor()}")
        # print(f"Static central FS: {sfs.getCentralStaticSafetyFactor()}")
        # print(f"Static central intersection FS: {sfs.getCentralIntersectionStaticSafetyFactor()}\n")
        #
        # print(f"PGA: {sr.getPeakGroundAcceleration()} [m/s2]\n")
        #
        print(f"ShakedownInitiation elongated FS: {ms.getElongatedShakedownInitiationSafetyFactor()}")
        print(f"ShakedownInitiation intersection FS: {ms.getIntersectionShakedownInitiationSafetyFactor()}")
        print(f"ShakedownInitiation central FS: {ms.getCentralShakedownInitiationSafetyFactor()}")
        print(f"ShakedownInitiation central intersection FS: {ms.getCentralIntersectionShakedownInitiationSafetyFactor()}\n")

        print(f"ShakedownSurvival elongated FS: {ms.getElongatedShakedownSurvivalSafetyFactor()}")
        print(f"ShakedownSurvival intersection FS: {ms.getIntersectionShakedownSurvivalSafetyFactor()}")
        print(f"ShakedownSurvival central FS: {ms.getCentralShakedownSurvivalSafetyFactor()}")
        print(f"ShakedownSurvival central intersection FS: {ms.getCentralIntersectionShakedownSurvivalSafetyFactor()}\n")

        print(f"Self-Initiated Strainburst displacement FS: {ms.getSelfInitiatedStrainburstDisplacementSafetyFactor()}")
        print(f"Self-Initiated Strainburst energy FS: {ms.getSelfInitiatedStrainburstEnergySafetyFactor()}")
        print(f"Dynamically-Loaded Strainburst displacement FS: {ms.getDynamicallyLoadedStrainburstDisplacementSafetyFactor()}")
        print(f"Dynamically-Loaded Strainburst energy FS: {ms.getDynamicallyLoadedStrainburstEnergySafetyFactor()}\n")

        print(f"Self-Initiated Strainburst displacement PoF: {ms.getSelfInitiatedStrainburstDisplacementProbabilityOfFailure()}")
        print(f"Self-Initiated Strainburst energy PoF: {ms.getSelfInitiatedStrainburstEnergyProbabilityOfFailure()}")
        print(f"Dynamically-Loaded Strainburst displacement PoF: {ms.getDynamicallyLoadedStrainburstDisplacementProbabilityOfFailure()}")
        print(f"Dynamically-Loaded Strainburst energy PoF: {ms.getDynamicallyLoadedStrainburstEnergyProbabilityOfFailure()}")


if __name__ == "__main__":
    unittest.main()