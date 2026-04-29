import argparse


def greet(name: str) -> str:
    return f"Hello, {name}! Welcome to GitHub."


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Print a GitHub learning greeting."
    )
    parser.add_argument(
        "name",
        nargs="?",
        default="Omprakash",
        help="Name to include in the greeting",
    )

    args = parser.parse_args()
    print(greet(args.name))


if __name__ == "__main__":
    main()
