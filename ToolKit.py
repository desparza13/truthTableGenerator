#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 20:11:02 2021

@author: danielaesparza
"""

#Variables
import math 


proposicion=input(">>")

    
def seekVariables(proposicion):
    variables = []
    for i in proposicion:
        if (i!='V' and i!='v')and((i>='a' and i<= 'z') or (i>='A' and i<='Z')):
            if (variables.count(i)<1):
                variables.append(i)
    variables.sort()
    return variables

def printVariables(variables):
    for i in [True, False]:
        break
        
        
        
    
print(seekVariables(proposicion))
