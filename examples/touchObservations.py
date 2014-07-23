#!/usr/bin/env python 
# -*- coding: utf-8 -*-

 
import glob 
import os
 
os.chdir("/home/usuario/ctpython/examples/observations/")
 
for file_ in glob.glob("*"):
    os.system("touch "+file_)



