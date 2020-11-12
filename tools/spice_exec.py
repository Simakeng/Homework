#! /usr/bin/env python
# -*- coding: utf-8 -*-
# ******************************************************
# Author        : simakeng
# Email         : simakeng@outlook.com
# Filename      : spice_exec.py
# Description   : spice file executor
# ******************************************************
# This file loads sp net list and pass it to spice
import os
import sys
import json
import shutil
import subprocess
import regex as re
import os.path as path

root_dir = path.abspath(path.dirname(path.dirname(__file__)))
config_dir = path.join(root_dir, 'config.json')
if(not path.exists(config_dir)):
    print('config.json not found.')
    print('please run "configure" first')
    sys.exit(1)

config = json.loads(open(config_dir, encoding='utf-8').read())
ltspice_dir = config['LTSpice']


def main():
    input_file = sys.argv[1]
    input_dir = path.dirname(input_file)
    file_name = input_file[input_file.rfind('\\')+1:]
    output_dir = sys.argv[2]
    if(not path.exists(input_file)):
        print('[spice_exec] %s not found!' % input_file)
        return

    spice_content = open(input_file, encoding='utf-8').read()

    # 处理相对路径
    def dir_repl(s):
        return path.abspath(path.join(input_dir, s.group()))

    spice_content = re.sub(
        r'(?<=\s*\.lib\s*(\'|")).*(?=(\'|"))', dir_repl, spice_content)

    os.makedirs(output_dir, exist_ok=True)
    targit_path = path.join(output_dir, file_name)
    with open(targit_path, 'w', encoding='utf-8') as f:
        f.write(spice_content)
    try:
        print('[spice_exec] executing...')
        print(subprocess.check_output('"%s" -b "%s"' %
                                      (ltspice_dir, targit_path)).decode())
    except Exception as ex:
        print("[spice_exec]" + str(ex))
    log_path = path.join(output_dir,file_name[:file_name.rfind('.')] + '.log')
    raw_path = path.join(output_dir,file_name[:file_name.rfind('.')] + '.raw')
    if(path.exists(log_path)):
        print(open(log_path).read())
    if(path.exists(raw_path)):
        print('[spice_exec] simulation successed!')
        print('[spice_exec] saved to %s.' % raw_path)


if __name__ == "__main__":
    main()
