import random
import time
from FuncionesBingo import *
print("BIENVENIDOS AL BINGO, 🚫 PROHIBIDO JUGAR SI SOS MENOR DE 60 🚫")
#Ejercicio bingo en clase
while True:
    card = []

    for i in range(0, 5):
        row = []
        for j in range(0, 5):
            while True:
                num = int(input(f"Ingrese numero para fila {i+1} columna {j+1}: "))
                if num < 0 or num > 75:
                    print("Error: Fuera de rango")
                    continue
                
                if validator_card(num,card,row):
                    print("Error: Valor repetido en el carton")
                    continue
                row.append(num)
                break
        card.append(row)
        print(f"Fila añadida: {row}")

    game_numbers= []

    while True:
        time.sleep(0.25)
        #Numero al azar
        random_num = random.randint(1,75)

        if random_num in game_numbers: 
            continue
        else:
            print(f"Numero: {random_num}")
            game_numbers.append(random_num)
            card = random_validator(random_num, card)

            if row_validator(card):
                print("Ganaste horinzontalmente🎊🎊🎊")
                break

            if column_validator(card):
                print("Ganaste verticalmente🎊🎊🎊")
                break

            if diagonal_validator(card):
                print("Ganaste por diagonal🎊🎊🎊")
                break
    choice = input("Desea jugar nuevamente? Ingrese s/n: ").upper()
    if choice == "N":
        break