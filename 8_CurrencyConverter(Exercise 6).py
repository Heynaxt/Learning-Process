# Currency Converter
# Friday, April 8, 2022

# In this exercise the user will be able to choose which currencies to change.

dolar_euro = 0.919466
euro_dolar = 1.08759
libra_euro = 1.19699
euro_libra = 0.835405


opcion = input("Hola soy un conversor de divisas, por favor elija una de las opciones siguientes:\n"
               "A - Pasar de dólar a euro\n"
               "B - Pasar de euro a dólar\n"
               "C - Pasar de libra esterlina a euro\n"
               "D - Pasar de euro a libra esterlina\n"
               "Respuesta: ")

if opcion == "A":
    euro = float(input("Por favor introduzca la cantidad de dólares: "))
    print("{} dólares ".format(euro)+"equivale a {} euros.".format(euro*dolar_euro))
elif opcion == "B":
    dolar = float(input("Por favor introduzca la cantidad de euros: "))
    print("{} euros ".format(dolar)+"equivale a {} dólares.".format(dolar*euro_dolar))
elif opcion == "C":
    libras = float(input("Por favor introduzca la cantidad de libras esterlinas: "))
    print("{} libras esterlinas ".format(libras)+"equivale a {} euros.".format(libras*libra_euro))
elif opcion == "D":
    euros = float(input("Por favor introduzca la cantidad de euros: "))
    print("{} euros ".format(euros)+"equivale a {} libras esterlinas.".format(euros*euro_libra))
else:
    print("Solo hay opción A, B, C o D.")
    exit()

