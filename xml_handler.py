import xml.etree.ElementTree as ET

import all_item_ids
import pak_handler
import constants

tables_pak_abs_path = "{}/Tables.pak".format(constants.kcd_data_path)

def check_for_xml_files():
    """Makes sure that all needed xml files are extracted and ready. 
       If not, will extract them from the KCD game files.
    """
    
    for filename in constants.xml_filenames:
        try:
            tree = ET.parse(constants.xml_dir_path + "/" + filename)
        except:
            print("Missing {} \nAttempting extraction...".format(filename))
            extracted_file = pak_handler.extract_file_from_pak(
                filename, 
                tables_pak_abs_path,
                "{}/xml_files".format(constants.kiwi_install_path)
            )
            if extracted_file:
                print("Extracted to: \n{}".format(extracted_file))
            else:
                print(
                    "Failed to extract {}, please extract manually to xml_files{}".format(
                        filename,
                        constants.tables_path
                    )
                )

def search_all_xml_files_for_item_id(item_id):
    files_with_id = []

    xml_files_to_search = pak_handler.get_all_filepaths_with_str_in_filename(
        tables_pak_abs_path, '.xml'
    )

    for xml_file in xml_files_to_search:
        if is_item_id_in_xml_file(xml_file, item_id):
            files_with_id.append(xml_file)
    return files_with_id

def is_item_id_in_xml_file(xml_file, item_id):
    xml__tree = ET.parse(xml_file)
    xml_root = xml__tree.getroot()

    for armor_row in xml_root.iter('row'):
        row_item_id = armor_row.get('item_id')
        if item_id == row_item_id:
            return True
    return False

def get_material_filename_from_item_id(item_id):
    """Finds the .mtl filename of the given item_id.

    Args:
        item_id (str): The item id to search for.

    Returns:
        str: The filename with the .mtl extension.
    """
    material_id = get_material_id_from_item_id(item_id)
    if material_id != "":
        material_filename = material_id + ".mtl"
        return material_filename
    else:
        print_error_message()
    
    
def get_material_id_from_item_id(item_id):
    """Gets the material ID for the given item ID.

    Args:
        item_id_to_find (str): The item ID to search for.

    Returns:
        str: The material ID.
    """
    # item_name = get_item_name_from_item_ids(item_id)
    clothing_id = get_clothing_id_from_armor_xml(item_id)
    material_id = get_material_id_from_clothing_xml(clothing_id)
    if material_id:
        return material_id
    return None

def get_clothing_id_from_armor_xml(item_id_to_find):
    """Get the clothing ID linked to a given item ID from the armor.xml file.

    Args:
        item_id_to_find (str): The item ID to search for.

    Returns:
        str: The linked clothing ID.
    """
    armor_tree = ET.parse(constants.armor_xml)
    armor_root = armor_tree.getroot()

    for armor_row in armor_root.iter('row'):
        row_item_id = armor_row.get('item_id')
        if item_id_to_find == row_item_id:
            clothing_id_to_find = armor_row.get('clothing_id')
            return clothing_id_to_find
    print_error_message('clothing ID')


def get_material_id_from_clothing_xml(clothing_id_to_find):
    """Get the material ID linked to a given item ID from the armor.xml file.

    Args:
        clothing_id_to_find (str): The clothing ID to search for.

    Returns:
        str: The linked material ID.
    """
    clothing_tree = ET.parse(constants.clothing_xml)
    clothing_root = clothing_tree.getroot()

    for clothing_row in clothing_root.iter('row'):
        row_item_id = clothing_row.get('clothing_id')
        if row_item_id == clothing_id_to_find:
            material_to_find = clothing_row.get('material')
            return material_to_find
    print_error_message('material ID')


def get_item_name_from_item_ids(item_id):
    """Get the item name of the given item id.

    Args:
        item_id (str): The id to search for.

    Returns:
        str: The item name.
    """
    item_name = all_item_ids.all_item_ids[item_id]
    if item_name:
        return item_name
    else:
        print_error_message('item name')


def print_error_message(str_input):
    print("Could not find {}, please make sure you have the correct item ID!".format(str_input))
