#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Import Modules
from click import style
from lib.helper import *


# Style class
N = '\033[0m'
W = '\033[1;37m' 
B = '\033[1;34m' 
M = '\033[1;35m' 
R = '\033[1;31m' 
G = '\033[1;32m' 
Y = '\033[1;33m' 
C = '\033[1;36m' 


class Log:

    @classmethod
    def info(self,text):
 	    print("["+Y+"*"+N+"] ["+G+"INFO"+N+"] "+text)
 
    @classmethod
    def warning(self,text):
	    print("["+Y+"+"+N+"] ["+Y+"WARNING"+N+"] "+text)

    @classmethod
    def high(self,text):
 	    print("["+Y+"-"+N+"] ["+R+"CRITICAL"+N+"] "+text)
