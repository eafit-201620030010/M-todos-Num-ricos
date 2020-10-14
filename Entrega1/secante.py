import math 
from py_expression_eval import Parser

parser = Parser()

def secante(x, xNuevo, tolerancia, maximoIteraciones, f):

    tabla = [] #

    #fx = f(x)
    fx = parser.parse(f).evaluate({"x": x})

    if fx == 0:

        mensaje = [str(x) + " es una raiz.", True]     

    else:

        #fxNuevo = f(xNuevo)
        fxNuevo = parser.parse(f).evaluate({"x": xNuevo})

        contadorIteraciones = 0
        error = tolerancia + 1

        denominador = fxNuevo - fx

        tabla.append([contadorIteraciones, x, fx, 0])
        tabla.append([contadorIteraciones + 1, xNuevo, fxNuevo, 0])

        while error > tolerancia and fxNuevo != 0 and denominador != 0 and contadorIteraciones < maximoIteraciones:

            xAuxiliar = xNuevo - fxNuevo * (xNuevo - x) / denominador

            error = abs(xAuxiliar - xNuevo)

            x = xNuevo
            fx = fxNuevo

            xNuevo = xAuxiliar
            #fxNuevo = f(xNuevo)
            fxNuevo = parser.parse(f).evaluate({"x": xNuevo})

            denominador = fxNuevo - fx

            contadorIteraciones += 1

            tabla.append([contadorIteraciones + 1, xNuevo, fxNuevo, error])

        if fxNuevo == 0: 

            mensaje = [str(xNuevo) + " es una raiz.", True]     

        elif error < tolerancia: 

            mensaje = [str(xNuevo) + " es una aproximacion a una raiz con tolerancia=" + str(tolerancia), True]     

        elif denominador == 0: 

            mensaje = ["Hay una posible raiz multiple", True]     

        else: 

            mensaje = ["Fracaso en " + str(maximoIteraciones) + " iteraciones.", False]

    return [tabla, mensaje]

def main():
    a = secante(0.5,1,0.0000001,100,"log(sin(x)**2 + 1) - 1/2")
    print('\n')
    print(a)

if __name__ == "__main__":
    main()

