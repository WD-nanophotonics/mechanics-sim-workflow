"""One-dimensional harmonic oscillator helpers."""


def harmonic_acceleration(position: float, stiffness: float, mass: float) -> float:
    """Return the acceleration for a Hooke-law oscillator at ``position``."""
    if mass <= 0:
        raise ValueError("mass must be positive")
    return -(stiffness / mass) * position
