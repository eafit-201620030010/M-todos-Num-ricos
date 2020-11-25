import numpy as np
import tabulate as tb
from tabulate import tabulate
from sympy import *
tb.PRESERVE_WHITESPACE = True

x = symbols('x')
init_printing(use_unicode=False)

def vandermonde(puntos):
        print('---puntos---')
        print(puntos)
        grado = len(puntos) - 1
        matriz = []
        for i in puntos:
                row = []
                for j in range(grado,-1,-1):
                        row.append(i[0]**j)
                matriz.append(row)
        matriz = np.array(matriz,dtype=np.float64)
        print('---matriz A---')
        print(tabulate(matriz))
        vector = []
        for i in puntos:
                vector.append([i[1]])
        vector = np.array(vector,dtype=np.float64)
        print('---vector x---')
        print(tabulate(vector))
        sol = gauss(matriz, vector)
        print('---Coeficientes---')
        print(sol)
        expr = sympify('0')
        aux = grado
        for j in sol:
                expr = expr + sympify(str(j) + '*x**' + str(grado))
                grado += -1
        print('---Polinomio .............---')
        print(pretty(expr))
        print(expr)
        poli = expr 
        return [matriz, vector, sol, poli]


def checkSquare(array):
        rows = len(array)
        for i in range (0,rows):
                if len(array[i]) != rows:
                        raise Exception('La matriz debe ser cuadrada')
        return rows

def checkDet(array):
        det = np.linalg.det(array)
        #print('Determinante: ' + str(det))
        if det == 0: raise Exception('La determinante de la matriz debe ser diferente a cero')
        tol = 10e-4
        if abs(det) < tol:
                option = getOption('La determinante es menor a ' + str(tol) 
                        + ' y puede presentar problemas de evaluación ¿Desea continuar? si[s] no[n]',['s','n'])
                if option == 'n': raise Exception('Operación abortada por el usuario')

def pivoteoTotal(array, col, dimension, orden):
        subArray = array[col:,col:-1]
        dimSubArray = len(subArray)
        index = np.argmax(abs(array[col:,col:-1]))
        rowCol = getRowCol(index,dimSubArray,col)
        interCol(array,col,rowCol[1])
        inter1D(orden,col,rowCol[1])
        interRow(array,col,rowCol[0])
        return
def getRowCol(index, dimSub, corner):
        row = int(index / dimSub) 
        col = index % dimSub
        return [row + corner,col + corner]
def interCol(array, col1, col2):
        if col1 != col2:
                aux = array[:,col1].copy()
                array[:,col1] = array[:,col2]
                array[:,col2] = aux
def interRow(array, row1, row2):
        if row1 != row2:
                aux = array[row1].copy()
                array[row1] = array[row2]
                array[row2] = aux
def inter1D(array, pos1, pos2):
        aux = array[pos1]
        array[pos1] = array[pos2]
        array[pos2] = aux

def sumMultRow(array, rowAct, rowMult, mult, init):
        array[rowAct,init:] = array[rowAct,init:] + mult * array[rowMult,init:]

def sustitution(array):
        #print('---Sustitución regresiva---')
        dimension = len(array)
        solution = []
        #np.dot(A,B)
        for row in range(dimension - 1, -1, -1):
                variable = (array[row,dimension] - np.dot(array[row,row + 1:dimension],solution)) / array[row,row]
                #print('X' + str(row) + ' = ' + str(variable))
                solution.insert(0,variable)
        #solNumpy(array)
        return np.array(solution)



def gauss(matriz, vector):
        dimension = checkSquare(matriz)
        checkDet(matriz)

        array = np.zeros((dimension,dimension + 1))
        array[:,:-1] = matriz
        array[:,-1:] = vector

        orden = np.arange(dimension)
        cont = 0
        #print('---Etapa 0, matriz original---')
        #print(tabulate(array,floatfmt='.6f'))
        for col in range(0,dimension-1):
                pivoteoTotal(array, col, dimension, orden)
                for row in range(col+1,dimension):
                        mult = -(array[row,col]/array[col,col])
                        sumMultRow(array,row,col,mult,col)
                cont += 1
                #print('---Etapa ' + str(cont) + ', haciendo 0 la columna ' 
                #       + str(col) + '---')
                #print(tabulate(array,floatfmt='.6f'))
        sol = sustitution(array)
        for i in range(0,len(orden)):
                inter1D(sol,i,orden[i])
                inter1D(orden,i,orden[i])
        np.set_printoptions(precision=6)
        #print('Después de aplicar sustitución regresiva: ' + str(sol))
        return sol


