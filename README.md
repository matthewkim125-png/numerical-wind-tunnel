# Numerical Wind Tunnel

A beginner-built, explainable two-dimensional flow solver. This repository
starts with the numerical foundations and will grow through small, tested
milestones so that every result can be traced to code its author understands.

## Stage 0: the D2Q9 lattice

The project currently defines the D2Q9 lattice used by the lattice-Boltzmann
method. At each grid cell, D2Q9 stores nine population values: one stationary
population, four moving along the grid axes, and four moving diagonally.

```text
6 northwest    2 north    5 northeast
          \       |       /
3 west ----    0 rest    ---- 1 east
          /       |       \
7 southwest    4 south    8 southeast
```

Each direction has a velocity vector and a weight. The nine weights sum to one.
The example program prints these constants so their ordering and meaning are
visible before any fluid dynamics is added.

## Run it

The project uses Python 3.12 and
[`uv`](https://docs.astral.sh/uv/) for its isolated environment and dependency
lockfile.

```bash
uv sync --extra dev
uv run python examples/show_lattice.py
uv run pytest
```

The example should print nine directions followed by:

```text
total weight: 1.000000
```

## Planned progression

1. Convert density and velocity into equilibrium populations and recover them.
2. Add BGK collision and connect relaxation time to viscosity.
3. Stream populations across a periodic grid.
4. Add solid masks and stationary bounce-back walls.
5. Produce and validate force-driven channel flow.
6. Study grid refinement and analytical error.
7. Add a cylinder, Reynolds-number control, wake diagnostics, drag, and lift.
8. Add continuous integration and package reproducible benchmark results.

## Current limitations

This stage does not simulate fluid flow. It only defines and checks the D2Q9
lattice on which later simulation steps will operate. The eventual solver is a
learning and portfolio project, not engineering-grade CFD software, and its
results must not be used for design or safety decisions.

## License

No license has been selected yet. All rights are reserved unless a license is
added in a later milestone.
