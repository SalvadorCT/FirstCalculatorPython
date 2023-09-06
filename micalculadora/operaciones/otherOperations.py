# mayor, menor,igual, diferente, serie Fibonacci, factorial, mínimo común múltiplo máximo común divisor

def mayor(*notas):
    if len(notas) == 0:
        return None
    mayor = 0
    for i in len(notas):
        if i >= mayor:
            mayor = i
    return mayor

def menor(*notas):
    if len(notas) == 0:
        return None
    
    menor = notas[0]
    for nota in notas:
        if nota < menor:
            menor = nota
    return menor

def calcular_mcd(num1, num2):
    while num2:
        num1, num2 = num2, num1 % num2
    
    print(f"El MCD de {num1} y {num2} es {num1}")
    return num1

def calcular_mcm(num1, num2):
    if num1 == 0 or num2 == 0:
        return 0
    mcm = abs(num1 * num2) // calcular_mcd(num1, num2)
    print(f"El MCM de {num1} y {num2} es {mcm}")
    return mcm

def factorial(numero):
    if numero < 0:
        return "No se puede calcular el factorial de un número negativo"
    elif numero == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, numero + 1):
            resultado *= i
        print(f"El factorial de {numero} es {resultado}")
        return resultado


def fibonacci(n):
    try:
        n = int(n)  # Intenta convertir la entrada a un número entero
        if n < 0:
            raise ValueError("El número debe ser mayor o igual a cero")
    except ValueError as e:
        return f"Error: {e}"

    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]

    resultado = [0, 1]
    while resultado[-1] + resultado[-2] <= n:
        resultado.append(resultado[-1] + resultado[-2])

    print(f'La serie de Fibonacci hasta {n} es: {resultado}')
    return resultado


def potencia(base, exponente):
    try:
        resultado = base ** exponente
        print(f"{base} elevado a la {exponente} es igual a {resultado}")
        return resultado
    except Exception as e:
        return f"Error: {e}"