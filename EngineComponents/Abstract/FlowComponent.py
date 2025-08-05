from dataclasses import dataclass, replace
from EngineComponents.Abstract.FlowState import FlowState


@dataclass
class FlowComponent:
    # These parameters are back-ups in case child class does not define them
    #  ,so FlowComponents can always change the pressure, temperature or mass flow
    inlet_flow_state: FlowState
    _temperature_change: float = 0
    _pressure_change: float = 0
    _mass_flow_change: float = 0

    @property
    def inlet_pressure(self):
        return self.inlet_flow_state.pressure

    @property
    def inlet_temperature(self):
        return self.inlet_flow_state.temperature

    @property
    def inlet_mass_flow(self):
        return self.inlet_flow_state.mass_flow

    @property
    def temperature_change(self):
        return self._temperature_change

    @property
    def pressure_change(self):
        return self._pressure_change

    @property
    def mass_flow_change(self):
        return self._mass_flow_change

    @property
    def outlet_pressure(self):
        return self.inlet_pressure + self.pressure_change

    @property
    def outlet_temperature(self):
        return self.inlet_temperature + self.temperature_change

    @property
    def outlet_mass_flow(self):
        if self.inlet_mass_flow is None or self.mass_flow_change is None:
            return None
        return self.inlet_mass_flow + self.mass_flow_change

    @property
    def outlet_flow_state(self):
        return replace(self.inlet_flow_state,
                       pressure=self.outlet_pressure,
                       temperature=self.outlet_temperature,
                       mass_flow=self.outlet_mass_flow,
                       )

    @property
    def mass_flow(self):
        if self.inlet_mass_flow == self.outlet_mass_flow:
            return self.inlet_mass_flow
        else:
            raise ValueError('This FlowComponent has different inlet and outlet mass flows, so using mass_flow is '
                             'ambiguous, please use inlet_mass_flow or outlet_mass_flow instead')


