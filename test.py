import os
import xml.etree.ElementTree as ET
import zipfile
from zipfile import ZipFile

import pak_handler
import xml_handler
import extract_textures
import constants

test_item_id = "46857626-d7c9-985d-4acc-a6ad9a79afa2"

# test_pak_path = "{}/Cloth-part0.pak".format(constants.kcd_data_path)
# material_id = "s1_p3_l1_v0_tx002"

# test_dds_file = 'Objects/characters/humans/cloth/s1_p2_l2_v0_tx012b_diff.dds.1'
# print(test_dds_file)

# test_path = "Cloth-part0.pak/" + test_dds_file
# print(test_path)

# z_path = zipfile.Path(test_pak_path, test_dds_file)
# print(z_path)


# with ZipFile(test_pak_path, 'r') as pak:
#     pak.extract(z_path, constants.TEXTURES_EXTRACT_PATH)
#     pak.close()
# extracted_file = pak_handler.extract_filepath_from_pak(z_path, test_pak_path, constants.TEXTURES_EXTRACT_PATH)
# print(extracted_file)

# xml_handler.check_for_xml_files()

extract_textures.extract_textures_of_item_id_from_cloth_paks(test_item_id)
