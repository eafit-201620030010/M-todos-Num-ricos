from flask import Flask, render_template, request, session, redirect

from functions import *

#******* Ecuaciones de una varibale ***********
from cerrados import *
from abiertos import *

#******* Sistemas de ecuaciones lineales ***********
from directos import *
from iterativos import *

from interpolacion import *

from spline_lineal import *
from spline_cuadratico import *
from spline_cubico import *

app = Flask(__name__)

app.secret_key = "clave-inicial"

@app.route("/")
def hello_world(): 
	
	session["f"] = ""
	session["g"] = ""
	session["df"] = ""
	session["ddf"] = ""
	
	return render_template("/inicio.html")

@app.route("/ecuacionesDeUnaVariable", methods=["GET"])
def ecuacionesDeUnaVariable(): return render_template("/ecuaciones-de-una-variable.html")

@app.route("/sistemasDeEcuaciones", methods=["GET"])
def sistemasDeEcuaciones(): return render_template("/sistemas-de-ecuaciones-lineales.html")

@app.route("/interpolacion", methods=["GET"])
def interpolacion(): return render_template("/interpolacion.html")

@app.route("/graficar", methods=["GET"])
def graficar():
	
	session["metodo"] = request.args.get("metodo")
	
	return render_template("/graficar.html")

@app.route("/establecerFuncion", methods=["POST", "GET"])
def establecerFunciones():
	
	if request.method == 'POST':

		if request.form["f"] != "": session["f"] = request.form["f"]
		
		if request.form["g"] != "": session["g"] = request.form["g"]
		
		if request.form["df"] != "": session["df"] = request.form["df"]
		
		if request.form["ddf"] != "": session["ddf"] = request.form["ddf"]

		return redirect("/establecerFuncion?metodo="+session["metodo"])        
		
	else:

		session["metodo"] = request.args.get("metodo")
		return render_template("/establecer_funcion.html", f=session["f"], g=session["g"], df=session["df"], ddf=session["ddf"])

# ========================================================================
# Ecuaciones de una variable.
# ========================================================================

@app.route("/busquedasIncrementales", methods=["POST", "GET"])
def busquedasIncrementalesWeb():

	if request.method == 'POST':
	
		xInicial = float(request.form["txtXInicial"])
		delta = float(request.form["txtDelta"])
		maximoIteraciones = int(request.form["txtMaximoIteraciones"])

		resultado = busquedasIncrementales(xInicial, delta, maximoIteraciones, session["f"])

		return render_template("/ecuaciones_variable/busquedas-incrementales.html", tabla=resultado[0], numFilas=len(resultado[0]),
				mensaje=resultado[1][0], tipo=resultado[1][1])

	else:

		if session["f"] != "": permitir = True
		else: permitir = False

		return render_template("/ecuaciones_variable/busquedas-incrementales.html", permitir=permitir)

@app.route("/biseccion", methods=["POST", "GET"])
def biseccionWeb():

	if request.method == 'POST':

		xInferior = float(request.form["txtXInferior"])
		xSuperior = float(request.form["txtXSuperior"])
		tolerancia = float(request.form["txtTolerancia"])
		maximoIteraciones = int(request.form["txtMaximoIteraciones"])

		resultado = biseccion(xInferior, xSuperior, tolerancia, maximoIteraciones, session["f"])
		
		return render_template("/ecuaciones_variable/biseccion.html", tabla=resultado[0], numFilas=len(resultado[0]), mensaje=resultado[1][0], tipo=resultado[1][1])
	
	else:

		return render_template("/ecuaciones_variable/biseccion.html")

@app.route("/reglaFalsa", methods=["POST", "GET"])
def reglaFalsaWeb():

	if request.method == 'POST':
	
		xInferior = float(request.form["txtXInferior"])
		xSuperior = float(request.form["txtXSuperior"])
		tolerancia = float(request.form["txtTolerancia"])
		maximoIteraciones = int(request.form["txtMaximoIteraciones"])
		
		resultado = reglaFalsa(xInferior, xSuperior, tolerancia, maximoIteraciones, session["f"])

		return render_template("/ecuaciones_variable/regla-falsa.html", tabla=resultado[0], numFilas=len(resultado[0]), mensaje=resultado[1][0], tipo=resultado[1][1])

	else:

		return render_template("/ecuaciones_variable/regla-falsa.html")

@app.route("/puntoFijo", methods=["POST", "GET"])
def puntoFijoWeb():

	if request.method == 'POST':
	
		if not("f" in session and "g" in session): return redirect("/puntoFijo")

		xInicial = float(request.form["txtXInicial"])
		tolerancia = float(request.form["txtTolerancia"])
		maximoIteraciones = int(request.form["txtMaximoIteraciones"])

		resultado = puntoFijo(xInicial, tolerancia, maximoIteraciones, session["f"], session["g"])

		return render_template("/ecuaciones_variable/punto-fijo.html", tabla=resultado[0], numFilas=len(resultado[0]), mensaje=resultado[1][0], tipo=resultado[1][1])

	else:

		return render_template("/ecuaciones_variable/punto-fijo.html")

@app.route("/newton", methods=["POST", "GET"])
def newtonWeb():

	if request.method == 'POST':
	
		xInicial = float(request.form["txtXInicial"])       
		tolerancia = float(request.form["txtTolerancia"])
		maximoIteraciones = int(request.form["txtMaximoIteraciones"])

		resultado = newton(xInicial, tolerancia, maximoIteraciones, session["f"], session["df"])
		
		return render_template("/ecuaciones_variable/newton.html", tabla=resultado[0], numFilas=len(resultado[0]), mensaje=resultado[1][0], tipo=resultado[1][1])

	else:

		return render_template("/ecuaciones_variable/newton.html")

@app.route("/secante", methods=["POST", "GET"])
def secanteWeb():
 
	if request.method == 'POST':

		xInferior = float(request.form["txtXInferior"])
		xSuperior = float(request.form["txtXSuperior"]) 
		tolerancia = float(request.form["txtTolerancia"])
		maximoIteraciones = int(request.form["txtMaximoIteraciones"])

		resultado = secante(xInferior, xSuperior, tolerancia, maximoIteraciones, session["f"])

		return render_template("/ecuaciones_variable/secante.html", tabla=resultado[0], numFilas=len(resultado[0]), mensaje=resultado[1][0], tipo=resultado[1][1])

	else:

		return render_template("/ecuaciones_variable/secante.html")


@app.route("/raicesMultiples", methods=["POST", "GET"])
def raicesMultiplesWeb():

	if request.method == 'POST':
	
		xInicial = float(request.form["txtXInicial"])        
		tolerancia = float(request.form["txtTolerancia"])
		maximoIteraciones = int(request.form["txtMaximoIteraciones"])

		resultado = raicesMultiples(xInicial, tolerancia, maximoIteraciones, session["f"], session["df"], session["ddf"])

		return render_template("/ecuaciones_variable/raices-multiples.html", tabla=resultado[0], numFilas=len(resultado[0]),
				mensaje=resultado[1][0], tipo=resultado[1][1])

	else:

		return render_template("/ecuaciones_variable/raices-multiples.html")

# ========================================================================
# Sistemas de ecuaciones lineales.
# ========================================================================

@app.route("/gaussianaSimple", methods=["POST", "GET"])
def gaussianaSimpleWeb():
	
	if request.method == 'POST':
		
		if request.form.get("checkEtapas"): proceso = True
		else: proceso = False
	
		matriz = request.form["txtA"].split("\n")
		b = request.form["txtB"].split(",")

		A = [] # Matriz de coeficientes.

		for fila in matriz: A.append(fila.split(","))
	
		for i in range(len(A)):
			for j in range(len(A[0])): A[i][j] = float(A[i][j])

		for i in range(len(b)): b[i] = float(b[i])

		Ab = matrizAumentada(A, b)    
   
		resultado = gaussianaSimple(Ab, len(A))
		
		return render_template("/sistemas_ecuaciones/gaussiana-simple.html", Ab=Ab, etapas=resultado[0], numEtapas=len(resultado[0])-1, 
		n=len(A), x=resultado[1], proceso=proceso)

	else:

		return render_template("/sistemas_ecuaciones/gaussiana-simple.html")

@app.route("/pivoteoParcial", methods=["POST", "GET"])
def pivoteoParcialWeb():
	
	if request.method == 'POST':
		
		if request.form.get("checkEtapas"): proceso = True
		else: proceso = False
	
		matriz = request.form["txtA"].split("\n")
		b = request.form["txtB"].split(",")

		A = [] # Matriz de coeficientes.

		for fila in matriz: A.append(fila.split(","))
	
		for i in range(len(A)):
			for j in range(len(A[0])): A[i][j] = float(A[i][j])

		for i in range(len(b)): b[i] = float(b[i])

		Ab = matrizAumentada(A, b)    
   
		resultado = gaussianaPivoteoParcial(Ab, len(A))
		
		return render_template("/sistemas_ecuaciones/pivoteo-parcial.html", Ab=Ab, etapas=resultado[0], numEtapas=len(resultado[0]),
				n=len(A), x=resultado[1], filaMayorList=resultado[2], etapasPrevias=resultado[3], proceso=proceso)

	else:

		return render_template("/sistemas_ecuaciones/pivoteo-parcial.html")

@app.route("/pivoteoTotal", methods=["POST", "GET"])
def pivoteoTotalWeb():
	
	if request.method == 'POST':
		
		if request.form.get("checkEtapas"): proceso = True
		else: proceso = False
	
		matriz = request.form["txtA"].split("\n")
		b = request.form["txtB"].split(",")

		A = [] # Matriz de coeficientes.

		for fila in matriz: A.append(fila.split(","))
	
		for i in range(len(A)):
			for j in range(len(A[0])): A[i][j] = float(A[i][j])

		for i in range(len(b)): b[i] = float(b[i])

		Ab = matrizAumentada(A, b)    
   
		resultado = gaussianaPivoteoTotal(Ab, len(A))
		
		return render_template("/sistemas_ecuaciones/pivoteo-total.html", Ab=Ab, etapas=resultado[0], numEtapas=len(resultado[0]),
				n=len(A), x=resultado[1], mayorList=resultado[2], etapasPrevias=resultado[3], marcas=resultado[4], proceso=proceso)

	else:

		return render_template("/sistemas_ecuaciones/pivoteo-total.html")

@app.route("/crout", methods=["POST", "GET"])
def croutWeb():
	
	if request.method == 'POST':

		if request.form.get("checkEtapas"): proceso = True
		else: proceso = False
		
		matriz = request.form["txtA"].split("\n")
		b = request.form["txtB"].split(",")

		A = [] # Matriz de coeficientes.

		for fila in matriz: A.append(fila.split(","))
	
		for i in range(len(A)):
			for j in range(len(A[0])): A[i][j] = float(A[i][j])

		for i in range(len(b)): b[i] = float(b[i])

		resultado = factorizacionDirecta(A, len(A), b, "Crout")

		return render_template("/sistemas_ecuaciones/crout.html", etapas=resultado[0], numEtapas=len(resultado[0]), x=resultado[1], n=len(A),
				z=resultado[2], Lb=resultado[3], Uz=resultado[4], proceso=proceso)

	else:
		
		return render_template("/sistemas_ecuaciones/crout.html")

@app.route("/doolittle", methods=["POST", "GET"])
def doolittleWeb():
	
	if request.method == 'POST':
		
		if request.form.get("checkEtapas"): proceso = True
		else: proceso = False

		matriz = request.form["txtA"].split("\n")
		b = request.form["txtB"].split(",")

		A = [] # Matriz de coeficientes.

		for fila in matriz: A.append(fila.split(","))
	
		for i in range(len(A)):
			for j in range(len(A[0])): A[i][j] = float(A[i][j])

		for i in range(len(b)): b[i] = float(b[i])

		resultado = factorizacionDirecta(A, len(A), b, "Doolittle")

		return render_template("/sistemas_ecuaciones/doolittle.html", etapas=resultado[0], numEtapas=len(resultado[0]), x=resultado[1], n=len(A),
				z=resultado[2], Lb=resultado[3], Uz=resultado[4], proceso=proceso)

	else:

		return render_template("/sistemas_ecuaciones/doolittle.html")

@app.route("/cholesky", methods=["POST", "GET"])
def choleskyWeb():
	
	if request.method == 'POST':
		
		if request.form.get("checkEtapas"): proceso = True
		else: proceso = False
	
		
		matriz = request.form["txtA"].split("\n")

		b = request.form["txtB"].split(",")

		A = [] # Matriz de coeficientes.

		
		for fila in matriz: A.append(fila.split(","))
	
		
		for i in range(len(A)):
			for j in range(len(A[0])): A[i][j] = float(A[i][j])

		for i in range(len(b)): b[i] = float(b[i])

		
		resultado = factorizacionDirecta(A, len(A), b, "Cholesky")

		return render_template("/sistemas_ecuaciones/cholesky.html", etapas=resultado[0], numEtapas=len(resultado[0]), x=resultado[1], n=len(A),
				z=resultado[2], Lb=resultado[3], Uz=resultado[4], proceso=proceso)
	else:
			
		return render_template("/sistemas_ecuaciones/cholesky.html")


@app.route("/jacobi", methods=["POST", "GET"])
def jacobiWeb():
	
	if request.method == 'POST':
	

		matriz = request.form["txtA"].split("\n")
		b = request.form["txtB"].split(",")
		xInicial = request.form["txtXInicial"].split(",")
		tolerancia = float(request.form["txtTolerancia"])
		maximoIteraciones = int(request.form["txtMaximoIteraciones"])

		A = [] # Matriz de coeficientes.

		for fila in matriz: A.append(fila.split(","))
	
		for i in range(len(A)):
			for j in range(len(A[0])): A[i][j] = float(A[i][j])

		for i in range(len(b)): b[i] = float(b[i])
		for i in range(len(xInicial)): xInicial[i] = float(xInicial[i])

		resultado = iterativo(xInicial, tolerancia, maximoIteraciones, A, b, "Jacobi")  
		return render_template("/sistemas_ecuaciones/jacobi.html", tabla=resultado[0], numFilas=len(resultado[0]), numColumnas=len(resultado[0][0]), mensaje=resultado[1][0], tipo=resultado[1][1])
	
	else:
		
		return render_template("/sistemas_ecuaciones/jacobi.html")


@app.route("/gaussSeidel", methods=["POST", "GET"])
def gaussSeidelWeb():
	
	if request.method == 'POST':
	
		matriz = request.form["txtA"].split("\n")
		b = request.form["txtB"].split(",")
		xInicial = request.form["txtXInicial"].split(",")
		tolerancia = float(request.form["txtTolerancia"])
		maximoIteraciones = int(request.form["txtMaximoIteraciones"])

		A = [] # Matriz de coeficientes.

		for fila in matriz: A.append(fila.split(","))
	
		for i in range(len(A)):
			for j in range(len(A[0])): A[i][j] = float(A[i][j])

		for i in range(len(b)): b[i] = float(b[i])
		for i in range(len(xInicial)): xInicial[i] = float(xInicial[i])

		resultado = iterativo(xInicial, tolerancia, maximoIteraciones, A, b, "Seidel")  

		return render_template("/sistemas_ecuaciones/gauss_seidel.html", tabla=resultado[0], numFilas=len(resultado[0]), numColumnas=len(resultado[0][0]),
				mensaje=resultado[1][0], tipo=resultado[1][1])
	else:
		return render_template("/sistemas_ecuaciones/gauss_seidel.html")

@app.route("/jacobiRelajado", methods=["POST", "GET"])
def jacobiRelajadoWeb():
	
	if request.method == 'POST':
	
		matriz = request.form["txtA"].split("\n")
		b = request.form["txtB"].split(",")
		xInicial = request.form["txtXInicial"].split(",")
		tolerancia = float(request.form["txtTolerancia"])
		maximoIteraciones = int(request.form["txtMaximoIteraciones"])
		

		A = [] # Matriz de coeficientes.

		for fila in matriz: A.append(fila.split(","))
	
		for i in range(len(A)):
			for j in range(len(A[0])): A[i][j] = float(A[i][j])

		for i in range(len(b)): b[i] = float(b[i])
		for i in range(len(xInicial)): xInicial[i] = float(xInicial[i])

		

	else:
		return render_template("/sistemas_ecuaciones/jacobi_relajado.html")

@app.route("/SOR", methods=["POST", "GET"])
def sorWeb():
	
	if request.method == 'POST':
	
		"""matriz = request.form["txtA"].split("\n")
		b = request.form["txtB"].split(",")
		xInicial = request.form["txtX0"].split(",")
		w = float(request.form["txtW"])
		tolerancia = float(request.form["txtTolerancia"])
		maximoIteraciones = int(request.form["txtMaximoIteraciones"])
		

		A = [] # Matriz de coeficientes.
		B = []
		for fila in matriz: A.append(fila.split(","))
	
		for i in range(len(A)):
			for j in range(len(A[0])): A[i][j] = float(A[i][j])
		
		for fila in b:
			B.append(fila.split(","))
		
		for i in range(len(B)):
			for j in range(len(B[0])): B[i][j] = float(B[i][j])
		

		for i in range(len(xInicial)): xInicial[i] = float(xInicial[i])"""

		#Para pruebas:
		A = np.array([[4,-1,0,3],[1,15.5,3,8],[0,-1.3,-4,1.1], [14,5,-2,30]],dtype=np.float64)
		B = np.array([[1],[1],[1],[1]],dtype=np.float64)

		xInicial = np.array([[0],[0],[0],[0]],dtype=np.float64)
		tolerancia = 1e-7
		maximoIteraciones = 100
		w = 1.5

		resultado = SORMatricial(A, B, xInicial, tolerancia, maximoIteraciones, w)
		print("*************************Imprimir tabla desde web*************************")
		contF = 0
		tempVect = []
		for fila in resultado[0]:

			print(contF)
			for element in fila[1]:
				tempVect.append(element[0])
			fila[1] = tempVect
			print(tempVect)
			contF += 1
			tempVect = []
		
		print("******************************************************************************")
		print("*************************Imprimir tabla desde web buena*************************")
		for fila in resultado[0]:
			print(fila)

		print("******************************************************************************")
		print("*************************Imprimir mensaje desde web*************************")
		print(resultado[1])
		print("******************************************************************************")
		return render_template("/sistemas_ecuaciones/SOR.html", tabla=resultado[0], numFilas=len(resultado[0]), numColumnas=len(resultado[0][0]),
				mensaje=resultado[1][0], tipo=resultado[1][1])	
	else:   
		return render_template("/sistemas_ecuaciones/SOR.html")

# ========================================================================
# Interpolacion.
# ========================================================================

@app.route("/diferenciasDivididas", methods=["POST", "GET"])
def newtonDiferenciasDivididasWeb():

	if request.method == 'POST':

		xEval = float(request.form["txtXEval"])
		x = request.form["txtX"].split(",")
		y = request.form["txtY"].split(",")

		for i in range(len(x)): x[i] = float(x[i])
		for i in range(len(y)): y[i] = float(y[i])

		b = calcularB(x, y)
		yEval = p(xEval, b, x)
		
		return render_template("/interpolacion/diferencias_divididas.html", b=b, xEval=xEval, yEval=yEval, x=x, y=y, n=len(x)-1)

	else:
		
		return render_template("/interpolacion/diferencias_divididas.html")

@app.route("/lagrange", methods=["POST", "GET"])
def lagrangeWeb():

	if request.method == 'POST':
		
		xEval = float(request.form["txtXEval"])
		x = request.form["txtX"].split(",")
		y = request.form["txtY"].split(",")

		for i in range(len(x)): x[i] = float(x[i])
		for i in range(len(y)): y[i] = float(y[i])

		resultado = pLagrange(xEval, x, y)	
		return render_template("/interpolacion/lagrange.html", xEval=xEval, yEval=resultado[0], expr=resultado[1], x=x, y=y, n=len(x)-1)

	else:  
		return render_template("/interpolacion/lagrange.html")

@app.route("/splineLineal", methods=["POST", "GET"])
def splineLinealWeb():

	if request.method == 'POST':
		
		xEval = float(request.form["txtXEval"])
		x = request.form["txtX"].split(",")
		y = request.form["txtY"].split(",")

		for i in range(len(x)): x[i] = float(x[i])
		for i in range(len(y)): y[i] = float(y[i])

		resultado = mainLineal(x, y, xEval)
	   
		return render_template("/interpolacion/spline_lineal.html", xEval=xEval, yEval=resultado[0], expr=resultado[1], x=x, y=y, n=len(x)-1, numExpr=len(resultado[1]))
		
	else:
		
		return render_template("/interpolacion/spline_lineal.html")

@app.route("/splineCuadratico", methods=["POST", "GET"])
def splineCuadraticoWeb():

	if request.method == 'POST':
		
		xEval = float(request.form["txtXEval"])
		x = request.form["txtX"].split(",")
		y = request.form["txtY"].split(",")

		for i in range(len(x)): x[i] = float(x[i])
		for i in range(len(y)): y[i] = float(y[i])
		
		resultado = mainCuadratico(x, y, xEval)

		return render_template("/interpolacion/spline_cuadratico.html", xEval=xEval, yEval=resultado[0], expr=resultado[1], x=x, y=y,
				n=len(x)-1, numExpr=len(resultado[1]))
	
	else:
		return render_template("/interpolacion/spline_cuadratico.html")

@app.route("/splineCubico", methods=["POST", "GET"])
def splineCubicoWeb():

	if request.method == 'POST':
		
		xEval = float(request.form["txtXEval"])
		x = request.form["txtX"].split(",")
		y = request.form["txtY"].split(",")

		for i in range(len(x)): x[i] = float(x[i])
		for i in range(len(y)): y[i] = float(y[i])
		
		resultado = mainCubico(x, y, xEval)
		
		return render_template("/interpolacion/spline_cubico.html", xEval=xEval, yEval=resultado[0], expr=resultado[1], x=x, y=y,
				n=len(x)-1, numExpr=len(resultado[1]))

	else:
		return render_template("/interpolacion/spline_cubico.html")


app.run()
