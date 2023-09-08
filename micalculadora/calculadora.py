from operaciones.basicOperations import suma, resta, multiplicacion, dividir, modulo
from operaciones.otherOperations import mayor,menor, fibonacci, factorial, calcular_mcm, calcular_mcd,potencia
from micalculadora.validaciones import es_numero,input_data_basic,es_entero_positivo

def menu_calculadora():
    while True:
        print("Seleccione una operación:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Módulo")
        print("6. Mayor")
        print("7. Menor")
        print("8. Fibonacci")
        print("9. Factorial")
        print("10. Mínimo Común Múltiplo (MCM)")
        print("11. Máximo Común Divisor (MCD)")
        print("0. Salir")

        opcion = input("Ingrese el número de la operación deseada: ")
        if opcion == "1":
            suma(*input_data_basic())
        elif opcion == "2":
            resta(*input_data_basic())
        elif opcion == "3":
            multiplicacion(*input_data_basic())
        elif opcion == "4":
            dividir(*input_data_basic())
        elif opcion == "5":
            modulo(*input_data_basic())
        elif opcion == "6":
            mayor(input_data_basic())
        elif opcion == "7":
            menor(input_data_basic())
        elif opcion == "8":
            fibonacci(es_entero_positivo(es_numero("Ingrese numero: ")))
        elif opcion == "9":
            factorial(es_entero_positivo(es_numero("Ingrese numero: ")))
        elif opcion == "10":
            potencia(*input_data_basic())
        elif opcion == "11":
            calcular_mcm(*input_data_basic())
        elif opcion == "12":
            calcular_mcd(*input_data_basic())
        elif opcion == "0":
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    menu_calculadora()
