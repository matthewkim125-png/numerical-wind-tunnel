import numpy as np
import pytest

from windtunnel import WEIGHTS, equilibrium, macroscopic


def test_stationary_equilibrium_is_density_times_lattice_weights():
    density = np.full((3, 5), 2.0)
    velocity = np.zeros((2, 3, 5))

    populations = equilibrium(density, velocity)

    assert populations.shape == (9, 3, 5)
    expected = WEIGHTS[:, None, None] * density[None, :, :]
    np.testing.assert_allclose(populations, expected)


def test_equilibrium_round_trip_recovers_density_and_velocity():
    density = np.full((4, 7), 1.2)
    velocity = np.zeros((2, 4, 7))
    velocity[0] = 0.04
    velocity[1] = -0.01

    populations = equilibrium(density, velocity)
    recovered_density, recovered_velocity = macroscopic(populations)

    np.testing.assert_allclose(recovered_density, density, atol=1e-14)
    np.testing.assert_allclose(recovered_velocity, velocity, atol=1e-14)


def test_eastward_velocity_produces_more_east_than_west_population():
    density = np.ones((2, 3))
    velocity = np.zeros((2, 2, 3))
    velocity[0] = 0.04

    populations = equilibrium(density, velocity)

    assert np.all(populations[1] > populations[3])


def test_state_conversions_reject_incompatible_shapes():
    with pytest.raises(ValueError, match="density must have shape"):
        equilibrium(np.ones(5), np.zeros((2, 5)))

    with pytest.raises(ValueError, match="velocity must have shape"):
        equilibrium(np.ones((3, 5)), np.zeros((3, 5)))

    with pytest.raises(ValueError, match="populations must have shape"):
        macroscopic(np.ones((8, 3, 5)))


def test_state_conversions_reject_non_positive_density():
    with pytest.raises(ValueError, match="density must be positive"):
        equilibrium(np.zeros((3, 5)), np.zeros((2, 3, 5)))

    with pytest.raises(ValueError, match="population density must be positive"):
        macroscopic(np.zeros((9, 3, 5)))
