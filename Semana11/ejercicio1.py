while True:
    try:
        edad = int(input("Escribe tu edad: "))
        break
    except ValueError:
        print("Debes ingresar un numero carnal")
        
if edad >=18:
    print("Eres un adulto, pagale al SAT")
else:
    print("Estas chiquito, Aun no eres adulto")