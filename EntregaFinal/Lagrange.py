from Puntos import x, y
from sympy import *

def pLagrange(x, y, xEval):

    expresion = ""

    sumatoria = 0

    for k in range(len(x)):  
    
        productorio = 1 
    
        for i in range(len(x)): # El productorio es Lk(x)
        
            if i != k: 
                productorio *= (xEval - x[i]) / (x[k] - x[i]) 
                expresion = expresion + "(x - " + str(x[i]) + ") / (" + str(x[k]) + "-" + str(x[i]) + ") *" 

        sumatoria +=  productorio * y[k] # Lk(x)f(x)

    print expresion

    return sumatoria

pLagrange(3)

print sympy.latex(sympify("(3-1.5) / (1.0-1.5) *(3-2.0) / (1.0-2.0) *(3-2.5) / (1.0-2.5) *(3-3.0) / (1.0-3.0) *(3-1.0) / (1.5-1.0) *(3-2.0) / (1.5-2.0) *(3-2.5) / (1.5-2.5) *(3-3.0) / (1.5-3.0) *(3-1.0) / (2.0-1.0) *(3-1.5) / (2.0-1.5) *(3-2.5) / (2.0-2.5) *(3-3.0) / (2.0-3.0) *(3-1.0) / (2.5-1.0) *(3-1.5) / (2.5-1.5) *(3-2.0) / (2.5-2.0) *(3-3.0) / (2.5-3.0) *(3-1.0) / (3.0-1.0) *(3-1.5) / (3.0-1.5) *(3-2.0) / (3.0-2.0) *(3-2.5) / (3.0-2.5)"))
