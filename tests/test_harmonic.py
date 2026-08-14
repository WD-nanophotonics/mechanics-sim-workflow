import pytest

from mechanics_sim import harmonic_acceleration


def test_harmonic_acceleration_restoring_force() -> None:
    assert harmonic_acceleration(position=2.0, stiffness=4.0, mass=2.0) == -4.0


def test_harmonic_acceleration_requires_positive_mass() -> None:
    with pytest.raises(ValueError, match="mass must be positive"):
        harmonic_acceleration(position=1.0, stiffness=1.0, mass=0.0)
