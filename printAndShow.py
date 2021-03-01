#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 19:19:02 2021

@author: danielaesparza jenniferhernandez
"""

import math 
import setUp as su
import variables as v
import logicalConector as log 
import pandas as pd

def printRevision():

    var = pd.DataFrame(v.values.values(),index=v.values.keys())
    noVar=pd.DataFrame(v.negatedValues.values(),index=v.negatedValues.keys())
    exp = pd.DataFrame(v.expValues.values(),index=v.expression)
    print("\nProposition:",v.proposition,"\n")
    print("Variables")
    print(var,"\n")
    print("\Variables negadas que aparecen en el enunciado: ")
    print(v.negatedVariables,"\n")
    print("Negated variables")
    print(noVar,"\n")
    print("Expressions (Los valores solo son correctas para la primera expresion de momento)")
    print(exp,"\n")
    
    
