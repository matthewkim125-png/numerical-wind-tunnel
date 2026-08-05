import numpy as np

from windtunnel import DIRECTION_NAMES, VELOCITIES, WEIGHTS


def test_d2q9_has_nine_unique_two_dimensional_directions():
    assert VELOCITIES.shape == (9, 2)
    assert len(np.unique(VELOCITIES, axis=0)) == 9
    np.testing.assert_array_equal(VELOCITIES[0], [0, 0])


def test_direction_names_match_the_velocity_vectors():
    assert len(DIRECTION_NAMES) == len(VELOCITIES)
    assert len(set(DIRECTION_NAMES)) == len(DIRECTION_NAMES)
    assert DIRECTION_NAMES[0] == "rest"


def test_d2q9_weights_are_positive_and_normalized():
    assert WEIGHTS.shape == (9,)
    assert np.all(WEIGHTS > 0)
    np.testing.assert_allclose(WEIGHTS.sum(), 1.0, atol=1e-15)


def test_d2q9_weights_match_the_standard_groups():
    np.testing.assert_allclose(WEIGHTS[0], 4 / 9)
    np.testing.assert_allclose(WEIGHTS[1:5], np.full(4, 1 / 9))
    np.testing.assert_allclose(WEIGHTS[5:9], np.full(4, 1 / 36))
