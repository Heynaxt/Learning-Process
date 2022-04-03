# Park Discount
# Thursday, March 31, 2022

edad = int(input("Dígame su edad: "))
tipo_de_carnet = input("Dígame su tipo de carnet: (E para Estudiante / P pensionista / F Familia Numerosa / N  Nada): ")

# Para plantear este tipo de operaciones booleanas y no liarse una forma de interpretarlas es como nos explica
# Nate en la clase 11 de su curso de Python
if (25 <= edad <= 35 and tipo_de_carnet == "E") or edad <= 10 or (edad >= 65 and tipo_de_carnet == "P") or \
        tipo_de_carnet == "F":
    print("Se le aplica el descuento.")
# El operador AND evalúa si el valor del lado izquierdo y el lado derecho se cumple
# Devuelve True si ambos operandos son True
# "<=" más grande o igual
# ">=" más pequeño o igual
else:
    print("No se te aplica el descuento.")
# ElSE sirve para ejecutar el código alternativo en el caso de que no cumplirse las condiciones de IF
# Se puede ver en este ejercicio si no se cumple las condiciones de "If (25 <= edad ...)" se ejecutara la
# sentencia ELSE que significa "si no..." (condición)