# Guess The Number (With Import Random)
# Tuesday, March 29, 2022

import random
# Si queremos hacer números aleatorios utilizamos la librería "RANDOM", el "import" sirve para importar la "herramienta"
# en este caso es "random" y es importante ponerlo en la primera línea de código o si no, no funcionará

print("Hola te propongo un reto, pensare en un numero entre el 1 y 10 si lo adivinas ganas.")
print("¡Perfecto, buena suerte!")

numero_ganador = random.randint(1, 10)
# Para utilizar la herramienta "RANDOM" tenemos que elegir una función(hay varias) pero en mi caso
# será ".randint()" que en el código se verá asi "random.randint()"
# La función ".randint()" sirve para generar números aleatorios en Python de valor entero

numero_elegido = int(input("¿En que número estoy pensando? "))
# Hemos utilizado "INT" porque si no la respuesta del usuario sería un "STR" y no podríamos comparar una STRING con
# un valor ARITMÉTICO en las estructuras de control como "IF..."

if numero_elegido == numero_ganador:
    print("¡Enhorabuena has ganado!")

if numero_elegido > 10:
    print("Te has pasado un poco")
# >  mayor que
# <  menor que
if numero_elegido < 1:
    print("Te has quedado corto")

if numero_elegido != numero_ganador:
    print("El número ganador era {}".format(numero_ganador))

