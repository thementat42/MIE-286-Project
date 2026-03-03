import argparse
import os
import uuid

import interface

TESTING = True

def get_mode_from_argv() -> interface.Mode:
    arg_parser = argparse.ArgumentParser()

    arg_parser.add_argument(
        "-m", "--mode",
        type = str,
        choices=["baseline", "loss", "gain"],
        default = "baseline",
        help = "Set the mode for the test"
    )

    arg_parser.add_argument(
        "-b", "--baseline",
        action = "store_true",
        help = "Run the test in baseline mode"
    )

    arg_parser.add_argument(
        "-l", "--loss",
        action = "store_true",
        help = "Run the test in loss-based mode"
    )

    arg_parser.add_argument(
        "-g", "--gain",
        action = "store_true",
        help = "Run the test in gain-based mode"
    )

    args = arg_parser.parse_args()

    mode: interface.Mode|None = None

    if args.mode:
        match args.mode:
            case "baseline": mode = interface.Mode.BASELINE
            case "loss": interface.Mode.LOSS_BASED
            case "gain": interface.Mode.GAIN_BASED
            case _: raise Exception("Invalid mode")

    if args.baseline:
        if mode is not None:
            raise Exception("Baseline flag passed but mode was already set using the mode argument")
        mode = interface.Mode.BASELINE
    if args.loss:
        if mode is not None:
            raise Exception("Loss-based flag passed but mode was already set using the mode argument")
        mode = interface.Mode.LOSS_BASED
    if args.gain:
        if mode is not None:
            raise Exception("Gain-based flag passed but mode was already set using the mode argument")
        mode = interface.Mode.GAIN_BASED
    if mode is None:
        print("Warning: No mode set. Defaulting to baseline")
        mode = interface.Mode.BASELINE
    return mode

def get_uuid_based_filename(data_directory: str = "data") -> str:
    if TESTING:
        print("Warning: Test mode enabled. If this is an active test, set testing mode to false then re-run the script.")
        return "x.test.json"
    os.makedirs(data_directory, exist_ok=True)
    while True:
        filename = f"{uuid.uuid4()}.json"
        file_path = os.path.join(data_directory, filename)
        if not os.path.exists(file_path):
            return filename


def main():
    mode = get_mode_from_argv()
    filename = get_uuid_based_filename()
    interface.interface(filename, mode)

if __name__ == "__main__":
    main()