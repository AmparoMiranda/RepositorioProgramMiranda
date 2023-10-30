#compar intentos
#cantidad de plata segun cuando adivino
#al final preguntar si quiere retirar el total x de dinero o seguir jugando
import random
#Ingreso de nombre y edad del usuario
print("------------------------------------------------------------------------------------")
print("Bienvenido/a al juego |  🔮 GUEES THE NUMBER 🔢  |")
name = input("Ingresá tu nombre para comenzar:  ")
age = int(input("Para poder jugar debes ser mayor de 18 años. Ingresa tu edad:  "))
if(age >= 18):
    print("Bienvenido/a ", name, "!!!")
else: 
    print("< DEBES SER MAYOR DE EDAD PARA JUGAR >")
    sys.exit()
print("------------------------------------------------------------------------------------")
#generación de numero aleatorio, declaracion de variables y ciclo while donde comienza el juego
num_random = random.randint(0, 100)
money = 0
lives = 5
print("😁 Adivina el número entre 0 y 100 😁")
print(" ")
print("""REGLAS:
    ⬆️  : el num que ingresó es menor al buscado, ingrese un num mayor
    ⬇️  : el num que ingresó es mayor al buscado, ingrese un num menor
    📃   El dinero ganado en cada partida se irá acumulando, si pierde la partida pierde todo el dinero
    📃   Si aciertas en el primer intento ganas $500, en el segundo intento $400, en el tercer intento $300, en el cuarto intento $200, ultimo  intento $100
""")

while(True):
    print("(Tienes" , lives , "❤️  )")
    #si se queda sin vida sale el mensaje de que perdió y pierde todo el dinero, si le quedan vidas sigue ingresando números
    if(lives == 0):
        print(" ")
        print("OH! LO SIENTO MUCHO ", name, " perdiste 😢   El numero era -> ", num_random )
        money = 0
        break
    else:
        num_user = int(input("  :  "))
        #si el numero que ingresa el usuario es mayor al buscado y tiene vidas disponibles se imprime la flecha y se le resta una vida
        if((num_user > num_random) and (lives > 0)):
            print(" ⬇️ ")
            lives -= 1
            continue    
            #si el numero que ingresa el usuario es menor al buscado y tiene vidas disponibles se imprime la flecha y se le resta una vida
        elif((num_user < num_random) and (lives > 0)):
            print(" ⬆️ ")
            lives -= 1
            continue    
        else:
            #si acierta el numero se cuentan cuantas vidas le quedaron y segun eso, se suma el dinero que le corresponde
            print("ACERTASTE 😁 , el numero era -> ", num_random)
            if(lives == 5):
                money += 500
            elif(lives == 4):
                money += 400
            elif(lives == 3):
                money += 300
            elif(lives == 2):
                money += 200
            else:
                money += 100
            print(" ")
            #Menú de opciones si quiere seguir jugando o terminar + cuanto dinero acumulado lleva
            print(name," quieres jugar otra partida 😏 ?")
            print("TIENES ACUMULADO $ ", money)
            print("""
                S) seguir jugando
                N) salir del juego""".upper())
            option = input(" ")
            
            print("------------------------------------------------------------------------------------")
            #si decide seguir jugando las vidas se reinician y se genera un nuevo numero aleatorio, caso contrario break, termina el bucle
            if(option == "S" or option=="s"):
                lives = 5
                num_random = random.randint(0, 100)
                continue
            else:
                break
#Dinero total con el que termina el juego
print(name, ", gracias por jugar GUESS THE NUMBER, te retiraste con $", money)




