# Choosing your new mobile
# Friday, April 8, 2022

a = "Iphone Ultra Pro Max"
b = "Iphone Segunda Mano"
c = "Android Chino 100 €"
d = "Google Pixel Super Camara"
e = "Android Calidad Precio"

print("Hola te ayudare a elegir tu nuevo móvil con unas preguntas sencillas.")

opcion = input("¿Que prefieres IOS o Android? ")


# Esto se le conoce como Condiciones Anidadas, pues es una estructura condicional dentro de otra
if opcion == "Android":
    presupuesto = input("¿Dispones de más de 150 €? (S/N) ")

    if presupuesto == "S":
        camara = input("¿Te importa la cámara del móvil? (S/N) ")

        if camara == "S":
            print("La opción más viable es {}.".format(d))

        if camara == "N":
            print("La opción más viable es {}.".format(e))

        else:  # No le importa la cámara
            print("La opción más viable es {}.".format(e))

    else:  # No tiene dinero
        print("La opción mas viable es {}.".format(c))
        # Estos dos ELSE nos permiten ahorrarnos el tener que escribir dos condicionales IF
        # Y esto es posible, ya que solo nos queda la opción que el usuario conteste "N" o cualquier otra cosa
        # asi que lo "resumimos" con el ELSE lo mismo ocurre con los ELSE de la línea 44 y 47


elif opcion == "IOS":
    presupuesto = input("¿Dispones de más de 500€? (S/N) ")

    if presupuesto == "S":
        print("La opciones más viable es {}.".format(a))

    else:
        print("La opción más viable es {}.".format(b))

else:
    print("Elige las opciones disponibles")
    exit()

