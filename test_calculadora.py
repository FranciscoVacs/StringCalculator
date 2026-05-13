import pytest 
from calculadora import sumar

def test_vacio():
    assert sumar("") == 0 

def test_de_un_numero():
    assert sumar("5") == 5

def test_de_dos_numeros():
    assert sumar("1,2") == 3

def test_multiples_numeros():
    assert sumar("1,2,3,5,8,13") == 32

def test_barra_n():
    assert sumar("1\n2,3") == 6

def test_delimitador_configurable():
    assert sumar("//;\n1;3;6;4") == 14