# Fahrenheit to Celsius
# Today, March 26, 2022

print("Hola, te ayudaré a pasar de grados Fahrenheit a Celsius.")

fahrenheit = int(input("Por favor introduce los grados °F: "))

print("{}°F ".format(fahrenheit) + " són {}°C".format((fahrenheit-32)*5/9))
# Aquí como veis he utilizado {}.format para ahorrarme el tener que pasarlo de STR a INT y luego al revés.




