import re
import subprocess
import os
import shutil
from .config.path import *
from .config.config import *
import time


def get_pure_name(file_name: str) -> str:
    if file_name is None:
        return file_name
    name = file_name
    if re.search('/', file_name):
        name = file_name.split('/')[-1]
    if re.search('\.', name):
        name = name.split('.')[0]
    return name


def fix_direction(file_name: str) -> str:
    file_name = get_pure_name(file_name)
    folder, extension = OUTPUT_PATH['dot']
    dot_in_path = f'{folder}/{file_name}.{extension}'
    folder, extension = OUTPUT_PATH['gv']
    gv_out_path = f'{folder}/{file_name}.{extension}'

    dot_command = f'{DOT} {dot_in_path} -Grankdir=TB -o {gv_out_path}'
    subprocess.call([dot_command], shell=True)
    os.remove(dot_in_path)


def convert_verilog_to_gv(file_name: str) -> None:

    file_name = get_pure_name(file_name)

    folder, extension = OUTPUT_PATH['ver']
    verilog_in_path = f'{folder}/{file_name}.{extension}'
    # print(f'{verilog_in_path = }')
    folder, extension = OUTPUT_PATH['gv']
    gv_out_path = f'{folder}/{file_name}.{extension}'

    yosys_command = f"""
        read_verilog {verilog_in_path}
        opt
        clean
        show -prefix {gv_out_path[:-3]} -format gv
        """
    with open(f'yosys_graph.log', 'w') as y:
        subprocess.call([YOSYS, '-p', yosys_command], stdout=y)
    fix_direction(file_name)



def setup_folder_structure():
    # Setting up the folder structure
    directories = [OUTPUT_PATH['ver'][0], OUTPUT_PATH['aig'][0], OUTPUT_PATH['gv'][0], OUTPUT_PATH['z3'][0],
                   OUTPUT_PATH['report'][0], OUTPUT_PATH['figure'][0], TEST_PATH['tb'][0], TEST_PATH['z3'][0]]

    for directory in directories:
        if ~os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)


def clean_all():
    directories = [OUTPUT_PATH['ver'][0], OUTPUT_PATH['aig'][0], OUTPUT_PATH['gv'][0], OUTPUT_PATH['z3'][0],
                   OUTPUT_PATH['report'][0], OUTPUT_PATH['figure'][0], TEST_PATH['tb'][0], TEST_PATH['z3'][0]]

    for directory in directories:
        if os.path.exists(directory):
            shutil.rmtree(directory)


def check_graph_equality(G1, G2):
    if G1.graph.adj == G2.graph.adj and \
       G1.graph.nodes == G2.graph.nodes and \
       G1.graph.edges == G2.graph.edges and \
       G1.input_dict == G2.input_dict and \
       G1.output_dict == G2.output_dict and \
       G1.gate_dict == G2.gate_dict and \
       G1.constant_dict == G2.constant_dict:
        return True
    else:
        return False
