# Guess The Number
# Monday, March 28, 2022

print("Hola bienvenido, me llamo Atom, te propongo un juego. Te diré una adivinanza y tendrás que decirme la respuesta")

si = input("¿Que me dices, te atreves? (S/N) ")
respuesta = None
a = "2"

# "==" evalua que los valores sean iguales.
# "!=" evalúa si los valores son distintos.
# "="  este símbolo es ASIGNACIÓN

if si == "S":
    print("¡Perfecto, buena suerte!")
    respuesta = input("Soy más de uno sin llegar a tres y llego a cuatro cuando dos me des. ¿Cuál número soy? ")
# Aquí le asigno a la VARIABLE "respuesta" porque si no le asignáramos nada a la respuesta del comando INPUT no tendría
# salida y sería inútil

# La estructura básica de esta sentencia if es la siguiente:
if respuesta == a:
    print("Enhorabuena has ganado, aunque solo por esta vez.")

if si != "S" or respuesta != a:
    print("Otra vez sera")
# La estructura de control if... permite que un programa ejecute unas instrucciones cuando se cumplan una condición
# "Si la expresión evaluada en este caso "if si == "S":", resulta ser verdadera(True), se ejecuta el bloque de
# sentencias. Si el resultado es False no se ejecuta el bloque de sentencias.
