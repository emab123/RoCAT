from dataclasses import dataclass
from EngineComponents.Abstract.FlowState import FlowState


@dataclass
class Propellant:
    main_flow_state: FlowState
    burn_time: float  # [s]
    margin_factor: float  # [-]

    @property
    def name(self):
        return self.main_flow_state.propellant_name

    @property
    def mass_flow(self):
        return self.main_flow_state.mass_flow

    @property
    def density(self):
        return self.main_flow_state.density

    @property
    def mass(self):
        if self.mass_flow is None or self.burn_time is None or self.margin_factor is None:
            return 0  # or raise ValueError("One or more required values are None")
        return self.mass_flow * self.burn_time * self.margin_factor

    @property
    def volume(self):
        return self.mass / self.density

    @property
    def volumetric_flow(self):
        return self.mass_flow / self.density
