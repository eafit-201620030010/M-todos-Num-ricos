import math

def jacobi(x, A, b):

    newX = []

    n = len(x)

    for i in range(n):
    
        suma = 0
        
        for j in range(n):

            if j != i: suma += A[i][j] * x[j]

        newX.append( (b[i] - suma) / A[i][i] )

    return newX

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

def insertar(tabla, xInicial, contador, dispersion):

    fila = []

    fila.append(contador)

    for i in xInicial: fila.append(i)

    fila.append(dispersion)

    tabla.append(fila)

def iterativo(previus, tolerancia, maximoIteraciones, A, b):

    tabla = []

    contador = 0

    dispersion = tolerancia + 1

    insertar(tabla, previus, contador, 0)

    while contador < maximoIteraciones and dispersion > tolerancia :

        current = jacobi(previus, A, b)
        #elif metodo == "Seidel": current = seidel(previus, A, b)

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

if __name__ == "__main__":
    A = [[4.0,-1.0,0.0,3.0], [1.0,15.5,3.0,8.0], [0.0,-1.3,-4.0,1.1], [14.0,5.0,-2.0,30.0]]
    b = [1,1,1,1]
    x0 = [0,0,0,0]
    tol = 1e-7
    nMax = 100
    resultado = iterativo(x0, tol,nMax, A, b)
    tabla = resultado[0]
    mensaje = resultado[1]
    for row in tabla:
        print(row)
    print("Solucion: " + mensaje[0])
