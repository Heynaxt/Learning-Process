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
      print("\n")