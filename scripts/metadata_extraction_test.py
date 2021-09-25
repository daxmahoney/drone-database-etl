# Subtask 1.2 - Extract metadata from images using Pillow, and transform some of them as needed.
# Subtask 1.3 - Define JSON structure and work collaboratively to generate a standard JSON for each file

# TODO 1. Access more metadata 'stage', 'colorprofile', 'focallength', 'alpha',
#                              'redeye', fnumber', 'metering', 'exposure', 'exposuretime'
# TODO 2. Clean dictionary contents
# TODO 3. Add try/except statements

from PIL import Image, JpegImagePlugin
from PIL.ExifTags import TAGS
import os
import json


def extract_metadata(path_to_img: str) -> dict:
    """
    Returns dictionary with metadata from image
    --------------------------------------------
    Input: path to the image file (str)
    Output: dictionary with metadata
    """
    img_metadata = {}
    image = Image.open(path_to_img)
    exif_data = image.getexif()

    # Get general data
    img_metadata['filename'] = image.filename
    img_metadata['colorspace'] = image.mode
    img_metadata['imgwidth'] = image.width
    img_metadata['imgheight'] = image.height

    # Get exif_data
    for tag_id in exif_data:
        tag = TAGS.get(tag_id, tag_id)
        metadata = exif_data.get(tag_id)
        if isinstance(metadata, bytes):
            metadata = metadata.decode()
        img_metadata[f'exif_{tag}'] = metadata

    # Get xmp data
    image_jpeg = JpegImagePlugin.JpegImageFile(path_to_img)
    image_jpeg_data = image_jpeg.getxmp()

    for tag_, metadata_ in image_jpeg_data['xmpmeta']['RDF']['Description'].items():
        img_metadata[f'xmp_{tag_}'] = metadata_

    return img_metadata


def clean_metadata(metadata_dictionary):
    """

    """
    clean_metadata = {}

    filename_args = metadata_dictionary['filename'].split('/')
    clean_metadata['stage'] = filename_args[-3].lower()
    clean_metadata['filename'] = filename_args[-1][:-4]
    clean_metadata['imglocation'] = '/'.join(filename_args[-3:])

    data_to_keep = ['imgwidth', 'imgheight',
                    'exif_DateTime', 'exif_ImageDescription'
                    'xmp_CreateDate', 'xmp_Make', 'xmp_Model',]

    for md_k, md_v in metadata_dictionary.items():
        if md_k in data_to_keep:
            clean_metadata[md_k] = md_v

    return clean_metadata


def metadata_dict_to_json(clean_metadata_dict):
    """
    Returns structured JSON from input dictionary
    ---------------------------------------------
    input: dictionary of file metadata
    output: clean metadata json
    """
    clean_metadata_json = json.dumps(clean_metadata_dict)

    return clean_metadata_json


if __name__ == "__main__":

    example_img = 'C:/Users/G-Unit/Desktop/Arisa/VDJ2021/' \
                  'drone-database-etl-copy/data/Part1/Images/100_0006_0001 (2).JPG'

    print(os.path.getsize(example_img))
    metadata_dict = extract_metadata(example_img)

    for k, v in metadata_dict.items():
        print(f'{k}:{v}')

    print('======')

    print(metadata_dict_to_json(metadata_dict))
