import sys

from research_navigator.ingest.cli import (
    ingest,
    reindex,
    stats,
    validate,
)


def main():
    if len(sys.argv) < 2:
        print(
            "Usage:\n"
            "python -m research_navigator.ingest "
            "[ingest|validate|stats|reindex]"
        )

        return

    command = sys.argv[1]

    if command == "ingest":
        ingest()

    elif command == "validate":
        validate()

    elif command == "stats":
        stats()

    elif command == "reindex":
        reindex()

    else:
        print(f"Unknown command: {command}")


if __name__ == "__main__":
    main()
