#! /usr/bin/env python
# -*- coding: utf-8 -*-
# ******************************************************
# Author        : simakeng
# Email         : simakeng@outlook.com
# Filename      : rep_build.py
# Description   : Report Builder
# ******************************************************
import sys
import argparse
import regex as re

file_name = r'src\IC CAD\C1\report.rep'
out_file_name = r'build\IC CAD\C1\report.tex'


def perror(*args):
    for arg in args:
        print(arg, file=sys.stderr, end=' ')
    print('', file=sys.stderr)


if __name__ == "__main__":
    with open(file_name, encoding='utf-8') as f:
        lines = [line for line in f]
        line_lens = [len(line) for line in lines]
        raw_file_content = ''.join(lines)
        line_indexs = [0] + [sum(line_lens[:i+1]) for i in range(len(line_lens))]
        lines = [line[:-1] if line.endswith('\n') else line for line in lines]

    line_count = len(lines)

    lines = dict(zip(list(range(len(lines))), lines))

    current_line = 0

    find_error = False

    while current_line < line_count:
        line_content = lines[current_line]
        if(line_content.startswith('$')):
            # Parse command
            command_name = re.search(
                r'(?<=^\s*\$\s*)\w[\w\d]+(?=\s*:|\{)', line_content)
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
                current_line += 1
                command_arg = lines[current_line]
            elif(line_content.find('{') != -1):
                # parse command block
                beg_cnt = 1
                beg_index = raw_file_content.find('{',line_indexs[current_line])
                cur_index = beg_index + 1
                while(beg_cnt != 0):


            current_line += 1   
        else:         
            current_line += 1            
                

    if(find_error):
        sys.exit(1)
