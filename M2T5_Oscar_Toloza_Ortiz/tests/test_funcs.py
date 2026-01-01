import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.funcs import *


# =====================
# Tests sumatoria_positivos
# =====================
@pytest.mark.parametrize("nums, esperado", [
    ([], 0),
    ([-1, -5, -10], 0),
    ([1, 2, 3], 6),
    ([1, -2, 3, -4], 4),
    ([0, -1, 5], 5)
])
def test_sumatoria_positivos(nums, esperado):
    assert sumatoria_positivos(nums) == esperado

# =====================
# Tests es_palindromo
# =====================
@pytest.mark.parametrize(
    "s, esperado",
    [
        ("ana", True),
        ("Anita lava la tina", True),
        ("reconocer", True),
        ("", True),
        ("Python", False),
        ("Hola", False),
        ("A man a plan a canal Panama", True),
        ("Not a palindrome", False)
    ],
    ids=[
        "simple", "frase_larga", "reconocer", "vacio",
        "negativo_python", "negativo_hola", "frase_con_palindromo", "negativo_no_palindrome"
    ]
)
def test_es_palindromo(s, esperado):
    assert es_palindromo(s) == esperado

# =====================
# Tests maximo_seguro
# =====================
def test_maximo_seguro_normal():
    assert maximo_seguro([1, 2, 3]) == 3
    assert maximo_seguro([2.5, 7.1, 0.2]) == 7.1

def test_maximo_seguro_error():
    with pytest.raises(ValueError):
        maximo_seguro([])

# =====================
# Tests contar_palabras
# =====================
def test_contar_palabras():
    assert contar_palabras("") == {}
    assert contar_palabras("Hola hola") == {"hola": 2}
    assert contar_palabras("Uno dos dos") == {"uno":1, "dos":2}
    # Caso adicional para mayúsculas mezcladas
    assert contar_palabras("Hola hOLA HoLa") == {"hola": 3}

# =====================
# Tests filtrar_aprobados
# =====================
@pytest.mark.parametrize("pares, esperado", [
    ([], []),
    ([("Ana", 6), ("Luis", 7)], ["Ana","Luis"]),
    ([("Ana", 6), ("Luis", 4)], ["Ana"]),
    ([("Ana", 5), ("Luis", 5)], ["Ana","Luis"])
])
def test_filtrar_aprobados(pares, esperado):
    assert filtrar_aprobados(pares) == esperado

# =====================
# Tests normalizar_email
# =====================
def test_normalizar_email_valido():
    assert normalizar_email("User@Domain.COM") == ("user","domain.com")

def test_normalizar_email_invalido():
    # Caso sin '@' (0 '@')
    with pytest.raises(ValueError):
        normalizar_email("usuario#dominio.com")
    with pytest.raises(ValueError):
        normalizar_email("sinarroba")
    # Caso con 2 '@'
    with pytest.raises(ValueError):
        normalizar_email("usuario@@dominio.com")

# =====================
# Tests factorial
# =====================
@pytest.mark.parametrize("n, esperado", [
    (0,1),
    (1,1),
    (5,120)
])
def test_factorial_param(n, esperado):
    assert factorial(n) == esperado

def test_factorial_error():
    with pytest.raises(ValueError):
        factorial(-1)

# =====================
# Tests media
# =====================
def test_media_normal():
    assert media([1,2,3]) == pytest.approx(2.0)
    assert media([2.5, 3.5]) == pytest.approx(3.0)

def test_media_error():
    with pytest.raises(ValueError):
        media([])
