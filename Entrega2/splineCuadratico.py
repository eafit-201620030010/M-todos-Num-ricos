import numpy as np

#Este metodo recive 2 listas, los X y los Y de los puntos
#Retornara una lista con los Xs resultantes de la matriz generada y una lista de strings con las ecuaciones resultantes
def spline_cuadratico(X,Y):

    k = 0
    ecu1 = []
    ecu1y = []

    for i in range(2,len(X)):
        ecu11 = []
        a = (X[i-1])**2
        b = (X[i-1])
        c = 1
        d = Y[i-1]
        p = (3* (len(X)-1))-3

        for i in range(p):
            ecu11.append(0)
        if a == ((X[1])**2):
            a = 0
        
        ecu11.insert(k,c)
        ecu11.insert(k,b)
        ecu11.insert(k,a)
        ecu1.append(ecu11)
        ecu1y.append(d)
        k = k+3

    k = 3
    ecu2 = []
    ecu2y = []

    for i in range(2,len(X)):
        ecu22 = []
        a = (X[i-1])**2
        b = (X[i-1])
        c = 1
        d = Y[i-1]
        p = (3* (len(X)-1))-3
        for i in range(p):
            ecu22.append(0)
        ecu22.insert(k,c)
        ecu22.insert(k,b)
        ecu22.insert(k,a)
        ecu2.append(ecu22)
        ecu2y.append(d)
        k = k+3

    ecu3 = [0,X[0],1]
    p = (3* (len(X)-1)) - 3
    for i in range(p):
        ecu3.append(0)
    ecu3y=Y[0]

    a = (X[len(X)-1])**2
    ecu4 = [a, X[len(X)-1],1]
    p = (3*(len(X)-1)) -3
    for i in range(p):
        ecu4.insert(0,0)
    ecu4y = Y[len(X)-1]
    
    w = 3
    u = 0
    ecu5 = []
    ecu5y = []
    for i in range(2, len(X)):
        ecu55 = []
        p = (3* (len(X)-1)) -4
        for k in range(p):
            ecu55.append(0)
        a =( X[i-1]*2 )
        b = 1
        ecu55.insert(u,b)
        if a == (X[1])*2:
            a1 = 0
            ecu55.insert(u,a1)
        else:
            ecu55.insert(u,a)
        ecu55.insert(w,-b)
        ecu55.insert(w,-a)
        ecu5.append(ecu55)
        u = u+3
        w = w+3
        ecu5y.append(0)

    ecu6 = [1]
    p=(3*(len(X)-1))-1 
    for k in range(p):
        ecu6.append(0)
    ecu6y = 0

    matriz = []
    matrizy = []

    for i in range(len(ecu1)):
        matriz.append(ecu1[i])
        matrizy.append(ecu1y[i])
        matriz.append(ecu2[i])
        matrizy.append(ecu2y[i])
    
    matriz.append(ecu3)
    matrizy.append(ecu3y)

    matriz.append(ecu4)
    matrizy.append(ecu4y)

    for i in range(len(ecu5)):
        matriz.append(ecu5[i])
        matrizy.append(ecu5y[i])

    matriz.append(ecu6)
    matrizy.append(ecu6y)

    # imprimir la matriz resultante del sistema de ecuaciones
    """
    print(matriz)
    print("\nEl vector con los valores de y es:")
    print(matrizy)
    """

    solucion = np.linalg.solve(matriz, matrizy)

    ecuaciones = []
    for x in range(0,len(solucion),3):
        ecuacion = ""
        ecuacion = ecuacion +str(solucion[x])+"(X^2) "

        if solucion[x+1] < 0:
            ecuacion = ecuacion + str(solucion[x+1]) + "X "
        else:
            ecuacion = ecuacion +"+"+str(solucion[x+1]) + "X "

        if solucion[x+2] < 0:
            ecuacion = ecuacion + str(solucion[x+2])
        else:
            ecuacion = ecuacion +"+"+str(solucion[x+2])

        ecuaciones.append(ecuacion)

    return solucion, ecuaciones

#Recive las listas de X de los puntos y la lista de la solucion de Xs de la matriz resultante de las ecuaciones y el valor de X a evaluar
#Retorna el valor de F de X a evaluar
def evaluar_cuadratico(X,X2,X_eval):
    j = 0
    for i in range(len(X)-1):
        a = X[i]
        b = X[i+1]
        if X[i] <= X_eval and X_eval <= X[i+1]:
            G = ( X2[j] ) * ( X_eval**2 ) + ( X2[j+1] ) * X_eval + (X2[j+2])
        j = j+3
    return G

#Recibe un vector de Xs y uno de Ys de los puntos a interpolar, y un valor de X a evaluar
#Retorna el valor de F de X a evaluar y una lista de strings con los polinomios
def mainCuadratico(xs, ys, valor_evaluar):

    X2, ecuaciones = spline_cuadratico(xs,ys)
    evaluacion = evaluar_cuadratico(xs,X2,valor_evaluar)

    for x in range(len(ecuaciones)):
        ecuaciones[x] = ecuaciones[x] +"    "+str(xs[x]) + " <= X <= " + str(xs[x+1])
        
        #imprimir ecuaciones
        print(ecuaciones[x])

    #imprimir el valor de F de X a evaluar
    print("> Al evaluar",valor_evaluar, "se obtiene:", evaluacion)

    return evaluacion, ecuaciones

if __name__ == "__main__":
    x = [-1,0,3,4]
    y = [15.5,3,8,1]
    valor = 1

    evaluacion, ecuaciones = mainCuadratico(x,y,valor)