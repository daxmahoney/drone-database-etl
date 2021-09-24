# Subtask 2 - Extract metadata from images using Pillow, and transform some of them as needed.

# TODO 1. Access more metadata 'stage', 'colorprofile', 'focallength', 'alpha',
#                              'redeye', fnumber', 'metering', 'exposure', 'exposuretime'
# TODO 2. Clean dictionary contents
# TODO 3. Add try/except statements

from PIL import Image, JpegImagePlugin
from PIL.ExifTags import TAGS
import os


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


if __name__ == "__main__":

    example_img = 'C:/Users/G-Unit/Desktop/Arisa/VDJ2021/' \
                  'drone-database-etl-copy/data/Part1/Images/100_0006_0001 (2).JPG'

    print(os.path.getsize(example_img))
    metadata_dict = extract_metadata(example_img)

    for k, v in metadata_dict.items():
        print(f'{k}:{v}')

