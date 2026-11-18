import os
import sys

import pytest

# Permite importar main.py desde la raíz del proyecto
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from main import dividir, multiplicar, restar, sumar


def test_sumar():
    assert sumar(2, 3) == 5
    assert sumar(-1, 1) == 0


def test_restar():
    assert restar(5, 3) == 2
    assert restar(3, 5) == -2


def test_multiplicar():
    assert multiplicar(4, 3) == 12
    assert multiplicar(5, 0) == 0


def test_dividir():
    assert dividir(10, 2) == 5
    assert dividir(7, 2) == 3.5


def test_dividir_entre_cero():
    with pytest.raises(ValueError, match="No se puede dividir entre cero"):
        dividir(10, 0)
