def solicitar_edad():
    try:
        return int(input("Escribe tu edad: "))
    except ValueError:
        print("Ingresa un valor numerico")
        return solicitar_edad()
    
edad = solicitar_edad()