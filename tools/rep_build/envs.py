#! /usr/bin/env python
# -*- coding: utf-8 -*-
# ******************************************************
# Author        : simakeng
# Email         : simakeng@outlook.com
# Filename      : rep_build.py
# Description   : Report Builder
# ******************************************************
# This file contains enviroments settings
from os import path
import re

input_file_path = None
input_file_dir = None

output_tex_path = None
output_tex_dir = None

def set_input(file_name):
    global input_file_path
    global input_file_dir
    input_file_path = path.abspath(file_name)
    input_file_dir = path.dirname(input_file_path)

def set_output(file_name):
    global output_tex_path
    global output_tex_dir
    output_tex_path = path.abspath(file_name)
    output_tex_dir = path.dirname(output_tex_path)

def locate_input_resource(file_name):
    if(path.sep == '\\'):
        if(re.search(r'^\w:',file_name)):
            return file_name
        # Windows
    elif(path.sep == '/'):
        if(file_name.startsWith('/')):
            return file_name
        # *nix
    else:
        raise NotImplementedError('Unknow Platform')

    abs_path = path.abspath(path.join(input_file_dir,file_name))
    rel_path = path.abspath(file_name)

    if(path.exists(rel_path)):
        return rel_path
    
    return abs_path

def locate_output_resource(file_name):
    if(path.sep == '\\'):
        if(re.search(r'^\w:',file_name)):
            return file_name
        # Windows
    elif(path.sep == '/'):
        if(file_name.startsWith('/')):
            return file_name
        # *nix
    else:
        raise NotImplementedError('Unknow Platform')

    abs_path = path.abspath(path.join(output_tex_dir,file_name))
    rel_path = path.abspath(file_name)

    if(path.exists(rel_path)):
        return rel_path
    
    return abs_path