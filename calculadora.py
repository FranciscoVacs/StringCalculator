def sumar(numeros):
    
    if numeros == "":
        return 0
    elif len(numeros) == 1:
        return int(numeros)
    else:
        return int(numeros[0]) + int(numeros[2])