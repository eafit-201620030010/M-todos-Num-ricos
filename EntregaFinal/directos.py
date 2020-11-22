#!/usr/bin/env python
# -*- coding: utf-8 -*-

from functions import *
from pivoteo import *
import math

# ***********************************************************************************************
def valorMatriz(Matriz):

    nuevaMatriz = []

    for i in range(len(Matriz)):

        fila = []

        for j in range(len(Matriz[0])):

            fila.append(Matriz[i][j])

        nuevaMatriz.append(fila)

    return nuevaMatriz

def matrizAumentada(A, b):

    matrizAumentada = []

    copiaDeA = valorMatriz(A)

    for i in range(len(copiaDeA)):

        copiaDeA[i].append(b[i])

        matrizAumentada.append(copiaDeA[i])

    return matrizAumentada

def imprimirMatriz(Matriz): 
    for fila in Matriz: print(fila)


def sustitucionRegresiva(Ab):

    x = []

    for pivotIndex in range((len(Ab) - 1), -1, -1):

        summation = i =  0

        for column in range((len(Ab[0]) - 2), pivotIndex, -1):

            summation +=  Ab[pivotIndex][column] * x[i]

            i += 1

        x.append( ( Ab[pivotIndex][len(Ab[0]) - 1] - summation ) / Ab[pivotIndex][pivotIndex] )

    return x[::-1]

# ***********************************************************************************************

def sustitucionProgresiva(Ab):

    x = []

    for pivotIndex in range(len(Ab)):

        summation = i =  0

        for column in range(pivotIndex):
            
            summation += Ab[pivotIndex][column] * x[i]

            i += 1

        x.append( (Ab[pivotIndex][len(Ab[0]) - 1] - summation) / Ab[pivotIndex][pivotIndex] )

    return x

# ***********************************************************************************************

def gaussianaSimple(AbParam, n):
    
    #AbParam es la matriz aumentada Ab
    #n = len(AbParam)
    etapas = [] 

    Ab = valorMatriz(AbParam)

    etapas.append(valorMatriz(Ab))

    # Eliminación

    for k in range(n - 1):

        multiplicadoresDeEtapa = []

        for i in range(k + 1, n):

            multiplicator = Ab[i][k] / Ab[k][k]

            for j in range(k, n + 1):

                Ab[i][j] = Ab[i][j] - ( multiplicator * Ab[k][j] )

        etapas.append(valorMatriz(Ab))

    
    for i in range (len(etapas)):
        print("Etapa",i,":")
        imprimirMatriz(etapas[i])
        print(" ")

    #print("Etapa ", len(etapas), ": ")
    #imprimirMatriz(etapas[-1]) #etapas[-1] es lo mismo que decir etapas en la ultima posicion   

    #Sustitucion regresiva:
    x = sustitucionRegresiva(Ab)

    print(etapas)
    print(x)
    return [etapas, x]

# ***********************************************************************************************

def gaussianaPivoteoParcial(AbParam, n):

    etapas = [] 
    etapasPrevias = []
    filaMayorList = []

    Ab = valorMatriz(AbParam)

    # Eliminación

    for k in range(n - 1):

        etapasPrevias.append(valorMatriz(Ab))
        filaMayor = pivoteoParcial(Ab, k, n)
        filaMayorList.append(filaMayor)
        etapas.append(valorMatriz(Ab))
        
        multiplicadoresDeEtapa = []
        
        for i in range(k + 1, n):
        
            multiplicator = Ab[i][k] / Ab[k][k]

            for j in range(k, n + 1):
            
                Ab[i][j] = Ab[i][j] - ( multiplicator * Ab[k][j] )


    etapasPrevias.append(valorMatriz(Ab))
    etapas.append(valorMatriz(Ab))
    
    # Sustitución regresiva
    x = sustitucionRegresiva(Ab)

    return [etapas, x, filaMayorList, etapasPrevias]

# ***********************************************************************************************

def gaussianaPivoteoTotal(AbParam, n):

    etapas = [] 
    etapasPrevias = []
    mayorList = []
    
    marcas = []

    for i in range(n): marcas.append(i)

    Ab = valorMatriz(AbParam)

    # Eliminación

    for k in range(n - 1):

        etapasPrevias.append(valorMatriz(Ab))

        mayorIndex = pivoteoTotal(Ab, k, n, marcas)
        
        filaMayor = mayorIndex[0]
        columnaMayor = mayorIndex[1]

        mayorList.append([filaMayor, columnaMayor])
        etapas.append(valorMatriz(Ab))
        
        multiplicadoresDeEtapa = []
        
        for i in range(k + 1, n):
        
            multiplicator = Ab[i][k] / Ab[k][k]

            for j in range(k, n + 1):
            
                Ab[i][j] = Ab[i][j] - ( multiplicator * Ab[k][j] )


    etapasPrevias.append(valorMatriz(Ab))
    etapas.append(valorMatriz(Ab))
    
    # Sustitución regresiva
    x = sustitucionRegresiva(Ab)

    return [etapas, x, mayorList, etapasPrevias, marcas]

# ***********************************************************************************************

def factorizacionDirecta(A, n, b, metodo):

    etapas = []

    L = matrizIdentidad(n)
    U = matrizIdentidad(n)
  
    if metodo == "Crout": 
        for i in range(n): L[i][i] = 0
    elif metodo == "Doolittle": 
        for i in range(n): U[i][i] = 0

    for k in range(n):
 
        suma1 = 0

        for p in range(k):

            suma1 += L[k][p] * U[p][k]

        if metodo == "Crout": 
            L[k][k] = A[k][k] - suma1
        elif metodo == "Doolittle": 
            U[k][k] = A[k][k] - suma1
        elif metodo == "Cholesky":
            try:  
                L[k][k] = math.sqrt(A[k][k] - suma1)
                U[k][k] = L[k][k]
            except:
                print("No se puede realizar el metodo porque hay un numero negativo en la raiz, no se trabaja con imaginarios")

        for i in range(k + 1, n):

            suma2 = 0

            for p in range(k):

                suma2 += L[i][p] * U[p][k]
        
            L[i][k] = (A[i][k] - suma2) / float(U[k][k])

        for j in range(k + 1, n):

            suma3 = 0

            for p in range(k):

                suma3 += L[k][p] * U[p][j]
 
            U[k][j] = (A[k][j] - suma3) / float(L[k][k])

        etapas.append([valorMatriz(L), valorMatriz(U)])
    
    Lb = matrizAumentada(L, b)
    
    z = sustitucionProgresiva(Lb)

    Uz = matrizAumentada(U, z)

    x = sustitucionRegresiva(Uz)

    return [etapas, x, z, Lb, Uz]

'''A = [[36., 3., -4., 5.], [5., -45., 10., -2.], [6., 8., 57., 5.], [2., 3., -8., -42.]]
b = [-20., 69., 96., -32.]

result = factorizacionDirecta(A, len(A), b, "Crout")

for i in range(len(result[3])):

    imprimirMatriz(result[3][i][0])
    print()
    imprimirMatriz(result[3][i][1])
    print("***************************************")'''

# ***********************************************************************************************

def elimination(AbParam, n, tipo):

    Ab = valorMatriz(AbParam)

    multiplicadores = []
    etapas = [] 
    
    etapas.append(valorMatriz(Ab))
    
    for k in range(n - 1):

        if tipo == 1: pivoteoParcial(Ab, k, n)
        elif tipo == 2: pivoteoTotal(Ab, k, n)

        multiplicadoresDeEtapa = []
        
        for i in range(k + 1, n):
        
            multiplicator = Ab[i][k] / Ab[k][k]
            multiplicadoresDeEtapa.append(str(Ab[i][k]) + " / " + str(Ab[k][k]))

            for j in range(k, n + 1):
            
                Ab[i][j] = Ab[i][j] - ( multiplicator * Ab[k][j] )

        etapas.append(valorMatriz(Ab))
        multiplicadores.append(multiplicadoresDeEtapa)

    return [etapas, multiplicadores]

def factorizdacionDirecta(A, n, metodo):
    
    etapas = []

    l = identityMatrix(n)
    u = identityMatrix(n)
  
    if metodo == 0: 
        for i in range(n): l[i][i] = 0 # Crout
    elif metodo == 1: 
        for i in range(n): u[i][i] = 0 # Doolittle


    for k in range(n):

        suma1 = 0

        for p in range(k):

            suma1 += l[k][p] * u[p][k]

        if metodo == 0: l[k][k] = A[k][k] - suma1 # Crout
        elif metodo == 1: u[k][k] = A[k][k] - suma1 # Doolittle

        for i in range(k + 1, n):

            suma2 = 0

            for p in range(k):

                suma2 += l[i][p] * u[p][k]
        
            l[i][k] = (A[i][k] - suma2) / float(u[k][k])

        for j in range(k + 1, n):

            suma3 = 0

            for p in range(k):

                suma3 += l[k][p] * u[p][j]
 
            u[k][j] = (A[k][j] - suma3) / float(l[k][k])

    return [l, u]


def factorizacionLU(A):

    marks = []

    for i in range(len(A)): marks.append(i)

    for pivotIndex in range(len(A) - 1):

        #partialPivoting(M, marks, pivotIndex)

        for row in range(pivotIndex + 1, len(A)):
        
            mult = A[row][pivotIndex] / A[pivotIndex][pivotIndex]

            for column in range(pivotIndex, len(A[0])):
            
                A[row][column] = A[row][column] - ( mult * A[pivotIndex][column] )

            A[row][pivotIndex] = mult

    auxMforL = copyMatrix(A)
    auxMforU = copyMatrix(A)

    U = generateU(auxMforU) 
    L = generateL(auxMforL)
    
    return [L, U, marks]
