import numpy as np
from tabulate import tabulate
from sympy import *
import matplotlib.pyplot as plt

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
		option = getOption('La determinante es menor a ' + str(tol) 
			+ ' y puede presentar problemas de evaluación ¿Desea continuar? si[s] no[n]',['s','n'])
		if option == 'n': raise Exception('Operación abortada por el usuario')


def gauss_seidelMatricial(matriz, vector, x0, tol, nMax):
	dimension = checkSquare(matriz)
	checkDet(matriz)
	array = np.zeros((dimension,dimension + 1))
	array[:,:-1] = matriz
	array[:,-1:] = vector
	print(tabulate(array))

	numpySol = solNumpy(array)

	D = np.triu(np.tril(matriz))

	L = -np.tril(matriz,-1)
	U = -np.triu(matriz,+1)
	Tj = np.dot(np.linalg.inv(D-L),U)
	print('---Tj---')
	print(tabulate(Tj, floatfmt='.8f'))
	radioS = np.amax(abs(np.linalg.eigvals(Tj)))
	print('Radio espectral: ' + str(radioS))

	Cg = np.dot(np.linalg.inv(D-L),vector)
	print('---Cg---')
	print(tabulate(Cg, floatfmt='.8f'))
	

	table = [[0,x0]]

	for n in range(1,nMax):
		table.append([n])
		table[n].append(np.dot(Tj,table[n-1][1])+Cg)
		errorAbs = abs(np.linalg.norm(table[n][1])-np.linalg.norm(table[n-1][1]))
		table[n].append(errorAbs)
		if errorAbs < tol: break
	print(tabulate(table, headers=['i','b','E'], floatfmt=['i','.8f','.1E']))

	print('La solución es: ' + str(numpySol))

def SORMatricial(matriz, vector, x0, tol, nMax, w):
	dimension = checkSquare(matriz)
	checkDet(matriz)
	array = np.zeros((dimension,dimension + 1))
	array[:,:-1] = matriz
	array[:,-1:] = vector
	print(tabulate(array))

	numpySol = solNumpy(array)

	D = np.triu(np.tril(matriz))

	L = -np.tril(matriz,-1)
	U = -np.triu(matriz,+1)
	Tw = np.dot(np.linalg.inv(D - w*L),((1-w)*D + w*U))
	print('---Tw---')
	print(tabulate(Tw, floatfmt='.8f'))
	radioS = np.amax(abs(np.linalg.eigvals(Tw)))
	print('Radio espectral: ' + str(radioS))

	Cw = w * np.dot((np.linalg.inv(D - w*L)),vector)
	print('---Cw---')
	print(tabulate(Cw, floatfmt='.8f'))

	table = [[0,x0]]

	for n in range(1,nMax):
		table.append([n])

		table[n].append(np.dot(Tw,table[n-1][1])+Cw)
		errorAbs = abs(np.linalg.norm(table[n][1])-np.linalg.norm(table[n-1][1]))
		table[n].append(errorAbs)
		if errorAbs < tol: break
	print(tabulate(table, headers=['i','b','E'], floatfmt=['i','.8f','.1E']))

	print('La solución es: ' + str(numpySol))

A = np.array([[4,-1,0,3],[1,15.5,3,8],[0,-1.3,-4,1.1], [14,5,-2,30]],dtype=np.float64)
x = np.array([[1],[1],[1],[1]],dtype=np.float64)

x0 = np.array([[0],[0],[0],[0]],dtype=np.float64)
tol = 1e-7
nMax = 100
w = 1.5
print("************************************************************************************************\n")
print("Metodo Gauss-Seidel\n")
gauss_seidelMatricial(A,x,x0,tol,nMax)
print("\n")
print("************************************************************************************************\n")
print("Metodo SOR (Gauss-Seidel relajado)\n")
SORMatricial(A,x,x0,tol,nMax,1.5)
print("\n")

