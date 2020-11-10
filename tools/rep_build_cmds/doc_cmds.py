#! /usr/bin/env python
# -*- coding: utf-8 -*-
# ******************************************************
# Author        : simakeng
# Email         : simakeng@outlook.com
# Filename      : rep_build.py
# Description   : Report Builder
# ******************************************************
# This file contains commands in documentation generation.

import time
import getpass

default_args = {
    "title": "PLEASE SET REPORT TITLE!",
    "author": getpass.getuser(),
    "date": time.strftime("%Y-%m-%d"),
}

def title(args):
    global default_args
    default_args['title'] = args
    return None

def author(args):
    global default_args
    default_args['author'] = args

def date(args):
    global default_args
    default_args['date'] = args

def section(args):
    return r'\section{%s}' % args

def subsection(args):
    return r'\subsection{%s}' % args

def _gen_doc_header():
    res = []
    res.append(r'\title{%s}' % default_args['title'])
    res.append(r'\author{%s}' % default_args['author'])
    res.append(r'\date{%s}' % default_args['date'])
    return '\n'.join(res)