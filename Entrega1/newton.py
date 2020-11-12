import math 
from py_expression_eval import Parser

parser = Parser()

def newton(x, tolerancia, maximoIteraciones, f, df):

    tabla = [] #

    #fx = f(x)
    fx = parser.parse(f).evaluate({"x": x})
    #derivada = fd(x)
    derivada = parser.parse(df).evaluate({"x": x})

    contadorIteraciones = 0
    error = tolerancia + 1

    tabla.append([contadorIteraciones, x, fx, derivada, 0]) #

    while error > tolerancia and contadorIteraciones < maximoIteraciones and fx != 0 and derivada != 0:

        xNuevo = x - (fx / derivada)
        #fx = f(xNuevo)
        fx = parser.parse(f).evaluate({"x": xNuevo})
        #derivada = fd(xNuevo)
        derivada = parser.parse(df).evaluate({"x": xNuevo})

        error = abs(xNuevo - x)

        x = xNuevo

        contadorIteraciones += 1

        tabla.append([contadorIteraciones, x, fx, derivada, error]) #

    if fx == 0: 

        mensaje = [str(x) + " es una raiz.", True] #

    elif error <= tolerancia: 

        mensaje = [str(x) + " es una aproximacion con tolerancia " + str(tolerancia), True] #

    elif derivada == 0: 

        mensaje = [str(xNuevo) + "es una posible raiz multiple", True] #

    else: 

        mensaje = ["Fracaso en " + str(maximoIteraciones) + " iteraciones.", False] #

    return [tabla, mensaje]

def main():
    #a = newton(0.5,0.0000001,100,"log(sin(x)**2 + 1) - 1/2","(2*sin(x)*cos(x))/(sin(x)**2 + 1)")
    a = newton(0.55, 0.00001, 100, "(0.44*(x**2))-(0.44*x)+0.11", "0.88*x-0.44")
    print('\n')
    #print(a)
    for row in a[0]:
        print(row)
    print(a[1])

if __name__ == "__main__":
    main()

