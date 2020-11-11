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

input_file_path = None
input_file_dir = None

output_tex_path = None
output_tex_dir = None

def set_input(file_name):
    global input_file_path
    global input_file_dir
    input_file_path = path.abspath(file_name)
    input_file_dir = path.dirname(input_file_path)

def get_input_file():
    return input_file_path

def get_input_dir():
    return input_file_dir

def set_output(file_name):
    global output_tex_path
    global output_tex_dir
    output_tex_path = path.abspath(file_name)
    output_tex_dir = path.dirname(output_tex_path)

def get_output_file():
    return output_tex_path

def get_output_dir():
    return output_tex_dir