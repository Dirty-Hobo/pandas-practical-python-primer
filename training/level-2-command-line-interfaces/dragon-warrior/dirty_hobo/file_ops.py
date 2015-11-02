"""This module provides various functions for operating on files"""

import subprocess


def copy_files(files: list, destination: str):
    """
    Copy files to a given destination.

    Args:
        files: A list of files to copy.
        destination: A str specifying the destination for copied files.        
    """
    for file in files:
        result = subprocess.check_output(
            args=['cp', '-vp', file, destination],
            stderr=subprocess.STDOUT)
        print(
            result.decode(
                'utf-8').rstrip())
