import math
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

def pivoteoParcial(Ab, k, n):

    mayor = math.fabs(Ab[k][k])
    filaMayor = k

    for i in range(k + 1, n):

        if math.fabs(Ab[i][k]) > mayor:

            mayor = Ab[i][k]
            filaMayor = i

    if mayor == 0:

        print("El sistema no tiene solución única.")

    elif filaMayor != k:

        intercambiarFilas(Ab, k, filaMayor)

    return filaMayor

def sustitucionRegresiva(Ab):

    x = []

    for pivotIndex in range((len(Ab) - 1), -1, -1):

        summation = i =  0

        for column in range((len(Ab[0]) - 2), pivotIndex, -1):

            summation +=  Ab[pivotIndex][column] * x[i]

            i += 1

        x.append( ( Ab[pivotIndex][len(Ab[0]) - 1] - summation ) / Ab[pivotIndex][pivotIndex] )

    return x[::-1]

def gaussianaPivoteoParcial(AbParam, n, imprimirEtapas):

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
    if imprimirEtapas == True:
        for i in range (len(etapas)):
            print("Etapa",i,":")
            imprimirMatriz(etapas[i])
            print(" ")
    #Sustitucion regresiva
    x = sustitucionRegresiva(Ab)
    return [etapas, x, filaMayorList, etapasPrevias]

def main():
    A = [
        [2, -1, 0, 3],
        [1, 0.5, 3, 8],
        [0, 13, -2, 11],
        [14, 5, -2, 3]
    ]
    b = [1, 1, 1, 1]
    Ab = matrizAumentada(A, b)
    
    print("Matriz A: ")
    imprimirMatriz(A)
    print("Vector b: ")
    imprimirMatriz(b)
    print("Matriz Ab: ")
    imprimirMatriz(Ab)
    imprimirEtapas = True
    print("Despues de aplicar sustitucion Gaussiana con pivoteo parcial: ")
    resultado = gaussianaPivoteoParcial(Ab, len(Ab), imprimirEtapas)
    x = resultado[1]
    imprimirMatriz(x)


if __name__ == "__main__":
    main()
