from dataclasses import dataclass
from typing import Optional


@dataclass
class Material:
    yield_strength: float  # [Pa]
    density: float  # [kg/m3]
    poisson_ratio: Optional[float] = None  # [-]
    thermal_conductivity: Optional[float] = None  # [W/(K m)]
    minimal_thickness: Optional[float] = None  # [m]


Inconel718 = Material(yield_strength=1200e6, density=8190, poisson_ratio=.29, thermal_conductivity=11.4, minimal_thickness=0.5e-3)
Inconel600 = Material(yield_strength=1035e6, density=8470, poisson_ratio=.31, thermal_conductivity=14.9, minimal_thickness=0.5e-3)
Ti6Al4V = Material(yield_strength=1170e6, density=4330, poisson_ratio=.31, thermal_conductivity=6.7, minimal_thickness=0.5e-3)
Al2219 = Material(yield_strength=414e6, density=2840, poisson_ratio=.33, thermal_conductivity=120, minimal_thickness=0.5e-3)
NarloyZ = Material(yield_strength=315e6, density=9130, poisson_ratio=.34, thermal_conductivity=350, minimal_thickness=0.5e-3)
Al7075T6 = Material(yield_strength=570e6, density=2810, poisson_ratio=.33, thermal_conductivity=130, minimal_thickness=0.5e-3)
StainlessSteel301_Annealed = Material(yield_strength=275e6, density=7830, poisson_ratio=.27, thermal_conductivity=16.3, minimal_thickness=0.5e-3)
StainlessSteel301_FullHard = Material(yield_strength=965e6, density=7830, poisson_ratio=.27, thermal_conductivity=16.3, minimal_thickness=0.5e-3)
Al6061T6 = Material(yield_strength=276e6, density=2700, poisson_ratio=.33, thermal_conductivity=167, minimal_thickness=0.5e-3)
KwakPropellantTankMaterial = Material(yield_strength=250e6, density=2850, minimal_thickness=0)
KwakPressurantTankMaterial = Material(yield_strength=1100e6, density=4430, minimal_thickness=0)
KwakGasGeneratorMaterial = Material(yield_strength=550e6, density=8220, minimal_thickness=0)