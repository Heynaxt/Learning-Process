
titulo = "Bienvenido al Test Como de virgen eres según el LOL"
print("\n" + titulo + "\n" + "-" * len (titulo) + "\n")

puntuacion = 0

opcion = input("Pregunta 1: Cual de estos campeones has jugado más?\n"
               "A - Nidalee\n"
               "B - Malzahar\n"
               "C - Garen\n"
               "Respuesta: ")
if opcion == "A":
    puntuacion += 0
elif opcion == "B":
    puntuacion += 5
elif opcion == "C":
    puntuacion += 10
else:
    print("Las opciones posibles són A, B y C")
    exit()

opcion = input("Pregunta 2: Que haces cuando te tilteas mucho en una partida?\n"
               "A - Me aguanto y sigo jugando\n"
               "B - Me pongo a insultar a todo el mundo y le hecho la culpa a mi equipo\n"
               "C - Me voy AFK\n"
               "Respuesta: ")

if opcion == "A":
    puntuacion += 0
elif opcion == "B":
    puntuacion += 5
elif opcion == "C":
    puntuacion += 10
else:
    print("Las opciones posibles són A, B y C")
    exit()

opcion = input("Pregunta 3: Que prefieres las tres opciones siguientes:\n"
               "A - Socializar\n"
               "B - Jugar al LOL y pasármelo bien (improbable)\n"
               "C - Mi objetivo de vida es llegar a Challenger\n"
               "Respuesta: ")

if opcion == "A":
    puntuacion += 0
elif opcion == "B":
    puntuacion += 5
elif opcion == "C":
    puntuacion += 10
else:
    print("Las opciones posibles són A, B y C")
    exit()

if puntuacion >= 30:
    print("Resultado: Eres trivirgen y además no tienes padre enhorabuena")
elif puntuacion >= 15:
    print("Resultado: Eres virgen, pero tienes posibilidades de perderla y tienes padre")
else:
    print("Resultado: Lo siento tío/a, pero si juegas al lol eres virgen si o si aunque eres salvable")