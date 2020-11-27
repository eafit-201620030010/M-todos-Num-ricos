import math
from py_expression_eval import Parser

parser = Parser()

# ***********************************************************************************************

def puntoFijo(x, tolerancia, maximoIteraciones, f, g):

    tabla = [] #

    #fx = f(x)
    fx = parser.parse(f).evaluate({"x": x})

    contadorIteraciones = 0
    error = tolerancia + 1

    tabla.append([contadorIteraciones, '{1:>10.10f}'.format(1,x),'{1:>10.10f}'.format(1,fx), 0]) #

    while error > tolerancia and contadorIteraciones < maximoIteraciones and fx != 0:
       
        #xNuevo = g(x)
        xNuevo = parser.parse(g).evaluate({"x": x})
        #fx = f(xNuevo)
        fx = parser.parse(f).evaluate({"x": xNuevo})
 
        error = abs(xNuevo - x)
        
        x = xNuevo

        contadorIteraciones += 1

        tabla.append([contadorIteraciones, '{1:>10.10f}'.format(1,x), '{1:>10.10f}'.format(1,fx), "{:.1e}".format(error)]) #
    
    if fx == 0: 
        
        mensaje = [str(x) + " es una raiz.", True] #
    
    elif error <= tolerancia: 
        
        mensaje = [str(x) + " es una aproximacion con tolerancia " + str(tolerancia), True] #
    
    else: 
        
        mensaje = ["Fracaso en " + str(maximoIteraciones) + " iteraciones.", False] #
    
    return [tabla, mensaje]

# ***********************************************************************************************

def newton(x, tolerancia, maximoIteraciones, f, df):

    tabla = [] #

    #fx = f(x)
    fx = parser.parse(f).evaluate({"x": x})
    #derivada = fd(x)
    derivada = parser.parse(df).evaluate({"x": x})

    contadorIteraciones = 0
    error = tolerancia + 1

    tabla.append([contadorIteraciones, '{1:>10.10f}'.format(1,x), '{1:>10.10f}'.format(1,fx), '{1:>10.10f}'.format(1,derivada), 0]) #
    
    while error > tolerancia and contadorIteraciones < maximoIteraciones and fx != 0 and derivada != 0:
       
        xNuevo = x - (fx / derivada)
        #fx = f(xNuevo)
        fx = parser.parse(f).evaluate({"x": xNuevo})
        #derivada = fd(xNuevo)
        derivada = parser.parse(df).evaluate({"x": xNuevo})

        error = abs(xNuevo - x)
        
        x = xNuevo

        contadorIteraciones += 1
        
        tabla.append([contadorIteraciones, '{1:>10.10f}'.format(1,x), '{1:>10.10f}'.format(1,fx), '{1:>10.10f}'.format(1,derivada), "{:.1e}".format(error)]) #

    if fx == 0: 
        
        mensaje = [str(x) + " es una raiz.", True] #
    
    elif error <= tolerancia: 
        
        mensaje = [str(x) + " es una aproximacion con tolerancia " + str(tolerancia), True] #
    
    elif derivada == 0: 
        
        mensaje = [str(xNuevo) + "es una posible raiz multiple", True] #
    
    else: 
        
        mensaje = ["Fracaso en " + str(maximoIteraciones) + " iteraciones.", False] #
    
    return [tabla, mensaje]

# ***********************************************************************************************

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

        tabla.append([contadorIteraciones, '{1:>10.10f}'.format(1,x), '{1:>10.10f}'.format(1,fx), 0])
        tabla.append([contadorIteraciones + 1, '{1:>10.10f}'.format(1,xNuevo), '{1:>10.10f}'.format(1,fxNuevo), 0])
        
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

            tabla.append([contadorIteraciones + 1, '{1:>10.10f}'.format(1,xNuevo), '{1:>10.10f}'.format(1,fxNuevo), "{:.1e}".format(error)])
        
        if fxNuevo == 0: 
            
            mensaje = [str(xNuevo) + " es una raiz.", True]     
        
        elif error < tolerancia: 
            
            mensaje = [str(xNuevo) + " es una aproximacion a una raiz con tolerancia=" + str(tolerancia), True]     
        
        elif denominador == 0: 
            
            mensaje = ["Hay una posible raiz multiple", True]     
        
        else: 
            
            mensaje = ["Fracaso en " + str(maximoIteraciones) + " iteraciones.", False]

    return [tabla, mensaje]

# ***********************************************************************************************

def raicesMultiples(x, tolerancia, maximoIteraciones, f, df, ddf):
    
    tabla = []

    #fx = f(x)
    fx = parser.parse(f).evaluate({"x": x})
    #fdx = fd(x)
    fdx = parser.parse(df).evaluate({"x": x})
    #fddx = fdd(x)
    fddx = parser.parse(ddf).evaluate({"x": x})

    contadorIteraciones = 0
    error = tolerancia + 1

    tabla.append([contadorIteraciones, '{1:>10.10f}'.format(1,x), '{1:>10.10f}'.format(1,fx), '{1:>10.10f}'.format(1,fdx), '{1:>10.10f}'.format(1,fddx), 0])

    while error > tolerancia and contadorIteraciones < maximoIteraciones and fx != 0 and fdx != 0:

        xNuevo = x - ((fx * fdx) / (math.pow(fdx, 2) - fx * fddx)) #Habia un error, estaba math.pow(fddx, 2) 

        #fx = f(xNuevo)
        fx = parser.parse(f).evaluate({"x": xNuevo})
        #fdx = fd(xNuevo)
        fdx = parser.parse(df).evaluate({"x": xNuevo})
        #fddx = fdd(xNuevo)
        fddx = parser.parse(ddf).evaluate({"x": xNuevo})

        error = abs(xNuevo - x)

        x = xNuevo

        contadorIteraciones += 1

        tabla.append([contadorIteraciones, '{1:>10.10f}'.format(1,x), '{1:>10.10f}'.format(1,fx), '{1:>10.10f}'.format(1,fdx), '{1:>10.10f}'.format(1,fddx), "{:.1e}".format(error)])

    if fx == 0: 

        mensaje = [str(x) + " es una raiz.", True]     

    elif error <= tolerancia: 

        mensaje = [str(x) + " es una aproximacion a una raiz con tolerancia=" + str(tolerancia), True]     

    elif fdx == 0: 

        mensaje = ["Hay una posible raiz multiple", True]     

    else: 

        mensaje = ["Fracaso en " + str(maximoIteraciones) + " iteraciones.", False]

    return [tabla, mensaje]

