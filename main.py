from pyexiv2 import Image
import sys


def add_metadata(path):
    pass


if __name__ == "__main__":
    if sys.argv[1] == "add":
        add_metadata(sys.argv[2])
