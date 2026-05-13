def sumar(numeros):
    
    if not numeros :
        return 0
    elif "//" in numeros:
        delimitador = numeros[2]
        numeros = numeros[4:]
    else:
        numeros = numeros.replace("\n", ",")
        delimitador = ","
    
    
    lista_numeros = numeros.split(delimitador)

    return sum(int(n) for n in lista_numeros)

    