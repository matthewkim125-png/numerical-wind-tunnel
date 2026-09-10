"""Create equilibrium populations and recover their fluid variables."""

import numpy as np

from windtunnel import equilibrium, macroscopic


def main() -> None:
    density = np.ones((4, 7))
    velocity = np.zeros((2, 4, 7))
    velocity[0] = 0.04

    populations = equilibrium(density, velocity)
    recovered_density, recovered_velocity = macroscopic(populations)

    print(f"density shape: {density.shape}")
    print(f"velocity shape: {velocity.shape}")
    print(f"populations shape: {populations.shape}")
    print(f"maximum density error: {np.max(np.abs(recovered_density - density)):.3e}")
    print(f"maximum velocity error: {np.max(np.abs(recovered_velocity - velocity)):.3e}")


if __name__ == "__main__":
    main()
