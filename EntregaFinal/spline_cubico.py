import numpy as np

#Este metodo recive 2 listas, los X y los Y de los puntos
#Retornara una lista con los Xs resultantes de la matriz generada y una lista de strings con las ecuaciones resultantes
def spline_cubico(X,Y):

    k = 0
    ecu1 = []
    ecu1y = []
    for i in range(2,len(X)):
        ecu11 = []
        a = (X[i-1])**3
        b = (X[i-1])**2
        c = (X[i-1])
        d = 1
        e = Y[i-1]
        p = (4* (len(X)-1))-4
        for i in range(p):
            ecu11.append(0)
        ecu11.insert(k,d)
        ecu11.insert(k,c)
        ecu11.insert(k,b)
        ecu11.insert(k,a)
        ecu1.append(ecu11)
        ecu1y.append(e)
        k = k+4

    k = 4
    ecu2 = []
    ecu2y = []
    for i in range(2,len(X)):
        ecu22 = []
        a = (X[i-1])**3
        b = (X[i-1])**2
        c = (X[i-1])
        d = 1
        e = Y[i-1]
        p = (4* (len(X)-1))-4
        for i in range(p):
            ecu22.append(0)
        ecu22.insert(k,d)
        ecu22.insert(k,c)
        ecu22.insert(k,b)
        ecu22.insert(k,a)
        ecu2.append(ecu22)
        ecu2y.append(e)
        k = k+4

    ecu3 = [ X[0]**3, X[0]**2, X[0], 1 ]
    p = (4* (len(X)-1)) - len(ecu3)
    for i in range(p):
        ecu3.append(0)
    ecu3y=Y[0]

    a = X[len(X)-1]**3
    b = X[len(X)-1]**2
    c = X[len(X)-1]
    ecu4=[a,b,c,1]
    p = (4*(len(X)-1)) - len(ecu4)
    for i in range(p):
        ecu4.insert(0,0)
    ecu4y = Y[len(X)-1]

    w = 4
    u = 0
    ecu5 = []
    ecu5y = []
    for i in range(2, len(X)):
        ecu55 = []
        p = (4* (len(X)-1)) -6
        for k in range(p):
            ecu55.append(0)
        a =( X[i-1]**2 )*3
        b = X[i-1]*2
        c = 1
        ecu55.insert(u,c)
        ecu55.insert(u,b)
        ecu55.insert(u,a)
        ecu55.insert(w,-c)
        ecu55.insert(w,-b)
        ecu55.insert(w,-a)
        ecu5.append(ecu55)

        u = u+4
        w = w+4
        ecu5y.append(0)

    w = 4
    u = 0
    ecu6 = []
    ecu6y = []
    for i in range(2, len(X)):
        ecu66 = []
        a = X[i-1]*6
        b = 2
        p = (4* (len(X)-1)) -4
        for k in range(p):
            ecu66.append(0)
        ecu66.insert(u,b)
        ecu66.insert(u,a)
        ecu66.insert(w,-b)
        ecu66.insert(w,-a)
        ecu6.append(ecu66)
        u = u+4
        w = w+4
        ecu6y.append(0)

    a = 6 * X[0]
    b = 2
    ecu7 = []
    p = ( 4*(len(X)-1) ) -2
    for k in range(p):
        ecu7.append(0)
    ecu7.insert(0,b)
    ecu7.insert(0,a)
    ecu7y = 0

    a = 6*X[len(X)-1]
    b = 2
    w = 4 * (len(X)-2)
    ecu8 = []
    p = (4*(len(X)-1)) -2
    for k in range(p):
        ecu8.append(0)
    ecu8.insert(w,b)
    ecu8.insert(w,a)
    ecu8y = 0

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

    for i in range(len(ecu6)):
        matriz.append(ecu6[i])
        matrizy.append(ecu6y[i])

    matriz.append(ecu7)
    matrizy.append(ecu7y)

    matriz.append(ecu8)
    matrizy.append(ecu8y)

    # imprimir la matriz resultante del sistema de ecuaciones
    """
    print(matriz)
    print("\nEl vector con los valores de y es:")
    print(matrizy)
    """

    solucion = np.linalg.solve(matriz, matrizy)

    ecuaciones = []
    for x in range(0,len(solucion),4):
        ecuacion = ""
        ecuacion = ecuacion +str(round(solucion[x],2))+"(X^3) "

        if solucion[x+1] < 0:
            ecuacion = ecuacion + str(round(solucion[x+1],2)) + "(X^2) "
        else:
            ecuacion = ecuacion +"+"+str(round(solucion[x+1],2)) + "(X^2) "

        if solucion[x+2] < 0:
            ecuacion = ecuacion + str(round(solucion[x+2],2)) + "X "
        else:
            ecuacion = ecuacion +"+"+str(round(solucion[x+2],2)) + "X "

        if solucion[x+3] < 0:
            ecuacion = ecuacion + str(round(solucion[x+3],2))
        else:
            ecuacion = ecuacion +"+"+str(round(solucion[x+3],2))

        ecuaciones.append(ecuacion)

    return solucion, ecuaciones

#Recive las listas de X de los puntos y la lista de la solucion de Xs de la matriz resultante de las ecuaciones y el valor de X a evaluar
#Retorna el valor de F de X a evaluar
def evaluar_cubico(X,X2,X_eval):
    j = 0
    for i in range(len(X)-1):
        a = X[i]
        b = X[i+1]
        if X[i] <= X_eval and X_eval <= X[i+1]:
            G = ( X2[j] ) * (X_eval**3) + (X2[j+1]) * (X_eval**2) + (X2[j+2]) * X_eval + (X2[j+3])
        j = j+4
    return round(G, 6)

#Recibe un vector de Xs y uno de Ys de los puntos a interpolar, y un valor de X a evaluar
#Retorna el valor de F de X a evaluar y una lista de strings con los polinomios
def mainCubico(xs, ys, valor_evaluar):

    X2, ecuaciones = spline_cubico(xs,ys)
    evaluacion = evaluar_cubico(xs,X2,valor_evaluar)

    for x in range(len(ecuaciones)):
        ecuaciones[x] = ecuaciones[x] +"    "+str(xs[x]) + " <= X <= " + str(xs[x+1])
        
        #imprimir ecuaciones
        print(ecuaciones[x])

    #imprimir el valor de F de X a evaluar
    print("> Al evaluar",valor_evaluar, "se obtiene:", evaluacion)

    return evaluacion, ecuaciones
