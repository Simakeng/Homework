#! /usr/bin/env python
# -*- coding: utf-8 -*-
# ******************************************************
# Author        : simakeng
# Email         : simakeng@outlook.com
# Filename      : subp.py
# Description   : Report Builder
# ******************************************************
# This file contains commands in documentation generation.
import os
import os.path as path
import rep_build.envs as envs


def loadfile(args):
    arg = args[0]
    file_path = envs.locate_input_resource(arg)
    return open(file_path, encoding='utf-8').read()


def spice_exec(args):
    arg = args[0]
    file_path = envs.locate_input_resource(arg)
    out_dir = envs.output_tex_dir
    os.system('python "%s" "%s" "%s"' %
              (path.join('tools', 'spice_exec.py'), file_path, out_dir))
