# suma, resta, multiplicación, división, módulo

def suma(num1, num2):
    return num1 + num2


def resta(num1, num2):
    return num1 - num2


def multiplicacion(num1, num2):
    return round(num1 * num2,2)

def dividir(num1, num2):
    try:
        resultado = num1 / num2
        return resultado
    except ZeroDivisionError:
        return "Error: No se puede dividir por cero"

def modulo(num1, num2):
    try:
        resultado = num1 % num2
        return resultado
    except ZeroDivisionError:
        return "Error: No se puede dividir por cero"