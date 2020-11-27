import math
from py_expression_eval import Parser

parser = Parser()

raices = []

def busquedasIncrementales(x, delta, maximoIteraciones, f):
    
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

            mensaje = ["Hay una raiz de f en " + str(x) + " y " + str(xNuevo), True] #
            raices.append(mensaje[0])
            busquedasIncrementales(xNuevo, delta, (maximoIteraciones-contadorIteraciones), f)

        else: 

            mensaje = ["Fracaso en " + str(maximoIteraciones), False] #


    #print(tabla)
    #print(raices)
    return [raices, mensaje] #


# ***********************************************************************************************

def biseccion(xInferior, xSuperior, tolerancia, maximoIteraciones, f):

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

        xMedio = (xInferior + xSuperior) / 2
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

            xMedio = (xInferior + xSuperior) / 2
            #fxMedio = f(xMedio)
            fxMedio = parser.parse(f).evaluate({"x": xMedio})

            error = abs(xMedio - auxiliar)
            contadorIteraciones += 1

            tabla.append([contadorIteraciones, xInferior, xSuperior, xMedio, fxMedio, "{:.1e}".format(error)]) #
        
        if fxMedio == 0:

            mensaje = [str(xMedio) + " es una raiz.", True] #

        elif error < tolerancia:

            mensaje = [str(xMedio) + " es una aproximacion a una raiz con una tolerancia = " + str(tolerancia), True] #
        
        else:

            mensaje = ["Fracaso en " + str(maximoIteraciones) + " iteraciones.", False] #
    
    else:

        mensaje = ["El intervalo es inadecuado.", False] #

    return [tabla, mensaje] #
 
# ***********************************************************************************************

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
            
            tabla.append([contadorIteraciones, xInferior, xSuperior, xMedio, fxMedio, "{:.1e}".format(error)]) #

        if fxMedio == 0:

            mensaje = [str(xMedio) + " es una raiz.", True] #
        
        elif error < tolerancia:
            
            mensaje = [str(xMedio) + " es una aproximacion a una raiz con una tolerancia = " + str(tolerancia), True] #
    
        else:

            mensaje = ["Fracaso en " + str(maximoIteraciones), False] #

    else:

        mensaje = ["El intervalo es inadecuado.", False] #
    
    return [tabla, mensaje] #
