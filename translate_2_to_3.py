import glob
import subprocess
import os

CMD_BASE = f"2to3 -f all -f idioms -f set_literal -f ws_comma -f buffer -w"

if __name__ == "__main__":
    py_file_list = glob.glob('./python/ofdm/*.py')
    print(len(py_file_list))
    print(py_file_list[0])
    
    # Remove __init__.py from the list

    init_file_idx = [i for i, py_file in enumerate(py_file_list) if py_file.endswith('__init__.py')]
    print(len(init_file_idx))

    if (len(init_file_idx) > 1):
        raise ValueError(
            f"Trying to remove {len(init_file_idx)} (>1) files from list"
            f", check for more __init__.py in dir?"
        )
    else:
        del py_file_list[init_file_idx[0]]
    
    print(len(py_file_list))

    for py_file in py_file_list:
        subprocess.run(
                (f"{CMD_BASE} {py_file}"),
                shell=True,
                check=True
            )