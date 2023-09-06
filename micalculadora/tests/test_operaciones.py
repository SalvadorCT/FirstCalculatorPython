import pytest
from micalculadora.operaciones.basicOperations import suma
# from mi_calculadora.operaciones.basicOperations import suma,resta,dividir,modulo
# from mi_calculadora.operaciones.basicOperations import suma, resta, multiplicacion, dividir, modulo
from micalculadora.operaciones.otherOperations import mayor,menor, fibonacci, factorial, calcular_mcm, calcular_mcd

@pytest.mark.parametrize(
        "input_x, input_y, expected", 
        [
            (5, 3, 8),
            (0, 0, 0),
            (-5, 5, 0),
        ]
    )

def test_suma(input_x, input_y, expected):
    assert suma(input_x, input_y) == expected
"""
@pytest.mark.parametrize(
        #"a, b, resultado", 
        [
            (5, 3, 2), 
            (0, 0, 0), 
            (10, 5, 5)
        ]
    )

def test_resta(a, b, resultado):
    assert resta(a, b) == resultado

@pytest.mark.parametrize(
        "a, b, resultado", 
        [
            (10, 2, 5.0), 
            (5, 0, None)
        ]
    )

def test_division(a, b, resultado):
    if b == 0:
        with pytest.raises(ZeroDivisionError):
            dividir(a, b)
    else:
        assert dividir(a, b) == resultado

@pytest.mark.parametrize(
        "a, b, resultado", 
        [
            (10, 3, 1), 
            (15, 5, 0)
        ]
    )

def test_modulo(a, b, resultado):
    assert modulo(a, b) == resultado

"""