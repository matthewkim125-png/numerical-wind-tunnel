"""Constants that define the two-dimensional, nine-direction D2Q9 lattice."""

from __future__ import annotations

import numpy as np

# Every row is a lattice direction written as (x movement, y movement).
# The order is rest, four axial directions, then four diagonal directions.
VELOCITIES = np.array(
    [
        [0, 0],
        [1, 0],
        [0, 1],
        [-1, 0],
        [0, -1],
        [1, 1],
        [-1, 1],
        [-1, -1],
        [1, -1],
    ],
    dtype=int,
)

DIRECTION_NAMES = (
    "rest",
    "east",
    "north",
    "west",
    "south",
    "northeast",
    "northwest",
    "southwest",
    "southeast",
)

# D2Q9 quadrature weights: 4/9 at rest, 1/9 on each axis, and 1/36
# on each diagonal. Together they sum to one.
WEIGHTS = np.array(
    [4 / 9, 1 / 9, 1 / 9, 1 / 9, 1 / 9, 1 / 36, 1 / 36, 1 / 36, 1 / 36],
    dtype=float,
)
