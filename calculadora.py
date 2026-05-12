def sumar(numeros=""):
    
    if numeros == "":
        return 0

    return sum(map(int, numeros.split(",")))