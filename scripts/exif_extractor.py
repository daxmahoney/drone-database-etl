#!/usr/bin/env python3

from PIL import Image
from PIL.ExifTags import TAGS

import json
import os
import uuid

def extract_exif_data(file_name: str) -> dict:
    image_data = { "filename": file_name}
    image = Image.open(file_name)
    exifdata = image.getexif()
    for tag_id in exifdata:
        tag = TAGS.get(tag_id, tag_id)
        data = exifdata.get(tag_id)
        if isinstance(data, bytes):
            data = data.decode()
        #cleaning step for XP exif data
        data = str(data).replace("\x00",'')
        image_data[tag] = data
    return image_data

def main():
    # Original source folder with images
    source_dir = "Part1/Images/"
    # Destination folder for converted images
    destination_dir = "/opt/icons/"
    count = 0

    all_the_data = {}
    for file_name in os.listdir(source_dir):
        exif_data = extract_exif_data(source_dir + file_name)
        all_the_data[str(uuid.uuid4())] = exif_data
        count += 1

    #console message for count of pictures
    print("number of pictures inspected:", count)

    #write to local file
    destination_file = "drone_exif_data.json"
    with open(destination_file, "w") as f:
        json.dump(all_the_data, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    main()

