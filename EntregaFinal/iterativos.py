import math
import numpy

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
