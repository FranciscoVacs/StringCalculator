import pytest 
from calculadora import sumar

def test_vacio():
    assert sumar("") == 0 

def test_de_coma():
    assert sumar("1,2") == 3