import pandas as pd
import numpy as np

nombre = ['Olivia', 'Daniela', 'Juan', 'German', 'Edward', 'Alex', 'Julio', 'Edgar', 'Angie', 'Irlesa']
puntuaje = [11.5, 8, 15.5, np.nan, 8, 19, 13.5, np.nan, 8, 19]
intentos = [1, 3, 2, 3, 2, 3, 1, 1, 2, 1]
califico = ['Si', 'No', 'Si', 'No', 'No', 'Si', 'Si', 'No', 'No', 'Si']

indices = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

jugadores = {'nombre': nombre, 'puntuaje': puntuaje, 'intentos': intentos, 'califico': califico}

df = pd.DataFrame(data=jugadores, index=indices)

print(df)

n = 5
print(df.iloc[0:-n])