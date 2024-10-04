"""
Main module
"""
from argparse import ArgumentParser


def main() -> None:
    """Main method"""
    parser = ArgumentParser()
    parser.add_argument("--filepath", required=True, type=str)
    args = parser.parse_args()

    filepath: str = args.filepath

    if filepath != "":
        print(filepath)
        # do something with the filepath


if __name__ == "__main__":
    main()
