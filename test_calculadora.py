import pytest 
from calculadora import sumar

def test_vacio():
    assert sumar("") == 0 

