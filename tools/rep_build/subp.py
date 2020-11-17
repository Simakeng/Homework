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

def archive(args):
    return '详情请见附件'

def loadfile(args):
    arg = args[0]
    file_path = envs.locate_input_resource(arg)
    return open(file_path, encoding='utf-8').read()

def spice_graph(args):
    input_raw_file = envs.locate_output_resource(args[0])
    output_img_file = path.join(envs.output_tex_dir,args[1])
    args[0] = '"%s"' % input_raw_file
    args[1] = '"%s"' % output_img_file
    os.system('python "%s" %s' % (path.join('tools', 'spice_graph.py'),' '.join(args)))

def spice_exec(args):
    arg = args[0]
    file_path = envs.locate_input_resource(arg)
    out_dir = envs.output_tex_dir
    os.system('python "%s" "%s" "%s"' %
              (path.join('tools', 'spice_exec.py'), file_path, out_dir))
