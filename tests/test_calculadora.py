import pytest

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from calculadora import sumar, restar, multiplicar, dividir


# 🔧 Fixtures
@pytest.fixture
def enteros():
    return (4, 2)

@pytest.fixture
def flotantes():
    return (0.1, 0.2)

# 🧪 Casos de Éxito
@pytest.mark.smoke
def test_sumar_exito(enteros):
    a, b = enteros
    assert sumar(a, b) == 6

def test_restar_exito(enteros):
    a, b = enteros
    assert restar(a, b) == 2

def test_multiplicar_exito(enteros):
    a, b = enteros
    assert multiplicar(a, b) == 8

def test_dividir_exito(enteros):
    a, b = enteros
    assert dividir(a, b) == 2

# 🧪 Casos de Error
@pytest.mark.exception
def test_dividir_por_cero():
    with pytest.raises(ValueError):
        dividir(10, 0)

# 🧪 Flotantes
def test_sumar_flotantes(flotantes):
    a, b = flotantes
    assert round(sumar(a, b), 1) == 0.3

def test_multiplicar_flotantes(flotantes):
    a, b = flotantes
    assert round(multiplicar(a, b), 2) == 0.02

# 🏷️ Parametrización
@pytest.mark.smoke
@pytest.mark.parametrize("a,b,resultado", [
    (1, 2, 3),
    (-1, 5, 4),
    (0, 0, 0)
])
def test_sumar_parametrizado(a, b, resultado):
    assert sumar(a, b) == resultado

@pytest.mark.parametrize("a,b,resultado", [
    (5, 3, 2),
    (10, 5, 5),
    (0, 0, 0)
])
def test_restar_parametrizado(a, b, resultado):
    assert restar(a, b) == resultado
