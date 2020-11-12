import numpy as np
from math import sqrt
from tabulate import tabulate

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

	cont = 0
	print('---Etapa 0, matriz original---')
	print(tabulate(matriz,floatfmt='.6f'))

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
		print('L')
		print(tabulate(L,floatfmt='.6f'))
		print('U')
		print(tabulate(U,floatfmt='.6f'))
	return L,U

def LUGaussVector(matriz, vector):
	dimension = len(matriz)
	array = np.zeros((dimension,dimension + 1))
	array[:,:-1] = matriz
	array[:,-1:] = vector
	numpySol = solNumpy(array)

	L, U = LUGauss(matriz)
	Larr = np.zeros((dimension,dimension + 1))
	Larr[:,:-1] = L
	Larr[:,-1:] = vector
	print('Dado el sistema Lz = b')
	print(tabulate(Larr,floatfmt='.6f'))
	print('Aplicamos sustitución progresiva y obtenemos')
	pSus = progSustitution(Larr)
	print(pSus)
	Uarr = np.zeros((dimension,dimension + 1))
	Uarr[:,:-1] = U
	Uarr[:,-1] = pSus
	print('Dado el sistema Ux = z')
	print(tabulate(Uarr,floatfmt='.6f'))
	print('Aplicamos sustitución regresiva y obtenemos')
	print(sustitution(Uarr))
	print('---Opcional---')
	print('La solución de  es: ' + str(numpySol))


def LUGaussPivoteoParcial(matriz):
	dimension = checkSquare(matriz)
	checkDet(matriz)

	cont = 0
	print('---Etapa 0, matriz original---')
	print(tabulate(matriz,floatfmt='.6f'))

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
		print('P')
		print(tabulate(P,floatfmt='.6f'))
		print('A')
		print(tabulate(A,floatfmt='.6f'))
	print('---Última etapa---')	
	U = np.array(A, copy=True)
	print('U = A =')
	print(tabulate(U,floatfmt='.6f'))
	print('Se construye la matriz L con los multiplicadores almacenados')
	np.fill_diagonal(L, 1)
	print('L')
	print(tabulate(L,floatfmt='.6f'))
	print('P')
	print(tabulate(P,floatfmt='.6f'))
	return L,U,P

def LUGaussPivoteoParcialVector(matriz, vector):
	dimension = len(matriz)
	array = np.zeros((dimension,dimension + 1))
	array[:,:-1] = matriz
	array[:,-1:] = vector
	numpySol = solNumpy(array)

	L, U, P = LUGaussPivoteoParcial(matriz)
	Bn = np.matmul(P,vector)
	print('Calculamos el producto Pb = Bn')
	print(tabulate(Bn,floatfmt='.6f'))
	Larr = np.zeros((dimension,dimension + 1))
	Larr[:,:-1] = L
	Larr[:,-1:] = Bn
	print('Dado el sistema Lz = Bn')
	print(tabulate(Larr,floatfmt='.6f'))
	print('Aplicamos sustitución progresiva y obtenemos')
	pSus = progSustitution(Larr)
	print(pSus)
	Uarr = np.zeros((dimension,dimension + 1))
	Uarr[:,:-1] = U
	Uarr[:,-1] = pSus
	print('Dado el sistema Ux = z')
	print(tabulate(Uarr,floatfmt='.6f'))
	print('Aplicamos sustitución regresiva y obtenemos')
	print(sustitution(Uarr))
	print('---Opcional---')
	print('La solución de  es: ' + str(numpySol))


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

A = np.array([[4,-1,0,3],[1,15.5,3,8],[0,-1.3,-4,1.1], [14,5,-2,30]],dtype=np.float64)
x = np.array([[1],[1],[1],[1]],dtype=np.float64)


try:

	print("Factorizacion LU con gauss simple: ")
	LUGaussVector(A,x) # LU con gauss simple si dan matriz y vector

	print("Factorizacion LU con pivoteo parcial: ")
	LUGaussPivoteoParcialVector(A,x) # LU con pivoteo parcial si dan matriz y vector

except Exception as msg:
	print(msg)




