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


def gaussianaSimple(AbParam, n, printEtapas):

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

    if printEtapas == True:
        for i in range (len(etapas)):
            print("Etapa",i,":")
            imprimirMatriz(etapas[i])
            print(" ")
    
    #print("Etapa ", len(etapas), ": ")
    #imprimirMatriz(etapas[-1]) #etapas[-1] es lo mismo que decir etapas en la ultima posicion   

    #Sustitucion regresiva:
    x = sustitucionRegresiva(Ab)
    #imprimirMatriz(x)
    return[x]
    
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
    print("Despues de aplicar sustitucion Gaussiana simple: ")
    resultado = gaussianaSimple(Ab, len(Ab), imprimirEtapas)
    print("resultados x: ")
    imprimirMatriz(resultado)




if __name__ == "__main__":
    main()
