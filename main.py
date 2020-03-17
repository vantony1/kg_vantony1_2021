# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 11:39:02 2020

@author: victo
"""
import sys

def checkMapping(first, second):
    if len(first) != len(second):
        return False 
    
    mapping = {}
    
    for i in range(len(first)):
        a = first[i]
        b = second[i]
        if a in mapping:
            if mapping[a] != b:
                return False
        else: 
            mapping[a] = b

    return True
    
def result(arg1, arg2):
    if(checkMapping(arg1, arg2) == True):
        print("true")
    else:
        print("false")

argv = sys.argv

result(argv[1], argv[2])