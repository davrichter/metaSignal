import datetime

from pyexiv2 import Image
import sys
import os


def add_metadata(path):
    for file in os.listdir(path):
        filename = os.fsdecode(file)
        if filename.endswith(".jpg"):
            with Image(str(path + filename)) as img:
                date = datetime.datetime.strptime((filename[7:23]), "%Y-%m-%d-%H-%M")

                exif = img.read_exif()
                exif['Exif.Photo.DateTimeOriginal'] = date.strftime('%Y:%m:%d %H:%M:%S')
                img.modify_exif(exif)
            continue
        else:
            continue


if __name__ == "__main__":
    if sys.argv[1] == "add":
        add_metadata(sys.argv[2])
