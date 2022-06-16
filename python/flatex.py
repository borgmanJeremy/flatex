from pathlib import Path
import sys
import argparse


def parse_args(args):
    parser = argparse.ArgumentParser(
        description="create a single latex file with no include/inputs"
    )

    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Display file structure"
    )
    parser.add_argument(
        "-q", "--quiet", action="store_true", help="Quiet mode with cleaner output"
    )
    parser.add_argument(
        "-b", action="store_true", help="Do not insert bibliography file(.bbl)"
    )
    parser.add_argument("filename")
    return parser.parse_args(args)


def flat_it(input_file):
    for input_line in input_file:
        print(input_line)


def flat_file(args):
    input_file_name = args.filename
    with open(input_file_name, encoding="utf-8") as input_file:
        print(f"input file: {input_file_name}")

        output_file_name = Path(input_file_name).with_suffix(".flt")

        with open(output_file_name, "w", encoding="utf-8") as output_file:
            flat_it(input_file)
    print(f"\tFile: {output_file_name} generated")


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    flat_file(args)
