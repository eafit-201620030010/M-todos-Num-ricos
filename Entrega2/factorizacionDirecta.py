import math


def matrizIdentidad(n):

	M = []

	for i in range(n):

		row = []

		for j in range(n):

			if i == j: row.append(1)
			else: row.append(0)

		M.append(row)

	return M

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

def imprimirMatriz(Matriz): 
    for fila in Matriz: print(fila)

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

def imprimirResultados(etapas, x):
	contEtapa = 0
	for etapa in etapas:
		print("Resumen de la etapa " + str(contEtapa) + ": ")
		L = etapa[0]
		U = etapa[1]
		print("L: ")
		for element in L:
			print(element)
		print("U: ")
		for element in U:
			print(element)
		
		contEtapa+=1
			
	#print(etapas)
	print("Resultado: ")
	print(x)

if __name__ == "__main__":
	A = [[4.0,-1.0,0.0,3.0], [1.0,15.5,3.0,8.0], [0.0,-1.3,-4.0,1.1], [14.0,5.0,-2.0,30.0]]
	b = [1,1,1,1]
	n = len(A)
	etapas, x, z, Lb, Uz = factorizacionDirecta(A,n,b,"Crout")
	print("**************************************************************************************************")
	print("Resultados Crout: ")
	imprimirResultados(etapas, x)
	

	etapas, x, z, Lb, Uz = factorizacionDirecta(A,n,b,"Doolittle")
	print("**************************************************************************************************")
	print("Resultados Doolittle: ")
	imprimirResultados(etapas, x)

	etapas, x, z, Lb, Uz = factorizacionDirecta(A,n,b,"Cholesky")
	print("**************************************************************************************************")
	print("Resultados Cholesky: ")
	imprimirResultados(etapas, x)
	
	
