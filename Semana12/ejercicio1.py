try:
    resultado = 10/0
    print(resultado)
except(ZeroDivisionError):
    print("Para dividir en este programa, el divisor no tiene que ser 0, intenta insertando un numero diferentes de 0")