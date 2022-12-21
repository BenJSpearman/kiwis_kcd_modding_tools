import os
from zipfile import ZipFile

import constants


def extract_file_from_pak(filename, pak_path, dst_path):
    """Extracts a single file from a given pak, to the given destination.

    Args:
        filename (str): The file to extract, with the extension.
        pak_path (str): The pak to extract from.
        dst_path (str): The path to extract the file to.

    Returns:
        str: The path of the extracted file.
    """
    rel_filepath = get_rel_filepath_from_pak(pak_path, filename)
    if rel_filepath:
        extracted_file = extract_filepath_from_pak(pak_path, rel_filepath, dst_path)
        return extracted_file
    else:
        return None

def extract_multiple_files_from_pak(filenames, pak_path, dst_path):
    failed_extractions = []
    for file in filenames:
        extracted_file = extract_file_from_pak(file, pak_path, dst_path)
        if extracted_file:
            print(extracted_file)
        else:
            failed_extractions.append(file)
    if failed_extractions:
        print('\n'.join(failed_extractions))

def get_rel_filepath_from_pak(pak_path, filename):
    """Finds the relative filepath for a given filename within a .pak. 
    This will search all dirs.

    Args:
        pak_path (str): The absolute path of the .pak to search.
        filename (str): The name of the file to search for, with the extension.

    Returns:
        str(optional): The filepath relative to the given .pak path.
    """
    with ZipFile(pak_path, 'r') as pak:
        files_in_pak = pak.namelist()
        for file_path in files_in_pak:
            path_tail = os.path.split(file_path)[1]
            if path_tail == filename:
                return file_path
        return None

def get_all_filepaths_with_str_in_filename(pak_path, search_str):
    """Gets the relative filepath of a file containing the search string.

    Args:
        pak_path (str): The pak to search.
        search_str (str): The string to search for.

    Returns:
        str: The filepath of the found file.
    """
    file_paths = []
    with ZipFile(pak_path, 'r') as pak:
        files_in_pak = pak.namelist()
        for file_path in files_in_pak:
            path_tail = os.path.split(file_path)[1]
            if search_str in path_tail:
                file_paths.append(file_path)
        return file_paths

# def get_all_files_with_filename_str_in_pak(pak_path, search_str):


def find_cloth_pak_containing_material(material_id):
    """Gets the cloth pak path that contains the files for the material_id.

    Args:
        material_id (str): The material id to search for.

    Returns:
        str: The path of the pak containg the material files.
    """
    pak_paths = get_cloth_pak_paths()
    for pak in pak_paths:
        if get_all_filepaths_with_str_in_filename(pak, material_id):
            return pak
    return None

def get_cloth_pak_paths():
    cloth_pak_paths = []
    cloth_pak_names = ['Cloth-part0.pak', 'Cloth-part1.pak', 'Cloth-part2.pak']
    for pak in cloth_pak_names:
        pak_path = constants.kcd_data_path + "/" + pak
        cloth_pak_paths.append(pak_path)
    return cloth_pak_paths

def extract_filepath_from_pak(pak_path, filepath, extract_dst):
    """Extracts a known relative filepath from a given .pak file.

    Args:
        pak_path (str): The path of the .pak to extract from.
        filepath (str): The relative path of the file to extract.
        extract_dst (str): The absolute path to extract to.

    Returns:
        str: The path the file was extracted to, or None if failure.
    """
    try:
        with ZipFile(pak_path, 'r') as pak:
            pak.extract(filepath, extract_dst)
            pak.close()
        return extract_dst
    except Exception as exc:
        print(exc)
        return None

def extract_multiple_files_from_pak(pak_path, files_to_extract, extract_dst):
    failed_to_extract = []
    for filepath in files_to_extract:
        extracted_file = extract_filepath_from_pak(pak_path, filepath, extract_dst)
        if extracted_file:
            continue
        else:
            failed_to_extract.append(filepath)
    
    if failed_to_extract:
        print("Failed to extract the following file(s):\n")
        print('\n'.join(failed_to_extract))
