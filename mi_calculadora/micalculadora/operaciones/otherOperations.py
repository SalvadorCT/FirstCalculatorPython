# mínimo común múltiplo , máximo común divisor,potencia

def calcular_mcd(num1, num2):
    while num2:
        num1, num2 = num2, num1 % num2
    return num1

def calcular_mcm(num1, num2):
    if num1 == 0 or num2 == 0:
        return 0
    mcm = abs(num1 * num2) // calcular_mcd(num1, num2)
    print(f"El MCM de {num1} y {num2} es {mcm}")
    return mcm

def potencia(base, exponente):
    try:
        resultado = base ** exponente
        return resultado
    except Exception as e:
        return f"Error: {e}"
    
