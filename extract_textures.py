import os

import xml_handler
import pak_handler
import constants

# 46857626-d7c9-985d-4acc-a6ad9a79afa2

def main():
    extract_textures_of_item_id()


def extract_textures_of_item_id():

    item_id = input("Item ID to search for: ")

    item_name = xml_handler.get_item_name_from_item_ids(item_id)
    print("Item name linked to ID: {}".format(item_name))

    material_id = xml_handler.get_material_id_from_item_id(item_id)
    print("{} material ID: {}".format(item_name, material_id))

    pak_path = pak_handler.find_cloth_pak_containing_material(material_id)
    print(os.path.split(pak_path)[1])

    file_paths = pak_handler.get_all_filepaths_with_str_in_filename(pak_path, material_id)

    for path in file_paths:
        pak_handler.extract_file_from_pak(pak_path, path, constants.textures_dir_path)

if __name__ == "__main__":
    main()
