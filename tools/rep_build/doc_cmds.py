#! /usr/bin/env python
# -*- coding: utf-8 -*-
# ******************************************************
# Author        : simakeng
# Email         : simakeng@outlook.com
# Filename      : rep_build.py
# Description   : Report Builder
# ******************************************************
# This file contains commands in documentation generation.
import re
import time
import getpass
import os.path as path
import rep_build.envs as envs

default_args = {
    "title": "PLEASE SET REPORT TITLE!",
    "author": getpass.getuser(),
    "date": time.strftime("%Y-%m-%d"),
    "department" : "",
    "subject": ""
}
def graph(args):
    input_dir = envs.input_file_dir
    abs_path = path.abspath(path.join(input_dir,args))
    rel_path = path.abspath(args)

    if(path.exists(rel_path)):
        return "\\begin{center}\n\\includegraphics[width=0.7\\textwidth]{%s}\n\\end{center}" % rel_path.replace(path.sep,'//')
    elif(path.exists(abs_path)):
        return "\\begin{center}\n\\includegraphics[width=0.7\\textwidth]{%s}\n\\end{center}" % abs_path.replace(path.sep,'//')
    else:
        raise Exception('img file not found! (' + args + ')')

def tex_safe(s):
    return s.replace('\n',r'\\ ')

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
    template = template.replace('%<department>%',default_args['department'])
    template = template.replace('%<title>%',default_args['title'])
    template = template.replace('%<subject>%',default_args['subject'])
    res.append(r'\author{%s}' % default_args['author'])
    res.append(r'\date{%s}' % default_args['date'])
    template = template.replace('%<header>%','\n'.join(res))
    return template