from EngineArguments.DefaultArguments import gg_arguments, open_arguments, ep_arguments, base_arguments
from EngineComponents.Abstract.FlowState import ManualFlowState

gg_arguments_rp1_kwak = gg_arguments | {
    'gg_base_flow_state': ManualFlowState(propellant_name='ExhaustGas',
                                          temperature=open_arguments['turbine_maximum_temperature'],
                                          pressure=None,
                                          mass_flow=None,
                                          type='combusted',
                                          _molar_mass=0.03033368339292229,
                                          _specific_heat_capacity=2024.7,
                                          _heat_capacity_ratio=1.16,
                                          _density=None),

    'gg_mass_mixture_ratio': 0.320,
}
ep_arguments_rp1_kwak = ep_arguments | {'battery_coolant_specific_heat_capacity': 2009, }
common_arguments_kwak = base_arguments | {
    '_ignore_cooling': True,
    'fuel_initial_temperature': 263.6,
    'specific_impulse_quality_factor': 1.0,
    'shaft_mechanical_efficiency': 1.0,
    'exit_pressure_forced': 0.002E6,
    # To get the as close as possible to density given by Kwak with his initial pressure of 2.5 bar
    'oxidizer_initial_temperature': 93.340,  # To get the same density as Kwak with his initial pressure of 4 bar
    '_fuel_pump_pressure_factor_first_guess': 1.55,
    '_oxidizer_pump_pressure_factor_first_guess': 1.15,
    'is_frozen': False,

}
kwak_specific_arguments = {
    'pressurant_heat_capacity_ratio': 1.667,
    'pressurant_molar_mass': 0.00399733779,
    'manual_oxidizer_density': 1126.1,
    'manual_fuel_density': 804.2,
}
