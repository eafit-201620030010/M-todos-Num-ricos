#Algoritmo de busquedas incrementales
import math
from py_expression_eval import Parser
parser = Parser()
#Datos de entrada:
#f (funcion)
#x (x inicial, x0)
#deltax (variacion en x)
#N (Numero maximo de iteraciones)
raices = []

def busquedasIncrementales(f, x, delta, maximoIteraciones):

    tabla = [] #

    #fx = f(x)
    fx = parser.parse(f).evaluate({"x": x})

    tabla.append([x, fx]) #

    if fx == 0:

        mensaje = [str(x) + " es una raiz.", True] #

    else:
        
        xNuevo = x + delta
        #fxNuevo = f(xNuevo)
        fxNuevo = parser.parse(f).evaluate({"x": xNuevo})
       
        tabla.append([xNuevo, fxNuevo]) #
        
        contadorIteraciones = 1

        while fx * fxNuevo > 0 and contadorIteraciones < maximoIteraciones:
 
            x = xNuevo
            fx = fxNuevo

            xNuevo = x + delta
            #fxNuevo = f(xNuevo)
            fxNuevo = parser.parse(f).evaluate({"x": xNuevo})
 
            tabla.append([xNuevo, fxNuevo]) #

            contadorIteraciones += 1

        if fxNuevo == 0: 
            
            mensaje = [str(xNuevo) + " es una raiz.", True] #
        
        elif fx * fxNuevo < 0: 
            
            mensaje = ["Hay una raiz entre " + str(x) + " y " + str(xNuevo), True] #
            raices.append([mensaje[0]])
            busquedasIncrementales(f, xNuevo, delta, (maximoIteraciones-contadorIteraciones))
        
        else: 
            
            mensaje = ["Fracaso en " + str(maximoIteraciones), False] #


    #print(tabla)
    #print(mensaje)
    #return [tabla, mensaje] #


def main():
    x0 = -3
    deltax = 0.5
    N = 100
    f = 'log(sin(x)**2+1) - 1/2'

    #print(busquedasIncrementales(f, x0, deltax, N))
    busquedasIncrementales(f, x0, deltax, N)
    for fila in raices:
        print(fila)
if __name__ == "__main__":
    main()