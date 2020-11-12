def calcularB(x, y):

    diferenciasGradoAnterior = y # Diferencias divididas de orden 0.

    b = []
    b.append(diferenciasGradoAnterior[0])

    # En este ciclo se buscan los bi.
    for orden in range(1, len(x)):

        diferencias = []

        i = 0
        j = i + orden

        for diferencia in range(len(diferenciasGradoAnterior) - 1):
       
            numerador = diferenciasGradoAnterior[i] - diferenciasGradoAnterior[i + 1]
            denominador = x[i] - x[j]

            diferencias.append(numerador/denominador)

            i += 1
            j += 1

        b.append(diferencias[0])

        diferenciasGradoAnterior = diferencias

    return b

def p(xEval, b, x):

    sumatoria = 0

    for i in range(len(b)):

        productorio = 1

        for j in range(i): productorio *= xEval - x[j]

        sumatoria += b[i] * productorio

    return sumatoria

if __name__==("__main__"):
    x = [-1,0,3,4]
    y = [15.5,3,8,1]

    resultado = calcularB(x,y)
    print(resultado)
