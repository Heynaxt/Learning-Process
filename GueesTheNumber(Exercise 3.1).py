# Guess The Number (With Import Random)
# Tuesday, March 29, 2022

import random
print("Hola te propongo un reto, pensare en un numero entre el 1 y 10 si lo adivinas ganas.")

numero_ganador = random.randint(1, 10)
si = input("¿Que me dices, te atreves? (S/N) ")


if si == "S":
    print("¡Perfecto, buena suerte!")
    numero_elegido = int(input("¿En que número estoy pensando? "))


if numero_elegido == numero_ganador:
    print("¡Enhorabuena has ganado!")

if numero_elegido != numero_ganador:
    print("El número ganador era {}".format(numero_ganador))

