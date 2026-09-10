"""Conversions between D2Q9 populations and familiar fluid variables."""

from __future__ import annotations

import numpy as np

from .lattice import VELOCITIES, WEIGHTS


def equilibrium(density: np.ndarray, velocity: np.ndarray) -> np.ndarray:
    """Return equilibrium D2Q9 populations for a density and velocity field.

    ``density`` has shape ``(rows, columns)`` and ``velocity`` has shape
    ``(2, rows, columns)``. The returned array has one layer for each of the
    nine lattice directions, so its shape is ``(9, rows, columns)``.
    """
    density = np.asarray(density, dtype=float)
    velocity = np.asarray(velocity, dtype=float)

    if density.ndim != 2:
        raise ValueError("density must have shape (rows, columns)")
    if velocity.shape != (2, *density.shape):
        raise ValueError("velocity must have shape (2, rows, columns)")
    if np.any(density <= 0):
        raise ValueError("density must be positive")

    populations = np.empty((9, *density.shape), dtype=float)
    speed_squared = velocity[0] ** 2 + velocity[1] ** 2

    for direction, (cx, cy) in enumerate(VELOCITIES):
        directional_velocity = cx * velocity[0] + cy * velocity[1]
        populations[direction] = WEIGHTS[direction] * density * (
            1.0
            + 3.0 * directional_velocity
            + 4.5 * directional_velocity**2
            - 1.5 * speed_squared
        )

    return populations


def macroscopic(populations: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Recover density and velocity fields from D2Q9 populations."""
    populations = np.asarray(populations, dtype=float)

    if populations.ndim != 3 or populations.shape[0] != 9:
        raise ValueError("populations must have shape (9, rows, columns)")

    density = populations.sum(axis=0)
    if np.any(density <= 0):
        raise ValueError("population density must be positive")

    momentum = np.zeros((2, *density.shape), dtype=float)
    for direction, (cx, cy) in enumerate(VELOCITIES):
        momentum[0] += populations[direction] * cx
        momentum[1] += populations[direction] * cy

    velocity = momentum / density[None, :, :]
    return density, velocity
