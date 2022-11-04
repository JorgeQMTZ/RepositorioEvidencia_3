try:
    print(5/0)
except(TypeError,ZeroDivisionError) as e:
    
    print("Error", e)
else:
    print(5/0)
        
print("Fin del programa")