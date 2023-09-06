# suma, resta, multiplicación, división, módulo

def suma(num1, num2):
    print(f"La suma de {num1} y {num2} es {num1 + num2}")
    return num1 + num2


def resta(num1, num2):
    print(f"La resta de {num1} y {num2} es {num1 - num2}")
    return num1 - num2


def multiplicacion(num1, num2):
    print(f"La multiplicación de {num1} y {num2} es {num1 * num2}")
    return round(num1 * num2,2)

def dividir(num1, num2):
    try:
        resultado = num1 / num2
        print(f"La división de {num1} y {num2} es {resultado:.2f}")
        return resultado
    except ZeroDivisionError:
        return "Error: No se puede dividir por cero"

def modulo(num1, num2):
    try:
        resultado = num1 % num2
        print(f"El resto de la división de {num1} y {num2} es {resultado}")
        return resultado
    except ZeroDivisionError:
        return "Error: No se puede dividir por cero"