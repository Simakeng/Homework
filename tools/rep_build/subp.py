#! /usr/bin/env python
# -*- coding: utf-8 -*-
# ******************************************************
# Author        : simakeng
# Email         : simakeng@outlook.com
# Filename      : subp.py
# Description   : Report Builder
# ******************************************************
# This file contains commands in documentation generation.
import rep_build.envs as envs
def loadfile(args):
    arg = args[0]
    file_path = envs.locate_input_resource(arg)
    return open(file_path,encoding='utf-8').read()