#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 01:29:08 2021

@author: danielaesparza jenniferhernandez
"""

import math 
import variables as v



#------------------------------Funciones SetUp----------------------

def seekVariables(proposition): #Buscar variables en la proposición y guardarlas en un arreglo
    proposition.lower() #Convertir todo a minúsculas para una mejor interpretación
    variables = []
    
    for i in proposition: 
        if (i!='V' and i!='v')and((i>='a' and i<= 'z')): #Ignorar las V porque son un operador, y checar que sea letra
            if (variables.count(i)<1): #Checar que no sea variable repetida
                variables.append(i) #Añadirla
                
    variables.sort() #Ordenarlas alfabeticamente
    return variables

#----------------------------------------------------------------------

def seekNegatedVariables(proposition): #Buscar las variables negadas en la proposición
    proposition.lower() #Convertir todo a minúsculas para una mejor interpretación
    negatedVariables = []
    
    for i in range(0, len(proposition)-1, 1):
        if(proposition[i]=="~")or(proposition[i]=="-")or(proposition[i]=="¬"):#Buscar los símbolos de negación (tres opciones: -, ~, ¬)
            if(proposition[i+1]>="a")and(proposition[i+1]<="z"):#Checar que el símbolo este acompañado de una letra
                if (negatedVariables.count(proposition[i+1])<1):#Checar que no esté repetido
                    negatedVariables.append(proposition[i+1])#Añadirla
    
    negatedVariables.sort()#Ordenarlas alfabeticamente
    return negatedVariables

#----------------------------------------------------------------------

def seekParenthesis(proposition): #Busca los parentesis de inicio y fin y regresa sus indexes
    openParenthesis = []
    closeParenthesis = []
    
    for i in range(0, len(proposition), 1):
        if (proposition[i]=='('): #Si encuentra un parentesis abierto añade su indice
            openParenthesis.append(i)
            
        if (proposition[i]==')'): #Si encuentra el cierre de un parentesis añade su indice
            closeParenthesis.append(i)
            
    closeParenthesis.reverse() #Invierte el orden de los indices de cerrar para poder emparejarlos a los parentesis que abren
    return openParenthesis,closeParenthesis

#----------------------------------------------------------------------
            
def getExpressions(proposition): #Obtener las expresiones por separado según sus parentesis
    expressions = []
    expression=""
    openParanthesis,closeParenthesis=seekParenthesis(proposition)
    for i in range(0,len(openParanthesis),1): #Por cada par de paréntesis
        for j in range(openParanthesis[i],closeParenthesis[i]+1,1): #Copiar la expresión desde donde abre hasta donde cierra el paréntesis
            expression=expression+proposition[j]
        expressions.append(expression) #Añadir la expresión al banco/array de expresiones
        expression="" #Vaciar la expresión para recomenzar
    
    expressions.reverse() #Ordenarlo de menor a mayor para que se vea de manera progresiva en la tabla de verdad
    return expressions
#----------------------------------------------------------------------

def saveValues(variables):
    variableValues = []
    values = []
    proportions = []
    varFinal=[]
    multiply=1
    for i in range(0,len(variables),1): #Obtener las proporciones, es decir el valor de 2^n-1 de cada variable
        proportions.append(2**i)
            
    for i in range(0,len(variables)+1,1): #Guarda una copia de 1vez la proporción de True y 1 vez la proporción de False
        for j in range(0,proportions[i-1],1): #Agrega los True
            values.append(True)
        for j in range(0,proportions[i-1],1): #Agrega los False
            values.append(False)
        values=[]
        variableValues.append(values) #Aquí te queda algo del tipo (p,q)={p=True,True,False,False} {q=True,False}


    for i in range(0,len(variableValues)-1,1): #Guarda todos los valores de la variable para llenar la tabla
        multiply=int((2**len(variables))/(proportions[i]*2))
        varFinal.append(variableValues[i]*multiply)  #Aquí te queda algo del tipo (p,q)={p=True,True,False,False} {q=True,False,True,False}
        
            
    return varFinal
    
#----------------------------------------------------------------------

def saveNegatedValues(variables):
    variableValues = []
    values = []
    proportions = []
    varFinal=[]
    multiply=1
    for i in range(0,len(variables),1): #Obtener las proporciones, es decir el valor de 2^n-1 de cada variable
        proportions.append(2**i)
            
    for i in range(0,len(variables)+1,1): #Guarda una copia de 1vez la proporción de True y 1 vez la proporción de False
        for j in range(0,proportions[i-1],1): #Agrega los True
            values.append(False)
        for j in range(0,proportions[i-1],1): #Agrega los False
            values.append(True)
        values=[]
        variableValues.append(values) #Aquí te queda algo del tipo (p,q)={p=True,True,False,False} {q=True,False}


    for i in range(0,len(variableValues)-1,1): #Guarda todos los valores de la variable para llenar la tabla
        multiply=int((2**len(variables))/(proportions[i]*2))
        varFinal.append(variableValues[i]*multiply)  #Aquí te queda algo del tipo (p,q)={p=True,True,False,False} {q=True,False,True,False}
        
            
    return varFinal

#----------------------------------------------------------------------

def setUp():
    v.proposition=input(">>")
    v.variables=(seekVariables(v.proposition))
    v.varValues=(saveValues(v.variables))
    v.negatedVariables=seekNegatedVariables(v.proposition)
    v.varNegatedValues=saveNegatedValues(v.variables)
    v.expression=getExpressions(v.proposition)

#----------------------------------------------------------------------

def trySetUp():
    print("Proposition",v.proposition)
    print("Variables",v.variables)
    print("Variable values",v.varValues)
    print("Negated variables",v.negatedVariables)
    print("Negated variables values",v.varNegatedValues)
    print("Expressions",v.expression)


















   