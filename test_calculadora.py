import pytest 
from calculadora import sumar

def test_vacio():
    assert sumar("") == 0 

def test_de_un_numero():
    assert sumar("5") == 5

