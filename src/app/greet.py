import argparse
import logging

logger = logging.getLogger(__name__)


def greet(name: str) -> str:
    return f"Hello, {name}! Welcome to GitHub."


def main() -> None:
    logger.info("greet CLI started")
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
    logger.info("Input name: %s", args.name)
    message = greet(args.name)
    logger.info("Output message: %s", message)
    print(message)


if __name__ == "__main__":
    main()
