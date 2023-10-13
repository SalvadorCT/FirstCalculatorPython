import pytest
from micalculadora.operaciones.basicOperations import suma,resta,dividir,modulo
from micalculadora.operaciones.otherOperations import mayor,menor, fibonacci, factorial,potencia, calcular_mcm, calcular_mcd

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

@pytest.mark.parametrize(
        "a, b, resultado", 
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
            (0,5, 0),
            (23,2,11.5)
        ]
    )

def test_division(a, b, resultado):
    # if b == 0:
    #     with pytest.raises(ZeroDivisionError):
    #         dividir(a, b)
    # else:
    assert dividir(a, b) == resultado

@pytest.mark.parametrize(
        "a, b, resultado", 
        [
            (10, 3, 1), 
            (15, 5, 0),
            (10,2,0)
        ]
    )

def test_modulo(a, b, resultado):
    assert modulo(a, b) == resultado


@pytest.mark.parametrize(
        "a, resultado", 
        [
            ((10, 3), 10), 
            ((15, 5), 15),
            ((0,2),2)
        ]
    )

def test_modulo(a, resultado):
    assert mayor(a) == resultado


@pytest.mark.parametrize(
        "a, resultado", 
        [
            ((10, 3), 3), 
            ((15, 5), 5),
            ((0,2),0)
        ]
    )

def test_modulo(a, resultado):
    assert menor(a) == resultado


@pytest.mark.parametrize(
        "a, resultado", 
        [
            (4, 24), 
            (2, 2),
            (0, 1)
        ]
    )

def test_modulo(a, resultado):
    assert factorial(a) == resultado

@pytest.mark.parametrize(
        "a,b, resultado", 
        [
            (5, 2,25),
            (0, 0,0),
            (12,2,144),
            (1, 2,1)
        ]
    )

def test_modulo(a,b, resultado):
    assert potencia(a,b) == resultado

@pytest.mark.parametrize(
        "a, resultado", 
        [
            (5, [0, 1, 1, 2, 3, 5]),
            (0, [0]),
            (12, [0, 1, 1, 2, 3, 5, 8]),
            (1, [0,1])
        ]
    )

def test_modulo(a, resultado):
    assert fibonacci(a) == resultado