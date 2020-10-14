import math 
from py_expression_eval import Parser

parser = Parser()


def puntoFijo(x, tolerancia, maximoIteraciones, f, g):

    tabla = [] #

    #fx = f(x)
    fx = parser.parse(f).evaluate({"x": x})

    contadorIteraciones = 0
    error = tolerancia + 1

    tabla.append([contadorIteraciones, x,fx, 0]) #

    while error > tolerancia and contadorIteraciones < maximoIteraciones and fx != 0:

        #xNuevo = g(x)
        xNuevo = parser.parse(g).evaluate({"x": x})
        #fx = f(xNuevo)
        fx = parser.parse(f).evaluate({"x": xNuevo})

        error = abs(xNuevo - x)

        x = xNuevo

        contadorIteraciones += 1

        tabla.append([contadorIteraciones, x, fx, error]) #

    if fx == 0: 

        mensaje = [str(x) + " es una raiz.", True] #

    elif error <= tolerancia: 

        mensaje = [str(x) + " es una aproximacion con tolerancia " + str(tolerancia), True] #

    else: 

        mensaje = ["Fracaso en " + str(maximoIteraciones) + " iteraciones.", False] #

    return [tabla, mensaje]


def main():
    a = puntoFijo(-0.5,0.0000001,100,"log(sin(x)**2 + 1) - 1/2","log(sin(x)**2 + 1) - 1/2")
    print('\n')
    print(a)

if __name__ == "__main__":
    main()
