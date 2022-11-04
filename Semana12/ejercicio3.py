try:
    colores = { 'rojo':'red', 'verde':'green', 'negro':'black' }
    colores['blanco']
except(KeyError):
    print("No existe el termino que buscas en el arreglo (en este caso 'blanco')")