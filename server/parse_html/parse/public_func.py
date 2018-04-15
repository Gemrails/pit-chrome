#!/usr/bin/python
#coding=utf-8

import uuid
import os

def write_txt(path, text):
    filepath = "{0}/{1}".format(path, create_name())
    print "filepath is {}".format(filepath)
    with open (filepath, 'w') as f:
        f.write(text)
    os.chown(filepath, 100, 101)

def create_name():
    return str(uuid.uuid1)+".search"