from operaciones.basicOperations import suma, resta, multiplicacion, dividir, modulo
from operaciones.otherOperations import calcular_mcm, calcular_mcd,potencia
from validaciones import es_numero
import os

archivo_registro = "registro_op.txt"

def verificar():
    if os.path.exists(archivo_registro):
        with open(archivo_registro, "r") as f:
            lineas = f.readlines()
        if len(lineas) >= 10:
            with open(archivo_registro, "w") as f:
                f.writelines(lineas[1:])

def guardar_operacion(operacion, a, b):
    verificar()
    resultado = operacion(a, b)
    with open(archivo_registro, "a") as f:
        f.write(f"{a},{b},{operacion.__name__},{resultado}\n")

def ultimoResultado():
    if os.path.exists(archivo_registro):
        with open(archivo_registro, "r") as f:
            filas = f.readlines()
        if filas:
            ultimafila = filas[-1].strip()
            partes = ultimafila.split(",")
            if len(partes) == 4:
                return float(partes[3])
    return None

def mostrarHistorial():
    if os.path.exists(archivo_registro):
        with open(archivo_registro, "r") as archivo:
            print("-"*48)
            print("Historial de Operaciones:")
            print("-"*48)
            for linea in archivo:
                partes = linea.strip().split(",")
                if len(partes) == 4:
                    a, b, operacion, resultado = partes
                    print(f"{a} {operacion} {b} = {resultado}")
            print("-"*48)
    else:
        print("El historial está vacío.")

def menu_calculadora():
    while True:
        print("Seleccione una operación:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Módulo")
        print("6. Potencia")
        print("7. Mínimo Común Múltiplo (MCM)")
        print("8. Máximo Común Divisor (MCD)")
        print("9. Para mostrar el historial")
        print("0. Salir")

        opcion = input("Ingrese la opcion deseada: ")
        if opcion in ["1", "2", "3", "4", "5", "6", "7", "8"]:
            a = ultimoResultado()
            if a is None:
                a = es_numero(input("Ingrese el primer número: "))
            b = es_numero(input("Ingrese el segundo número: "))


        if opcion == "1":
            guardar_operacion(suma, a, b)
            r = suma(a,b)
            print("-"*48)
            print(f"La suma de {a} y {b} es {r}")
            print("-"*48)

        elif opcion == "2":
            guardar_operacion(resta, a, b)
            r = resta(a,b)
            print("-"*48)
            print(f"La resta de {a} y {b} es {r}")
            print("-"*48)

        elif opcion == "3":
            guardar_operacion(multiplicacion, a, b)
            r = multiplicacion(a,b)
            print("-"*48)
            print(f"La multiplicación de {a} y {b} es {r}")
            print("-"*48)

        elif opcion == "4":
            guardar_operacion(dividir, a, b)
            r = dividir(a,b)
            print("-"*48)
            print(f"La división de {a} y {b} es {r:.2f}")
            print("-"*48)

        elif opcion == "5":
            guardar_operacion(modulo, a, b)
            r = modulo(a,b)
            print("-"*48)
            print(f"El resto de la división de {a} y {b} es {r}")
            print("-"*48)

        elif opcion == "6":
            guardar_operacion(potencia, a, b)
            r = potencia(a,b)
            print("-"*48)
            print(f"{a} elevado a la {b} es igual a {r}")
            print("-"*48)

        elif opcion == "7":
            guardar_operacion(calcular_mcm,a,b)
            r = calcular_mcm(a,b)
            print("-"*48)
            print(f"El MCM de {a} y {b} es {r}")
            print("-"*48)

        elif opcion == "8":
            guardar_operacion(calcular_mcd,a,b)
            r = calcular_mcd(a,b)
            print("-"*48)
            print(f"El MCD de {a} y {b} es {r}")
            print("-"*48)
        elif opcion == "9":
            mostrarHistorial()
            continue
        elif opcion == "0":
            break
        else:
            print("Opción no válida. Intente nuevamente.")

        

if __name__ == "__main__":
    menu_calculadora()
