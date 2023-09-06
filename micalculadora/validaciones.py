def es_numero(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False

def es_entero_positivo(valor):
    try:
        entero = int(valor)
        return entero > 0
    except ValueError:
        return False
