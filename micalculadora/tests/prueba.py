import pytest
from micalculadora.operaciones.basicOperations import suma

@pytest.mark.parametrize(
    "input_x, input_y, expected",
    [
        (5, 3, 8),
        (0, 0, 0),
        (-5, 5, 0)
    ]
)
def test_suma(input_x, input_y, expected):
    assert suma(input_x, input_y) == expected