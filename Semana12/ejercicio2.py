try:
    lista = [1, 2, 3, 4, 5]
    lista[10]
except(IndexError):
    print("Se esta solicitando un rango de indice mayor al que hay, ingresa un numero que este dentro del rango de indices (para este ejercicio, del 0 al 4)")