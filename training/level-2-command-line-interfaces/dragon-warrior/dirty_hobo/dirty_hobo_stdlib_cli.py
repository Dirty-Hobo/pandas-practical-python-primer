"""
This module provides a CLI that...
"""

import argparse

import file_ops


def _extract_arguments():
    parser = argparse.ArgumentParser(
        prog='My Cool Program',
        description="My cool program does a lot of cool things.",
        epilog="Thanks for using my cool program")

    parser.add_argument("-f", "--filenames", nargs="+", metavar="FILENAME",
                        required=True, help="Names of files to copy.")

    parser.add_argument("-d", '--destination', required=True,
                        help='Location to copy files to.')

    return parser.parse_args()

if __name__ == '__main__':

    program_arguments = _extract_arguments()
    file_ops.copy_files(
        program_arguments.filenames,
        program_arguments.destination)

# print(program_arguments)
