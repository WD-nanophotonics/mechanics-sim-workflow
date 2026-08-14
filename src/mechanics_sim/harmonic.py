"""One-dimensional harmonic oscillator helpers."""


def harmonic_acceleration(position: float, stiffness: float, mass: float) -> float:
    """Return the acceleration for a Hooke-law oscillator at ``position``."""
    if mass <= 0:
        raise ValueError("mass must be positive")
    return -(stiffness / mass) * position


def harmonic_energy(
    position: float, velocity: float, stiffness: float, mass: float
) -> float:
    """Return the total mechanical energy of the oscillator."""
    if mass <= 0:
        raise ValueError("mass must be positive")
    return 0.5 * mass * velocity**2 + 0.5 * stiffness * position**2
