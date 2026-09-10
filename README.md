# Numerical Wind Tunnel

A two-dimensional lattice-Boltzmann solver implemented in Python and NumPy.
The current implementation defines the D2Q9 lattice and converts between
equilibrium populations and macroscopic density and velocity fields.

## Current capabilities

The project defines the D2Q9 lattice used by the lattice-Boltzmann method. At
each grid cell, D2Q9 stores nine population values: one stationary population,
four moving along the grid axes, and four moving diagonally.

```text
6 northwest    2 north    5 northeast
          \       |       /
3 west ----    0 rest    ---- 1 east
          /       |       \
7 southwest    4 south    8 southeast
```

Each direction has a velocity vector and a weight. The nine weights sum to one.
The project can now convert density and velocity fields into equilibrium D2Q9
populations and recover the original macroscopic fields from those populations.

## Installation and usage

The project uses Python 3.12 and
[`uv`](https://docs.astral.sh/uv/) for its isolated environment and dependency
lockfile.

```bash
uv sync --extra dev
uv run python examples/show_lattice.py
uv run python examples/equilibrium_round_trip.py
uv run pytest
```

The lattice example prints nine directions followed by:

```text
total weight: 1.000000
```

The round-trip example prints the array shapes and numerical recovery error for
a small uniform flow field.

## Technical roadmap

1. Define and verify the D2Q9 lattice. **Complete**
2. Convert density and velocity into equilibrium populations and recover them. **Complete**
3. Add BGK collision and connect relaxation time to viscosity.
4. Stream populations across a periodic grid.
5. Add solid masks and stationary bounce-back walls.
6. Produce and validate force-driven channel flow.
7. Study grid refinement and analytical error.
8. Add a cylinder, Reynolds-number control, wake diagnostics, drag, and lift.
9. Add continuous integration and package reproducible benchmark results.

## Limitations

The implementation does not yet include collision, streaming, boundary
conditions, forcing, or time integration. It can represent an equilibrium fluid
state but does not yet perform a CFD simulation. Results are not suitable for
engineering design or safety decisions.

## License

No license has been selected. All rights are reserved.
