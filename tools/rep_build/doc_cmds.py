#! /usr/bin/env python
# -*- coding: utf-8 -*-
# ******************************************************
# Author        : simakeng
# Email         : simakeng@outlook.com
# Filename      : doc_cmds.py
# Description   : Report Builder
# ******************************************************
# This file contains commands in documentation generation.
import re
import os
import sys
import time
import getpass
import regex as re
import os.path as path
import rep_build.envs as envs
import rep_build.subp as subp
current_module = sys.modules[__name__]

default_args = {
    "title": "PLEASE SET REPORT TITLE!",
    "author": getpass.getuser(),
    "date": time.strftime("%Y-%m-%d"),
    "department": "",
    "subject": ""
}


def graph(args):
    file_path = envs.locate_input_resource(args)
    if(not path.exists(file_path)):
        file_path = envs.locate_output_resource(args)
        if(not path.exists(file_path)):
            raise Exception('img file not found! (' + args + ')')
    return "\\begin{center}\n\\includegraphics[width=0.7\\textwidth]{%s}\n\\end{center}" % file_path.replace(path.sep, '//')


def tex_safe(s):
    return s.replace('\n', r'\\ ')


def subject(args):
    global default_args
    default_args['subject'] = tex_safe(args)


def department(args):
    global default_args
    default_args['department'] = tex_safe(args)


def title(args):
    global default_args
    default_args['title'] = tex_safe(args)
    return None


def author(args):
    global default_args
    default_args['author'] = tex_safe(args)


def date(args):
    global default_args
    default_args['date'] = tex_safe(args)


def section(args):
    return r'\section{%s}' % tex_safe(args)


def subsection(args):
    return r'\subsection{%s}' % tex_safe(args)


def _apply_doc_header(template):
    res = []
    template = template.replace('%<department>%', default_args['department'])
    template = template.replace('%<title>%', default_args['title'])
    template = template.replace('%<subject>%', default_args['subject'])
    res.append(r'\author{%s}' % default_args['author'])
    res.append(r'\date{%s}' % default_args['date'])
    template = template.replace('%<header>%', '\n'.join(res))
    return template


def code(args):
    return '\\begin{lstlisting}[frame=shadowbox]\n' + args + '\n\\end{lstlisting}'

def newpage(dummy):
    return '\\newpage'

def exec(codes):
    codes = [code.strip() for code in codes.split('\n')]
    sym_table = {}
    for code in codes:
        if(code.startswith('#')):
            continue
        var = re.search(r'(?<=\s*)\w(\w|\d)+(?=\s*=\s*.+)', code)
        if(var):
            var = var.group()
            code = '='.join(code.split('=')[1:])

        code = code.strip()
        subprocess, args = (lambda x: (x[0], x[1:]))(code.split(' '))
        func_subp = getattr(subp, subprocess, None)
        if(subprocess != 'echo'):
            if(not func_subp):
                print('No such subprocess: %s' % subprocess)
                continue

            res = func_subp(args)
            if(var):
                sym_table[var] = res
        else:
            # echo
            args = ' '.join(args)
            for sym_name in sym_table.keys():
                args = args.replace('%%%s' % sym_name, sym_table[sym_name])
            command_name = re.search(
                r'(?<=^\s*\$\s*)\w[\w\d]+(?=\s*(:|\{))', args)
            if(command_name):
                command_name = command_name.group()
            m = re.search('(?<=' + command_name + r'\s*:).*', args)
            if(m):
                # cmd: arg
                args = m.group()
            else:
                m = re.search(
                    r'(?<=' + command_name + r'\s*\{)(\n|.)+(?=\})', args)
                if(m):
                    args = m.group()
                else:
                    raise Exception('echo missing arguments!')
            func = getattr(current_module, command_name, None)
            if(func):
                return func(args)
            else:
                raise Exception('echo no such command: %s' % command_name)
