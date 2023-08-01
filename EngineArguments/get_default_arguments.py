import EngineArguments.Kwak
import EngineArguments.DefaultArguments as args
from EngineCycles.Abstract.EngineCycle import EngineCycle
from EngineCycles.ElectricPumpCycle import ElectricPumpCycle
from EngineCycles.GasGeneratorCycle import GasGeneratorCycle_Mixin, GasGeneratorCycle_DoubleTurbineSeries
from EngineCycles.OpenExpanderCycle import OpenExpanderCycle_DoublePump_Mixin, OpenExpanderCycle_Mixin, \
    OpenExpanderCycle_DoubleTurbineSeries
from EngineCycles.Abstract.OpenCycle import OpenEngineCycle_DoubleTurbine
from KwakFix.KwakFixCycles import KwakEngineCycle


def get_default_kwargs(EngineClass: EngineCycle, mass_mixture_ratio: bool = True):
    if issubclass(EngineClass, KwakEngineCycle):
        default_args = EngineArguments.Kwak.common_arguments_kwak | EngineArguments.Kwak.kwak_specific_arguments
        if issubclass(EngineClass, ElectricPumpCycle):
            kwargs = default_args | EngineArguments.Kwak.ep_arguments_rp1_kwak
        else:
            kwargs = default_args | EngineArguments.Kwak.gg_arguments_rp1_kwak
    else:
        default_args = args.base_arguments if mass_mixture_ratio else args.base_arguments_o
        if issubclass(EngineClass, ElectricPumpCycle):
            kwargs = default_args | args.ep_arguments
        elif issubclass(EngineClass, GasGeneratorCycle_Mixin):
            kwargs = default_args | args.gg_arguments
        elif issubclass(EngineClass, OpenExpanderCycle_Mixin):
            kwargs = default_args | args.oe_arguments
        else:
            raise ValueError('No default arguments are known for this cycle')

        if issubclass(EngineClass, OpenEngineCycle_DoubleTurbine):
            pressure_ratio = kwargs.pop('turbine_pressure_ratio')
            efficiency = kwargs.pop('turbine_efficiency')
            expansion_ratio = kwargs.pop('exhaust_expansion_ratio')
            kwargs = kwargs | {
                'fuel_turbine_pressure_ratio': pressure_ratio,
                'oxidizer_turbine_pressure_ratio': pressure_ratio,
                'fuel_turbine_efficiency': efficiency,
                'oxidizer_turbine_efficiency': efficiency,
                'fuel_exhaust_expansion_ratio': expansion_ratio,
                'oxidizer_exhaust_expansion_ratio': expansion_ratio,
            }
            if issubclass(EngineClass, GasGeneratorCycle_DoubleTurbineSeries
                          ) or issubclass(
                EngineClass, OpenExpanderCycle_DoubleTurbineSeries
            ):
                kwargs.pop('fuel_exhaust_expansion_ratio')
        if issubclass(EngineClass, OpenExpanderCycle_DoublePump_Mixin):
            kwargs = kwargs | args.oe_double_pump_arguments
    return kwargs
