def es_entero_positivo(valor):
    try:
        if int(valor) >= 0:
            return valor
    except ValueError:
        print("\n!Intentelo Nuevamente¡ - No es entero Positivo\n")
        valor = input("Ingrese numero: ")
        return es_entero_positivo(valor)

def es_numero(valor):
    try:
        return float(valor)
    except ValueError:
        print("\n!Intentelo Nuevamente¡ - No es numero\n")
        valor = input("Ingrese numero: ")
        return es_numero()

# def input_data_basic():
#     a = es_numero(input("Ingrese el primer número: "))
#     b = es_numero(input("Ingrese el segundo número: "))
#     return a,b