from TP6funciones import*

#EJERCICIO 1
print("Ingrese nums. Para salir ingrese 0")
num_array = []

while True:
    num = int(input())
    if num == 0:
        break

    num_array.append(num)

show_array(num_array)

#EJERCICIO 2
number = int(input("Ingrese un número a remover en la lista: "))
if number in num_array:
    num_array.remove(number)
else:
    print(f"{number} no se encuentra en la lista")

show_array(num_array)

#EJERCICIO 3
summation = 0
for n in num_array:
    summation += n

print("\nSumatoria de la lista: ", summation)