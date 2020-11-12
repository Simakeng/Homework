#! /usr/bin/env python
# -*- coding: utf-8 -*-
# ******************************************************
# Author        : simakeng
# Email         : simakeng@outlook.com
# Filename      : configure.py
# Description   : spice file executor
# ******************************************************
# This file ask user to configure enviroment arguments
# and scan all avaliable rep to generate an makefile.

import os
import sys
import json
import subprocess 
import regex as re
from os import path

root_dir = path.abspath(path.dirname(path.dirname(__file__)))

def configure():
    # xelatex
    xelatex_path = subprocess.check_output('where xelatex').decode().replace('\r\n','')
    # iverilog    
    iverilog_path = subprocess.check_output('where iverilog').decode().replace('\r\n','')
    # LTSpice
    if(path.exists(r'C:\Program Files\LTC\LTspiceXVII\XVIIx64.exe')):
        ltspice_path = r'C:\Program Files\LTC\LTspiceXVII\XVIIx64.exe'
    else:
        ltspice_path = input('ltspice simulator not found, please specify:\n')
        if(len(ltspice_path.strip()) == 0):
            print('aborted.')
            sys.exit(1)
        if(not path.exists(ltspice_path)):
            print('%s is not a valid path.' % ltspice_path)
            sys.exit(1)
    with open(path.join(root_dir,'config.json'),'w',encoding='utf-8') as f:
        config = {
            "LTSpice" : ltspice_path,
            "xelatex" : xelatex_path,
            "iverilog" : iverilog_path
        }
        f.write(json.dumps(config,ensure_ascii=False))
    pass

def find_all_rep_file(root):
    reps = []
    for subdir in os.listdir(root):
        if(not path.isdir(path.join(root,subdir))):
            continue
        if(subdir.startswith('.')):
            continue
        reps += find_all_rep_file(path.join(root,subdir))
    for file in os.listdir(root):
        if(not path.isfile(path.join(root,file))):
            continue
        if(file.endswith('.rep')):
            reps.append(path.join(root,file))
    return reps

def main():
    if(not path.exists(path.join(root_dir,'config.json'))):
        configure()
    reps = find_all_rep_file(root_dir)
    print('%d targets successfuly generated.' % len(reps))
    print('type "make help" to view all targets.')

if __name__ == "__main__":
    main()