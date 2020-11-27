import math
import numpy as np
from tabulate import tabulate
from sympy import *
import matplotlib.pyplot as plt

from functions import *



A = [[45., 13., -4., 8.], [-5., -28., 4., -14.], [9., 15., 63., -7.], [2., 3., -8., -42.]]
b = [-25., 82., 75., -43.] 
# ---------------------------------------------------------------
# Normas.

def normaInfinito(x):

    maximo = 0.0
    
    n = len(x)

    for i in range(n):

        if math.fabs(x[i]) > maximo: maximo = math.fabs[i]

    return maximo

def norma1(x):

    sumatoria = 0.0
    
    n = len(x)

    for j in range(n):
        sumatoria += math.fabs(x[j])
    
    return sumatoria

def norma2Euclidiana(x):

    sumatoria = 0.0
    
    n = len(x)

    for j in range(n):
        sumatoria += math.pow(math.fabs(x[j]), 2)
    
    return math.sqrt(sumatoria)

def disp(x, y):

    mayor = 0

    for i in range(len(x)):

        if math.fabs(x[i]-y[i]) > mayor: mayor = math.fabs(x[i]-y[i])

    return mayor




def solNumpy(array):
	A = array[:,0:-1]
	B = array[:,-1]
	solution = np.linalg.solve(A, B)
	return solution

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
		option = getOption('La determinante es menor a ' + str(tol) + ' y puede presentar problemas de evaluación ¿Desea continuar? si[s] no[n]',['s','n'])
		if option == 'n': raise Exception('Operación abortada por el usuario')

# ---------------------------------------------------------------

def jacobi(x, A, b):

    newX = []

    n = len(x)

    for i in range(n):
    
        suma = 0
        
        for j in range(n):

            if j != i: suma += A[i][j] * x[j]

        newX.append( (b[i] - suma) / A[i][i] )

    return newX

def seidel(x, A, b):

    newX = []

    n = len(x)

    for i in range(n): newX.append(x[i])

    for i in range(n):
    
        suma = 0
        
        for j in range(n):

            if j != i: suma += A[i][j] * newX[j]

        newX[i] = ( (b[i] - suma) / A[i][i] )

    return newX

def insertar(tabla, xInicial, contador, dispersion):

    fila = []

    fila.append(contador)

    for i in xInicial: fila.append(i)

    fila.append(dispersion)

    tabla.append(fila)


def iterativo(previus, tolerancia, maximoIteraciones, A, b, metodo):

    tabla = []

    contador = 0

    dispersion = tolerancia + 1

    insertar(tabla, previus, contador, 0)

    while contador < maximoIteraciones and dispersion > tolerancia :

        if metodo == "Jacobi": current = jacobi(previus, A, b)
        elif metodo == "Seidel": current = seidel(previus, A, b)

        #dispersion = normaInfinito(current) - normaInfinito(previus)
        dispersion = disp(current, previus)

        previus = current 

        contador += 1
    
        insertar(tabla, previus, contador, dispersion)

    if dispersion < tolerancia:

        mensaje = [str(current) + " Es una aprox con tolerancia: "+str(tolerancia), True]

    else:

        mensaje = ["Fracaso en " + str(maximoIteraciones) + " iteraciones", False]

    return [tabla, mensaje]

def SORMatricial(matriz, vector, x0, tol, nMax, w):
	dimension = checkSquare(matriz)
	checkDet(matriz)
	array = np.zeros((dimension,dimension + 1))
	array[:,:-1] = matriz
	array[:,-1:] = vector
	#print(tabulate(array))

	numpySol = solNumpy(array)

	D = np.triu(np.tril(matriz))

	L = -np.tril(matriz,-1)
	U = -np.triu(matriz,+1)
	Tw = np.dot(np.linalg.inv(D - w*L),((1-w)*D + w*U))
	print('---Tw---')
	#print(tabulate(Tw, floatfmt='.8f'))
	radioS = np.amax(abs(np.linalg.eigvals(Tw)))
	print('Radio espectral: ' + str(radioS))

	Cw = w * np.dot((np.linalg.inv(D - w*L)),vector)
	print('---Cw---')
	#print(tabulate(Cw, floatfmt='.8f'))

	tabla = []
	fila = []
	table = [[0,x0]]

	for n in range(1,nMax):
		table.append([n])

		table[n].append(np.dot(Tw,table[n-1][1])+Cw)
		errorAbs = abs(np.linalg.norm(table[n][1])-np.linalg.norm(table[n-1][1]))
		table[n].append("{:.1e}".format(errorAbs))
		if errorAbs < tol: break
	#print(tabulate(table, headers=['i','b','E'], floatfmt=['i','.8f','.1E']))

	mensaje = ['La solución al sistema es: ' + str(numpySol) + " con tolerancia: "+str(tol), True]
	print(mensaje) 
	
	return [table , mensaje]
