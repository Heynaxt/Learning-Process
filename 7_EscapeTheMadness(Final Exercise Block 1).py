# Escape the madness
# Monday, April 11, 2022

import random

print("Escapa De La Locura\n"
      "-------------------\n"
      "\n"
      "Te levantas en una especie de cubículo 4x4, la habitación es totalmente blanca excepto las paredes que son\n"
      "espejos, te ves reflejado en todas ellas. Vas vestido con un mono blanco, la habitación esta totalmente vacía,\n"
      "te das cuenta de que tu mono tiene varios bolsillos, buscas en el bolsillo derecho y hay una nota que dice:\n"
      "En lo mas profundo de la oscuridad se puede ver todo con más claridad.\n"
      "\n")

respuesta1 = input("¿Que haces intentas decifrar la nota o la ignoras?\n"
                   "A - Comienzas a buscar por la habitación algún interruptor o de donde proviene la luz\n"
                   "B - La ignoras y comienzas a romper los espejos de la habitación\n"
                   "Respuesta: ")
print("\n")

if respuesta1 == "A":
      respuesta1 = input("Buscas por toda la habitación algún interruptor o algo que se le parezca, te das cuenta que\n"
                         "en uno de los espejos el reflejo se distorsiona un poco, lo miras con detalle y te das\n"
                         "cuenta que es una escotilla o algún tipo de armario muy bien camuflado.\n"
                         "¿Como lo abres?\n"
                         "A - Haces un poco de presión sobre esa parte del espejo para ver si se abre\n"
                         "B - Utilizas la fuerza bruta y rompes esa parte del espejo\n"
                         "Respuesta: ")
      if respuesta1 == "A":
          input("¿Rompes esa parte, aunque tu mano está sangrando mucho, detrás hay un interruptor y una pequeña caja\n"
                "que contiene una navaja multi-herramienta, de repente escuchas, pasos y gritos de gente corriendo\n"
                "hacia tu cubículo, que haces?\n"
                "A - Apagas el interruptor y te escondes lo más rapido posible\n"
                "B - Coges la navaja, te escondes y esperas a que entren al cubiculo para atacarles\n"
                "Respuesta: ") 
      elif respuesta1 == "B":
          input("Entran 3 cosas humanoides con los rostros borrosos, tu estas detras de la puerta para cuando\n"
                "entre el ultimo atacarlos, te das cuenta que la puerta no se puede abrir desde dentro solo desde\n"
                "fuera, y también se bloquea desde fuera con escáner dactilar, lo piensas mejor, tienes dos\n" 
                "opciones:\n"
                "A - Sales corriendo por la puerta y la bloqueas desde fuera\n"
                "B - Coges al ultimo que entra por la espalda poniéndole la navaja en el cuello, amenazas con\n"
                "matarlo si se acercan, sales lentamente sin darle la espalda a los humanoides, cuando estas\n"
                "fuera cierras la puerta rápidamente y la bloqueas utilizando la huella dactilar del humanoide.\n"
                "La criatura no dice nada, te encuentras en un dilema, te ralentiza mucho y eso es un problema\n"
                "si estas intentando escapar, pero te puede ser util por si necesitas su huella dactilar, hay\n"
                "hay varias opciones:\n"
                    "A - Te lo llevas contigo\n"
                    "B - Lo matas para que no pueda delatarte y le cortas el dedo, le quitas su ropa y te la pones\n"
                    "para pasar desapercibido\n"
                    "C -")
      print("\n")
      else:
            print("Se abre una especie de puerta de armario, dentro hay un interruptor y una pequeña caja que contiene\n"
                  "una navaja multi-herramienta")
      
      print("\n")
else:
    print("Una alarma comienza a sonar y las luces se vuelven rojas, de repente en la habitación entran dos personas\n"
          "con el rostro borroso y te inyectan un paralizante, y te llevan a un cubículo mucho más seguro.\n" 
          "Es casi imposible escapar.")

