while True:
    try:
        x = int(input("Introduce un numero entero: "))
    except ValueError:
        print("no es dato valido, intentale de nuevo......")
    else:
        print("divide entre 50/", x, "el resultado es: ", 50/x)
    finally:
        print("finalizacion de un programa")