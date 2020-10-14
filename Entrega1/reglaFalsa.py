import math
from py_expression_eval import Parser

parser = Parser()

def reglaFalsa(xInferior, xSuperior, tolerancia, maximoIteraciones, f):

    tabla = [] #

    #fxInferior = f(xInferior)
    fxInferior = parser.parse(f).evaluate({"x": xInferior})
    #fxSuperior = f(xSuperior)
    fxSuperior = parser.parse(f).evaluate({"x": xSuperior})

    if fxInferior == 0:

        mensaje = [str(xInferior) + " es una raiz.", True] #

    elif fxSuperior == 0:

        mensaje = [str(xSuperior) + " es una raiz.", True] #

    elif fxInferior * fxSuperior < 0:

        contadorIteraciones = 1

        xMedio = xInferior - ((fxInferior * (xSuperior - xInferior)) / (fxSuperior - fxInferior))
        #fxMedio = f(xMedio)
        fxMedio = parser.parse(f).evaluate({"x": xMedio})

        tabla.append([contadorIteraciones, xInferior, xSuperior, xMedio, fxMedio, 0]) #

        error = tolerancia + 1

        while error > tolerancia and fxMedio != 0 and contadorIteraciones < maximoIteraciones:

            if fxInferior * fxMedio < 0:

                xSuperior = xMedio
                fxSuperior = fxMedio

            else:

                xInferior = xMedio
                fxInferior = fxMedio

            auxiliar = xMedio

            xMedio = xInferior - ((fxInferior * (xSuperior - xInferior)) / (fxSuperior - fxInferior))
            #fxMedio = f(xMedio)
            fxMedio = parser.parse(f).evaluate({"x": xMedio})

            error = abs(xMedio - auxiliar)

            contadorIteraciones += 1

            tabla.append([contadorIteraciones, xInferior, xSuperior, xMedio, fxMedio, error]) #

        if fxMedio == 0:

            mensaje = [str(xMedio) + " es una raiz.", True] #

        elif error < tolerancia:

            mensaje = [str(xMedio) + " es una aproximacion a una raiz con una tolerancia = " + str(tolerancia), True] #

        else:

            mensaje = ["Fracaso en " + str(maximoIteraciones), False] #

    else:

        mensaje = ["El intervalo es inadecuado.", False] #

    return [tabla, mensaje] #


def main():
    a = reglaFalsa(0,1,0.0000001,100,"log(sin(x)**2 + 1) - 1/2")
    print('\n')
    print(a)

if __name__ == "__main__":
    main()
