from operaciones.basicOperations import suma, resta, multiplicacion, dividir, modulo
from operaciones.otherOperations import mayor,menor, fibonacci, factorial, calcular_mcm, calcular_mcd
from micalculadora.validaciones import es_numero

def menu_calculadora():
    while True:
        print("Seleccione una operación:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Módulo")
        print("6. Mayor/Menor")
        print("7. Fibonacci")
        print("8. Factorial")
        print("9. Mínimo Común Múltiplo (MCM)")
        print("10. Máximo Común Divisor (MCD)")
        print("0. Salir")
        opcion = input("Ingrese el número de la operación deseada: ")
        if opcion == "1":
            a = input("Ingrese el primer número: ")
            b = input("Ingrese el segundo número: ")
            # Validar la entrada del usuario
            if es_numero(a) and es_numero(b):
                resultado = suma(float(a), float(b))
                print(f"Resultado: {resultado}")
            else:
                print("Entrada no válida. Ingrese números válidos.")

        elif opcion == "2":
            pass
        elif opcion == "0":
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    menu_calculadora()