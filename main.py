from EngineCycles.ElectricPumpCycle import ElectricPumpCycle
from EngineCycles.GasGeneratorCycle import GasGeneratorCycle, GasGeneratorCycle_DoubleTurbine, \
    GasGeneratorCycle_DoubleTurbineSeries
from EngineCycles.OpenExpanderCycle import OpenExpanderCycle, OpenExpanderCycle_DoublePump, \
    OpenExpanderCycle_DoublePumpTurbine
from EngineArguments.get_default_arguments import get_default_kwargs
from Schematics.PerformanceSchematic import make_performance_schematic
from Schematics.MassSchematic import make_mass_schematic

# See EngineArguments.DefaultArguments for a full list of possible arguments
design_args = {
    'thrust': 100e3,
    'burn_time': 390,
    'combustion_chamber_pressure': 10e6,
    'expansion_ratio': 10,
}
# Choose from [ElectricPumpCycle, GasGeneratorCycle, OpenExpanderCycle, GasGeneratorCycle_DoubleTurbine,
# GasGeneratorCycle_DoubleTurbineSeries, OpenExpanderCycle_DoublePump, OpenExpanderCycle_DoublePumpTurbine]
Cycle = OpenExpanderCycle_DoublePumpTurbine

# Do not change
complete_args = get_default_kwargs(Cycle) | design_args
engine = Cycle(**complete_args)
make_performance_schematic(engine)
