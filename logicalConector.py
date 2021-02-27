#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 19:32:34 2021

@author: danielaesparza jenniferhernandez
"""
import math 
import setUp as su
import variables as v
import pandas

def searchConector(expression):
    expression=expression.lower()
    for i in expression:
        if i == 'v':
            return "v"
        elif i=="^":
            return "^"
        elif i=="→" or i=="->":
            return "->"
        elif i=="↔" or i=="<->":
            return "<->"
        
#---------------------------LOGIC CONNECTORS---------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------
def logicOr(expression):
    varInExpression=su.seekVariables(expression)
    exp=[]
    for i in range(0,2**len(v.variables),1):
        if v.values.get(varInExpression[0])[i] == False and v.values.get(varInExpression[1])[i] == False:
            exp.append(False)
        else:
            exp.append(True)
    v.expValues[expression]=exp
    

def logicAnd(expression):
    varInExpression=su.seekVariables(expression)
    exp=[]
    for i in range(0,2**len(v.variables),1):
        if v.values.get(varInExpression[0])[i] == True and v.values.get(varInExpression[1])[i] == True:
            exp.append(True)
        else:
            exp.append(False)
    v.expValues[expression]=exp
    
def logicConditional(expression):
    varInExpression=su.seekVariables(expression)
    exp=[]
    for i in range(0,2**len(v.variables),1):
        if v.values.get(varInExpression[0])[i] == True and v.values.get(varInExpression[1])[i] == False:
            exp.append(False)
        else:
            exp.append(True)       
    v.expValues[expression]=exp

def logicBiconditional(expression):
    varInExpression=su.seekVariables(expression)
    exp=[]
    for i in range(0,2**len(v.variables),1):
        if v.values.get(varInExpression[0])[i] == True and v.values.get(varInExpression[1])[i] == False:
            exp.append(False)   
        elif v.values.get(varInExpression[0])[i] == False and v.values.get(varInExpression[1])[i] == True:
            exp.append(False)
        else:
            exp.append(True)       
    v.expValues[expression]=exp
 #------------------------------------------------------------------------------------------------------------------------
def operate(expression):
    conector=searchConector(expression)
    if(conector=="v"):
        logicOr(expression)
    elif (conector=="^"):
        logicAnd(expression)
    elif (conector=="→" or conector=="->"):
        logicConditional(expression)
    elif (conector=="↔" or conector=="<->"):
        logicBiconditional(expression)
    v.evaluatedExp=v.evaluatedExp+1
    
def evaluateFirst():
    operate(v.expression[0])

def saveAll():
    data=[]
    dataAux=[]
    headers=[]
    print("LEn",len(v.variables))
    for i in range(0,i<(2**len(v.variables)),1):
        for j in range(0, i<len(v.variables),1):
            print(j)
            dataAux.append(v.values.get(v.variables[i])[j])
        data.append(dataAux)
    for i in range(0,i<len(v.variables),1):
        headers.append(v.variables[i])
    print(data)
    print(pandas.DataFrame(data, headers, headers))
            
            
        
            
    
    
    
def imprimirPrueba():
    print("Expressions values",v.expValues)


     
    