# Currency Converter GBP To EUR
# Saturday, March 26, 2022

print("Hola, soy un conversor de divisas, le ayudaré a pasar de Euros a Libra esterlina")

euro = float(input("Por favor introce la cantidad de Libras estarlinas: "))
# Como veis aquí no he puesto int(input() porque el INT solo es para números enteros, si el usuario intenta convertir
# por ejemplo 9.5 libras a euros le daría un resultado erróneo, para eso es comando FLOAT().
# FLOAT() Permite representar un número positivo o negativo con decimales.

print("{} libras ".format(euro)+"equivale a {} euros.".format(euro*1.20))
