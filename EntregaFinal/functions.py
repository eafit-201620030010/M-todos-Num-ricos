def iniciarCholesky(n, numero):

    L = []
    U = []

    for i in range(n):

        rowL = []
        rowU = []

        for j in range(n):

            if i == j: 
                rowL.append(numero)
                rowU.append(numero)
            elif i < j:
                rowL.append(0)
                rowU.append(numero+1)
            else:
                rowL.append(numero-1)
                rowU.append(0)

        L.append(rowL)
        U.append(rowU)

    return [L, U]

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

def imprimirMatriz(Matriz): 
    for fila in Matriz: print(fila)

def intercambiarFilas(M, indexA, indexB):

    aux = M[indexA]
    M[indexA] = M[indexB]
    M[indexB] = aux

def intercambiarColumnas(M, indexA, indexB, marcas):

    auxMarcas = marcas[indexA]
    marcas[indexA] = marcas[indexB]
    marcas[indexB] = auxMarcas

    for i in range(len(M)):

        aux = M[i][indexA]
        M[i][indexA] = M[i][indexB]
        M[i][indexB] = aux

