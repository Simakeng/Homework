#! /usr/bin/env python
# -*- coding: utf-8 -*-
# ******************************************************
# Author        : simakeng
# Email         : simakeng@outlook.com
# Filename      : rep_build.py
# Description   : Report Builder
# ******************************************************
# This file is used to generate homework report.
import os
import sys
import getpass
import argparse
import regex as re
from os import path
from functools import reduce
import rep_build.doc_cmds as cmds
import rep_build.envs as envs
from rep_build.doc_cmds import _apply_doc_header

file_name = r'src\IC CAD\C1\report.rep'
out_file_name = r'build\IC CAD\C1\report.tex'
envs.set_input(file_name)
envs.set_output(out_file_name)


def perror(*args):
    for arg in args:
        print(arg, file=sys.stderr, end=' ')
    print('', file=sys.stderr)


def execute_cmd(cmd, arg):
    if(cmd.startswith('_')):
        perror('Command error : No such command "%s"' % cmd)
        return ''
    executor = getattr(cmds, cmd, None)
    if(executor):
        return executor(arg)
    perror('Command error : No such command "%s"' % cmd)
    return ''


if __name__ == "__main__":
    with open(file_name, encoding='utf-8') as f:
        lines = [line for line in f]
        line_lens = [len(line) for line in lines]
        raw_file_content = ''.join(lines)
        line_indexs = [0] + [sum(line_lens[:i+1])
                             for i in range(len(line_lens))]
        lines = [line[:-1] if line.endswith('\n') else line for line in lines]


    lines = dict(zip(list(range(len(lines))), lines))

    current_line = 0

    find_error = False
    result_contents = []

    line_count = len(lines)
    while current_line < line_count:
        line_content = lines[current_line]
        try:
            if(line_content.startswith('$')):
                # Parse command
                command_name = re.search(
                    r'(?<=^\s*\$\s*)\w[\w\d]+(?=\s*(:|\{))', line_content)
                if(command_name):
                    command_name = command_name.group()
                else:
                    perror('Synatax Error in File "%s", line %d' %
                           (file_name, current_line))
                    find_error = True
                    current_line += 1
                    continue

                if(line_content.find(':') != -1):
                    # next line as arg
                    command_arg = line_content[line_content.find(':') + 1:]
                    current_line += 1
                    command_arg += lines[current_line]
                    command_arg = command_arg.strip()
                    pass
                elif(line_content.find('{') != -1):
                    # parse command block
                    beg_cnt = 1
                    beg_index = raw_file_content.find(
                        '{', line_indexs[current_line])
                    end_index = beg_index + 1
                    while(beg_cnt != 0):
                        if(raw_file_content[end_index] == '{'):
                            beg_cnt += 1
                        elif(raw_file_content[end_index] == '}'):
                            beg_cnt -= 1
                        end_index += 1
                    command_arg = raw_file_content[beg_index:end_index]
                    command_line_count = reduce(
                        lambda x, y: x + 1 if y == '\n' else x, command_arg, 0)
                    command_arg = command_arg[1:-1].strip()
                    current_line += command_line_count
                    pass

                result = execute_cmd(command_name, command_arg)
                result_contents.append(result)
                current_line += 1
            else:
                result_contents.append(line_content)
                current_line += 1
        except Exception as ex:
            print(ex)
            current_line+=1
            find_error = True
    if(find_error):
        sys.exit(1)

    while(None in result_contents):
        result_contents.remove(None)
    template = open(path.join(path.dirname(
        __file__), "rep_template.tex"), encoding='utf-8').read()

    os.makedirs(path.dirname(out_file_name), exist_ok=True)
    with open(out_file_name, 'w', encoding='utf-8') as f:
        template = _apply_doc_header(template)
        template = template.replace('%<body>%', '\n'.join(result_contents))
        f.write(template)
