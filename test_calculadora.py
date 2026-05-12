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