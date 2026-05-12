def sumar(numeros):
    
    

    if not numeros :
        return 0
        
    numeros = numeros.replace("\n", ",")

    lista_numeros = numeros.split(",")

    return sum(int(n) for n in lista_numeros)

    