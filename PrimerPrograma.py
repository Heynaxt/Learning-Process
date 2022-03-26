
# My Learning Process
# Today, March 26, 2022 begins my learning process of programming.

print("Hola, encontraré por ti el número más grande y más pequeño de los tres números que pondrás a continuación.")
# Lo que está entre comillas "Hola..." es una Cadena De Texto o un STRING(str)
# La función print() permite presentar los resultados de nuestros programas en pantalla

print("Por favor introduce los 3 números")

numero1 = int(input("Introduce un número: "))
# A 1, 1+4, 1*2... se le conoce como Operaciones Aritméticas o Aritmética(Números enteros como 1,2,3...)
# ARITMETICA(int)

numero2 = int(input("Introduce un número: "))
# El "numero2=..." Es una variable y la variable puede contener cualquier dato
# "numero2=..." Esto es una VARIABLE y ..."=int..." es un DATO

numero3 = int(input("Introduce un número: "))
# El comando "Input("...") sirve para que el usuario pueda introducir un valor
# Por ejemplo "Input("¿Cuál es tu nombre?") usuario: David"
# "David" es un VALOR

# La función de int(...)) es transformar un dato String(str) a un valor Aritmetico(int)
# Y esto también se puede aplicar al contrario como vemos en las lineas 24 y 27

maximo = str(max(numero1, numero2, numero3))
# El comando "max("...")" sirve para encontrar el máximo valor de varios números

minimo = str(min(numero1, numero2, numero3))
# El comando "min("...")" sirve para encontrar el mínimo entre varios números

print("El número más grande es "+maximo + " y el número más pequeño es "+minimo)
# Podemos concatenar STR con INT con "{}.format("..."), sin tener que pasar INT a STR por ejemplo:
# print("El número más grande es {}".format(minimo).
# El "comando" '{}".format' sirve para formatear strings metiéndole dentro números o cualquier otro tipo de variable.

