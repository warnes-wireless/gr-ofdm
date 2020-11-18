import glob
import subprocess
import os

CMD_BASE = f"pybombs -p defpref run gr_modtool update"

if __name__ == "__main__":
    xml_file_list = glob.glob('./grc/*.xml')
    print(len(xml_file_list))
    print(xml_file_list[0])
    # print(xml_file_list[0][xml_file_list[0].find('ofdm')+5:-4])
    # Strip the path and extension manually from the blocks
    for idx, xml_file in enumerate(xml_file_list):
        stripped_name = xml_file_list[idx][xml_file_list[idx].find('ofdm')+5:-4]
        xml_file_list[idx] = stripped_name
    print(len(xml_file_list))
    print(xml_file_list[0])

    # call the command with each found file
    for xml_file in xml_file_list:
        subprocess.run(
            f"pybombs -p defpref run gr_modtool update {xml_file}",
            shell=True,
            check=True
        )