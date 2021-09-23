# Subtask 1 - Crawl through the directories to obtain file structure, file name, file type, and other useful information

import os


def get_root_structure(filepath):
    """
    Get the file structure of the file path and return a dictionary
    --------------------------------------------------------------
    Input: "file path" (str)
    Output: a dictionary with 'sub_root':['file1', 'file2', ...]"""
    root_structure = {}
    try:
        for root in os.walk(str(filepath)):
            root_structure[root[0]] = root[2]
    except UnboundLocalError:
        print("Please check your file path.")
    return root_structure


def get_file_locations(folder_dictionary):
    """
    Get the file paths of all the images (.JPG format)
    ------------------------------------------------------------------
    Input: a dictionary of path and images as "path":['file1.jpg', 'file2.jpg', ...]
    Output: a list of image locations: ['file1.jpg', 'file2.jpg', ...]"""
    img_locations = []
    other_files = []
    try:
        for k, v in folder_dictionary.items():
            header = k.replace('\\', '/')
            img_locations = [f'{header}/{filename}' for filename in v if '.JPG' in filename]
            other_files += [f'{header}/{filename}' for filename in v if '.JPG' not in filename]
        if len(img_locations) < 0:
            print("There are no image files.")
        return img_locations, other_files
    except UnboundLocalError:
        print("Please check that your folder contains files.")


if __name__ == "__main__":

    # entry_point = input("Folder location:")
    entry_point = 'C:/Users/G-Unit/Desktop/Arisa/VDJ2021/drone-database-etl-copy/data'

    folder_dict = get_root_structure(entry_point)
    img_paths, file_paths = get_file_locations(folder_dict)

    print('folder_dict', folder_dict)

    print('Image Files:')
    for img in img_paths:
        print(img)
    print('====')

    print('Other Files:')
    for fil in file_paths:
        print(fil)
