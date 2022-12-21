import os
import xml.etree.ElementTree as ET
import pak_handler
import xml_handler
import constants

test_pak_path = "{}/Cloth-part0.pak".format(constants.kcd_data_path)
material_id = "s1_p3_l1_v0_tx002"

test_dds_file = os.path.abspath('Objects/characters/humans/cloth/s1_p2_l2_v0_tx012b_diff.dds.7')


# item_xml_rel_path = '/Libs/Tables/item/item.xml'
pak_handler.extract_filepath_from_pak(test_pak_path, test_dds_file, constants.textures_dir_path)
# xml_handler.check_for_xml_files()
