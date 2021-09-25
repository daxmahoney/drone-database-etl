# Subtask 2.1 - Parse JSON and upload images/files into S3. Return S3 URI once uploaded.
# local file location: 'C:/Users/G-Unit/Desktop/Arisa/VDJ2021/drone-database-etl-copy/data'


import boto3
from file_crawler import get_file_locations, get_root_structure
from metadata_extraction import extract_metadata, clean_metadata

# Get file_paths
root = input('File Location:')
root_structure = get_root_structure(root)
img_files, other_files = get_file_locations(root_structure)

# Get metadata of images
imgs_metadata = [clean_metadata(extract_metadata(img_file)) for img_file in img_files]
imgs_filenames = [root+x['imglocation'] for x in imgs_metadata]

# Check file names
print(imgs_filenames)


# Instantiate s3
s3 = boto3.client('s3')

# Upload files into s3
# For each filepath
for i in range(4, 6):
    file_location = img_files[i]
    file_name = imgs_filenames[i]
    file_metadata = imgs_metadata[i]

    s3.upload_file(file_location, 'part1-test1', file_name,
                   ExtraArgs={'Metadata': file_metadata})


