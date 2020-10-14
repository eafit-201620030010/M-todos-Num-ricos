import math
from py_expression_eval import Parser

parser = Parser()

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
    
    tabla.append([contadorIteraciones, x, fx, fdx, fddx, 0])

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

        tabla.append([contadorIteraciones, x, fx, fdx, fddx, error])
    
    if fx == 0: 
        
        mensaje = [str(x) + " es una raiz.", True]     
    
    elif error <= tolerancia: 
        
        mensaje = [str(x) + " es una aproximacion a una raiz con tolerancia=" + str(tolerancia), True]     
    
    elif fdx == 0: 
        
        mensaje = ["Hay una posible raiz multiple", True]     
    
    else: 
        
        mensaje = ["Fracaso en " + str(maximoIteraciones) + " iteraciones.", False]

    return [tabla, mensaje]

def main():
    hx = "exp(x)-x-1"
    dhx = "exp(x)-1"
    ddhx = "exp(x)"
    TOL = 0.0000001
    N = 100
    x0 = 1
    resultado = raicesMultiples(1, TOL, N, hx, dhx, ddhx)
    print(resultado)

if __name__ == "__main__":
    main()
