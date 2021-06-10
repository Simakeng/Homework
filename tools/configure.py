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

root_dir = path.dirname(path.dirname(path.abspath(__file__)))
root_dir = root_dir[0].upper() + root_dir[1:]


def configure():
    # xelatex
    xelatex_path = subprocess.check_output(
        'where xelatex').decode().replace('\r\n', '')
    # iverilog
    iverilog_path = subprocess.check_output(
        'where iverilog').decode().replace('\r\n', '')
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
    with open(path.join(root_dir, 'config.json'), 'w', encoding='utf-8') as f:
        config = {
            "LTSpice": ltspice_path,
            "xelatex": xelatex_path,
            "iverilog": iverilog_path
        }
        f.write(json.dumps(config, ensure_ascii=False))
    pass


def detect_rep_info(path):
    with open(path, encoding='utf-8') as f:
        content = f.read()
    subject = re.search(r'(?<=\$\s*subject\s*:(\s|\n)+).*', content)
    title = re.search(r'(?<=\$\s*title\s*:(\s|\n)+).*', content)
    index = re.search(r'(?<=\$\s*index\s*:(\s|\n)+).*', content)
    subject = subject.group() if subject else ''
    title = title.group() if title else ''
    index = index.group() if index else ''
    return title, subject, index


def find_all_rep_file(root):
    reps = []
    for subdir in os.listdir(root):
        if(not path.isdir(path.join(root, subdir))):
            continue
        if(subdir.startswith('.')):
            continue
        reps += find_all_rep_file(path.join(root, subdir))
    for file in os.listdir(root):
        if(not path.isfile(path.join(root, file))):
            continue
        if(file.endswith('.rep')):
            reps.append(path.join(root, file))
    return reps


def generate_makefile(reps):
    with open('makefile', 'w', encoding='utf-8') as f:
        f.write('rep_build = python tools/rep_builder.py\n')
        f.write('targit help:\n')
        f.write('\t@echo Targets:\n')
        reps = [detect_rep_info(rep)+(rep,) for rep in reps]
        ltitle = 0
        lsubj = 0
        indexs = {}
        targits = []
        for title, subject, index, file_name in reps:
            if index in indexs.keys():
                indexs[index] += 1
            else:
                indexs[index] = 1
            index = "%s%d" % (index, indexs[index])
            ltitle = max(ltitle, len(title))
            lsubj = max(lsubj, len(subject))
            root_dir = os.path.abspath('.') + os.path.sep
            input_path = file_name.replace(root_dir, '')
            filename = input_path.split(os.path.sep)[-1]
            filename_no_ext = '.'.join(filename.split('.')[:-1])
            output_path = path.join("build", path.dirname(
                input_path), filename_no_ext + '.tex')
            targits.append({
                "title": title,
                "subject": subject,
                "index": index,
                "input_path": input_path,
                "output_path": output_path
            })

        for targit in targits:
            f.write('\t@echo make %s: %s %s\n' %
                    (targit['index'], targit['title'].ljust(ltitle), targit['subject'].ljust(lsubj)))

        f.write('\n')

        for targit in targits:
            f.write(f'{targit["index"]}:\n')
            f.write(
                f'\t$(rep_build) "{targit["input_path"]}" "{targit["output_path"]}"\n\n')


def main():
    if(not path.exists(path.join(root_dir, 'config.json'))):
        configure()
    reps = find_all_rep_file(root_dir)

    generate_makefile(reps)
    print('%d targets successfuly generated.' % len(reps))
    print('type "make help" to view all targets.')


if __name__ == "__main__":
    main()
