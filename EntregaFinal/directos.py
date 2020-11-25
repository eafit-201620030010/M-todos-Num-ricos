#!/usr/bin/env python
# -*- coding: utf-8 -*-

from functions import *
from pivoteo import *
import math
import numpy as np
from math import sqrt
from tabulate import tabulate


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


# LU con gaussianaSimple y Lu con pivoteo parcial
def getOption(message, options):
        while True:
                ans = input(message)
                for i in options:
                        if i == ans:
                                return i
def interRow(array, row1, row2):
        if row1 != row2:
                aux = array[row1].copy()
                array[row1] = array[row2]
                array[row2] = aux

def interCol(array, col1, col2):
        if col1 != col2:
                aux = array[:,col1].copy()
                array[:,col1] = array[:,col2]
                array[:,col2] = aux


def solNumpy(array):
        A = array[:,0:-1]
        B = array[:,-1]
        solution = np.linalg.solve(A, B)
        return solution
def sumMultRow(array, rowAct, rowMult, mult, init):
        array[rowAct,init:] = array[rowAct,init:] + mult * array[rowMult,init:]
def checkSquare(array):
        rows = len(array)
        for i in range (0,rows):
                if len(array[i]) != rows:
                        raise Exception('La matriz debe ser cuadrada')
        return rows
def checkDet(array):
        det = np.linalg.det(array)
        print('Determinante: ' + str(det))
        if det == 0: raise Exception('La determinante de la matriz debe ser diferente a cero')
        tol = 10e-4
        if abs(det) < tol:
                option = getOption('La determinante es menor a ' + str(tol) 
                        + ' y puede presentar problemas de evaluación ¿Desea continuar? si[s] no[n]',['s','n'])
                if option == 'n': raise Exception('Operación abortada por el usuario')


def pivoteoParcial(array, col, dimension):
        maxRow = np.argmax(abs(array[col:,col])) + col
        interRow(array,col,maxRow)
        return

def progSustitution(array):
        print('---Sustitución progresiva---')
        dimension = len(array)
        solution = []
        #np.dot(A,B)
        for row in range(0, dimension):
                variable = (array[row,dimension] - np.dot(array[row,0:row],solution)) / array[row,row]
                solution.append(variable)
        #solNumpy(array)
        return np.array(solution)

def LUGauss(matriz):
        dimension = checkSquare(matriz)
        checkDet(matriz)
        etapas2 = []
        cont = 0
        print('---Etapa 0, matriz original---')
        #print(tabulate(matriz,floatfmt='.6f'))
        etapas2.append('---Etapa 0, matriz original---')
        print("----------here-------")
        print(matriz)
        print("----------here-------")
        etapas2.append(matriz)
        U = np.zeros((dimension,dimension))
        L = np.identity(dimension)
        for col in range(0,dimension):          
                for row in range(col+1,dimension):
                        mult = -(matriz[row,col]/matriz[col,col])
                        L[row,col] = -mult
                        sumMultRow(matriz,row,col,mult,col)
                U[col] =  matriz[col]
                cont += 1
                print('---Etapa ' + str(cont) + '---')
                etapas2.append('---Etapa ' + str(cont) + '---')
                print('L')
                etapas2.append('---L---')
                etapas2.append(L)
                #print(tabulate(L,floatfmt='.6f'))
                print('U')
                etapas2.append('---U---')
                etapas2.append(U)
                #print(tabulate(U,floatfmt='.6f'))

        return L,U,etapas2

def LUGaussVector(matriz, vector):

        tabla = []
        dimension = len(matriz)
        array = np.zeros((dimension,dimension + 1))
        array[:,:-1] = matriz
        array[:,-1:] = vector
        numpySol = solNumpy(array)

        L, U, etapas2 = LUGauss(matriz)
        tabla.append(L)
        tabla.append(U)
        tabla.append(etapas2)
        Larr = np.zeros((dimension,dimension + 1))
        Larr[:,:-1] = L
        Larr[:,-1:] = vector
        print('Dado el sistema Lz = b')
        #print(tabulate(Larr,floatfmt='.6f'))
        print('Aplicamos sustitución progresiva y obtenemos')
        pSus = progSustitution(Larr)
        print(pSus)
        Uarr = np.zeros((dimension,dimension + 1))
        Uarr[:,:-1] = U
        Uarr[:,-1] = pSus
        print('Dado el sistema Ux = z')
        #print(tabulate(Uarr,floatfmt='.6f'))
        print('Aplicamos sustitución regresiva y obtenemos')
        print(sustitution(Uarr))
        sus = sustitution(Uarr)
        print('---Opcional---')
        print('La solución de  es: ' + str(numpySol))
        mensaje = 'La solución de  es: ' + str(numpySol) 

        return [tabla, mensaje, sus]

def LUGaussPivoteoParcial(matriz):

        etapas = [] 
        dimension = checkSquare(matriz)
        checkDet(matriz)

        cont = 0
        print('---Etapa 0, matriz original---')
        #print(tabulate(matriz,floatfmt='.6f'))

        etapas.append('---Etapa 0, matriz original---')
        etapas.append(matriz) 
        A = matriz
        P = np.identity(dimension)
        L = np.zeros((dimension,dimension))

        for col in range(0,dimension):  

                maxRow = np.argmax(abs(A[col:,col])) + col
                interRow(A,col,maxRow)
                interRow(P,col,maxRow)
                interRow(L,col,maxRow)

                for row in range(col+1,dimension):
                        mult = -(A[row,col]/A[col,col])
                        L[row,col] = -mult
                        sumMultRow(A,row,col,mult,col)
                #U[col] =  matriz[col]
                cont += 1
                print('---Etapa ' + str(cont) + '---')
        
                etapas.append('---Etapa ' + str(cont) + '---')
                print('P')
                #print(tabulate(P,floatfmt='.6f'))
                etapas.append('---P---')
                etapas.append(P) 
                print('A')
                #print(tabulate(A,floatfmt='.6f'))
                etapas.append('---A---')
                etapas.append(A)

        print('---Última etapa---')     
        etapas.append('---Última etapa---')
        U = np.array(A, copy=True)
        print('U = A =')
        #print(tabulate(U,floatfmt='.6f'))
        etapas.append('U = A =')
        etapas.append(U)
        print('Se construye la matriz L con los multiplicadores almacenados')
        etapas.append('Se construye la matriz L con los multiplicadores almacenados')
        np.fill_diagonal(L, 1)
        
        print('L')
        #print(tabulate(L,floatfmt='.6f'))
        etapas.append('---L---')
        etapas.append(L)
        print('P')

        #print(tabulate(P,floatfmt='.6f'))
        etapas.append('---P---')
        etapas.append(P)
        return L,U,P, etapas

def LUGaussPivoteoParcialVector(matriz, vector):

        tabla= []

        dimension = len(matriz)

        array = np.zeros((dimension,dimension + 1))
        array[:,:-1] = matriz
        array[:,-1:] = vector
        numpySol = solNumpy(array)

        L, U, P, etapas = LUGaussPivoteoParcial(matriz)
        tabla.append(L)
        tabla.append(U)
        tabla.append(P)
        tabla.append(etapas)
        Bn = np.matmul(P,vector)
        print('Calculamos el producto Pb = Bn')
        #print(tabulate(Bn,floatfmt='.6f'))
        Larr = np.zeros((dimension,dimension + 1))
        Larr[:,:-1] = L
        Larr[:,-1:] = Bn
        
        print('Dado el sistema Lz = Bn')
        #print(tabulate(Larr,floatfmt='.6f'))
        print('Aplicamos sustitución progresiva y obtenemos')
        pSus = progSustitution(Larr)
        print(pSus)
        Uarr = np.zeros((dimension,dimension + 1))
        Uarr[:,:-1] = U
        Uarr[:,-1] = pSus
        print('Dado el sistema Ux = z')
        #print(tabulate(Uarr,floatfmt='.6f'))
        print('Aplicamos sustitución regresiva y obtenemos')
        print(sustitution(Uarr))
        sus2 = sustitution(Uarr)
        print('---Opcional---')
        print('La solución de  es: ' + str(numpySol))
        mensaje2 = 'La solución de  es: ' + str(numpySol)
        
        return [tabla, mensaje2, sus2]

def sustitution(array):
        print('---Sustitución regresiva---')
        dimension = len(array)
        solution = []
        #np.dot(A,B)
        for row in range(dimension - 1, -1, -1):
                variable = (array[row,dimension] - np.dot(array[row,row + 1:dimension],solution)) / array[row,row]
                #print('X' + str(row) + ' = ' + str(variable))
                solution.insert(0,variable)
        #solNumpy(array)
        return np.array(solution)

