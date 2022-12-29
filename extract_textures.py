import os

import xml_handler
import pak_handler
import constants

# 46857626-d7c9-985d-4acc-a6ad9a79afa2

# def main():
#     """Main.
#     """
#     extract_textures_of_item_id_from_cloth_paks()


def extract_textures_of_item_id_from_cloth_paks(item_id=None):
    """Extracts all of the textures for given item ID from the correct cloth paks.
    Currently, this only works for armor IDs as it only extracts from cloth paks.
    """
    if not item_id:
        item_id = input("Item ID to search for: ")

    xml_handler.check_for_xml_files()
    item_name = xml_handler.get_item_name_from_item_ids(item_id)
    print(f"Item name linked to ID: {item_name}")

    material_id = xml_handler.get_material_id_from_item_id(item_id)
    print(f"{item_name} material ID: {item_name}")

    pak_path = pak_handler.find_cloth_pak_containing_material(material_id)
    print(os.path.split(pak_path)[1])

    # file_paths = pak_handler.get_all_filepaths_with_str_in_filename(pak_path, material_id)

    filenames = pak_handler.get_all_filenames_with_str_in_filename(pak_path, material_id)
    pak_handler.find_and_extract_filenames_from_pak(filenames, pak_path, constants.TEXTURES_EXTRACT_PATH)
    # for path in file_paths:
    #     path = os.path(path)
    #     pak_handler.extract_filepath_from_pak(pak_path, path, constants.textures_dir_path)
    return "Finished"
# if __name__ == "__main__":
#     main()
