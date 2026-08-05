"""Print the directions and weights that make up the D2Q9 lattice."""

from windtunnel import DIRECTION_NAMES, VELOCITIES, WEIGHTS


def main() -> None:
    print("D2Q9 lattice")
    print("index  direction   vector    weight")
    for index, (name, velocity, weight) in enumerate(
        zip(DIRECTION_NAMES, VELOCITIES, WEIGHTS, strict=True)
    ):
        cx, cy = velocity
        print(f"{index:>5}  {name:<10} ({cx:>2}, {cy:>2})  {weight:.6f}")

    print(f"total weight: {WEIGHTS.sum():.6f}")


if __name__ == "__main__":
    main()
