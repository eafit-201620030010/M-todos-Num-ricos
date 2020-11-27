import numpy as np

#Este metodo recive 2 listas, los X y los Y de los puntos
#Retornara una lista con las pendientes de las rectas de 1 punto a otro y una lista de strings con las ecuaciones resultantes
def spline_lineal(X,Y):

    pendientes = []
    ecuaciones = []

    for i in range(len(X)-1):
        m = ( Y[i+1] - Y[i] ) / ( X[i+1] - X[i] )
        m = round(m, 2)
        pendientes.append(m)
        
        corte = (m*(-X[i+1])) + Y[i+1]
        corte = round(corte, 2)
        ecuacion = str(m)+"X "
        if corte < 0 :
            ecuacion = ecuacion + str(corte)
        else:
            ecuacion = ecuacion +"+"+str(corte)

        ecuacion = ecuacion +"    "+str(Y[i]) + " <= X <= " + str(Y[i+1])
        ecuaciones.append( ecuacion )

    return pendientes, ecuaciones

#Recive las listas de X y de Y, el valor de X a evaluar y la lista de las pendientes
#Retorna el valor de F de X a evaluar
def evaluar_recta(X,Y,X_eval,M):
    j = 0
    for i in range(len(X)-1):
        a = X[i]
        b = X[i+1]
        if X[i] <= X_eval and X_eval <= X[i+1]:
            G = ( M[j] ) * ( X_eval-X[j] ) + ( Y[j] )
        j = j+1
    return G

def mainLineal(xs, ys, valor_evaluar):

    M, ecuaciones = spline_lineal(xs,ys)
    evaluacion = evaluar_recta(xs,ys,valor_evaluar,M)

    #imprimir ecuaciones
    for x in ecuaciones:
        print(x)

    #imprimir el valor de F de X a evaluar
    print("> Al evaluar",valor_evaluar, "se obtiene:", str(evaluacion))

    return evaluacion, ecuaciones
