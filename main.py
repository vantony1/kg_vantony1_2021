# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 11:39:02 2020

@author: Victor Antony
"""
import sys

def checkMapping(first, second):
    """Function that checks for isomorphic one-to-one mapping in two strings

    Args:
        first (string): The first string.
        second (string): The second string.
    
    Returns:
        bool: True if mapping exists else False

    """
    
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
    """Function that prints "true" or "false" dependent on response from checkMapping

    Args:
        arg1 (string): The first string.
        arg2 (string): The second string.
    
    Returns:
        None
        
    """
    
    if(checkMapping(arg1, arg2) == True):
        print("true")
    else:
        print("false")

argv = sys.argv

result(argv[1], argv[2])