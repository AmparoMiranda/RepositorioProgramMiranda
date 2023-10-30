#PARCIAL AMPARO MIRANDA COMISIÓN A

#Pedir al usuario su nombre
name = input("Ingrese su nombre: ").upper()
#Generar menú de opciones
print("Bienvenido/a ", name, ", este es el menú de opciones:")
option = input("""
    1) Juego de números
    2) Juego de palabras
    """)
#Si elije la primera opción, realizar el juego de números:
if(option == "1"):
    even_number = 0
    sum = 0
    counter = 0
    average = 0
    while(True):
        #Pedir el ingreso de números enteros
        print(name, end = ", ")
        number = int(input(" ingresa un número entero: "))
        #Salir del bucle si ingresa 0
        if(number == 0):
            break
        elif(number % 2 == 0): #Llegar al mayor número par
            if(number > even_number):
                even_number = number
        else: #Sacar el promedio de los números impares
            counter += 1
            sum += number
    #Mostrar por pantalla el mayor numero par y el promedio de los impares
    print("--------------------------------------------------")
    print("Finalizó el juego de números ", name, ", aquí están los resultados:")
    print("El mayor número par es: ", even_number)
    print("El promedio de los números impares es: ", sum/counter)
    #Segunda opcion juego de palabras:
else:
    vocal_a = 0
    vocal_e = 0
    vocal_i = 0
    vocal_o = 0
    vocal_u = 0

    #Pedir el ingreso de una frase
    print(name, end = ", ")
    phrase = input("Ingrese una frase: ").lower()
    #Sumar cada vez que sale x vocal
    for i in phrase:
        if(i == "a"):
            vocal_a += 1
        elif(i == "e"):
            vocal_e += 1
        elif(i == "i"):
            vocal_i += 1
        elif(i == "o"):
            vocal_o += 1
        elif(i == "u"):
            vocal_u += 1
        else:
            continue
    #Mostrar por pantalla la cantidad final de vocales en la frase
    print("---------------------------------------------")
    print("Cantidad de vocales a: ", vocal_a)
    print("Cantidad de vocales e: ", vocal_e)
    print("Cantidad de vocales i: ", vocal_i)
    print("Cantidad de vocales o: ", vocal_o)
    print("Cantidad de vocales u: ", vocal_u)



