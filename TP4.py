#Ejercicio 1
x = 0
while (x < 30):
    x += 1
    if (x == 4 or x == 6 or x == 10):
        #Saltar las ejecuciones en 4,6 y 10
        print("Se ha saltado el valor " , x )
        continue
    elif (x == 15):
        print("La ejecución del bucle se ha interrumpido cuando x valía 15")
        break
    else:
        print(x)

#Ejercicio 1.2
while True:
    try:
        line = input()
        if line:
            print(line.upper())
        else:
            break
    except EOFError:
        break

#Ejercicio 2
count = 0
moneyD = 0
moneyR = 0
while (True):
    operation = input("""
    Indique la operación que desea realizar, (para finalizar presione enter)
        D) Depositar dinero
        R) Retirar dinero
    """).upper()
    if (operation == "D"):
        moneyD = int(input("Ingrese la cantidad de dinero que desea depositar: "))
        count = count + moneyD
        continue
    elif (operation == "R"):
        moneyR = int(input("Ingrese la cantidad de dinero que desea retirar: "))
        count = count - moneyR
        continue
    else:
        break
print("El total en su cuenta es : $", count)

#Ejercicio 3
numbers = 0
while True:
    num = int(input("Ingrese numeros para determinar cuantos son primos, para finalizar ingrese 0: "))
    if(num == 2 or num % 2 != 0):
        numbers += 1 
    elif(num == 0):
        break
    else:
        continue

print("La cantidad de numeros primos ingresados es : ", numbers)



