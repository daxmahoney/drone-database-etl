# Subtask 2 - Extract metadata from images using Pillow, and transform some of them as needed.

from file_crawler import get_root_structure, get_file_locations
from PIL import Image, JpegImagePlugin
from PIL.ExifTags import TAGS
import os
import defusedxml


def extract_metadata(path_to_img):

    img_metadata = {}
    image = Image.open(path_to_img)
    exif_data = image.getexif()

    for tag_id in exif_data:
        tag = TAGS.get(tag_id, tag_id)
        metadata = exif_data.get(tag_id)
        if isinstance(metadata, bytes):
            metadata = metadata.decode()
        img_metadata[tag] = metadata

    return img_metadata


if __name__ == "__main__":

    example_img = 'C:/Users/G-Unit/Desktop/Arisa/VDJ2021/' \
                  'drone-database-etl-copy/data/Part1/Images/100_0006_0001 (2).JPG'

    print(os.path.getsize(example_img))
    metadata_dict = extract_metadata(example_img)

    for k,v in metadata_dict.items():
        print(f'{k}:{v}')
    print('======')

    img1 = Image.open(example_img)

    for k, v in img1.info.items():
        print(f'{k}:{v}')

    print(type(metadata_dict['XPKeywords']))

    print('=======')

    print(img1.format)
    print(img1.mode)
    print(img1.size)
    print(img1.filename)
    print(img1.palette)

    print('==========')

    img = JpegImagePlugin.JpegImageFile(example_img)
    print(img.format)
    print(img.getxmp())

    for k, v in img.getxmp()['xmpmeta']['RDF']['Description'].items():
        print(f'{k}:{v}')


