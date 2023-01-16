import math

def operacionSuma(num1, num2):

    return float(num1+num2)

def operacionResta(num1, num2):

    return float(num1-num2)

def operacionMultiplicacion(num1, num2):

    return float(num1 * num2)

def operacionDivision(num1, num2):

    return float(num1 / num2)

def operacionPotencia(num1, num2):

    return math.pow(num1, num2) 

def operacionRaiz(num1, num2):

    return math.pow(num1, 1/num2)

def operacionSen(num1):
    
    radianes = math.radians(num1)

    return math.sin(radianes)

def operacionCos(num1):
    
    radianes = math.radians(num1)

    return math.cos(radianes)

def operacionTan(num1):
    
    radianes = math.radians(num1)

    return math.tan(radianes)