#Ejercicio 1
letters = int(input("Ingrese la cantidad de letras a correr: "))
position = 0
message1 = input("Mensaje 1: ").lower()
message2 = input("Mensaje 2: ").lower()
message3 = input("Mensaje 3: ").lower()
message4 = input("Mensaje 4: ").lower()
message5 = input("Mensaje 5: ").lower()

messages = [message1, message2, message3, message4, message5]

alph_list = 'abcdefghijklmnñopqrstuvwxyz'
for i in messages:
    print(" ")
    for l in i:
        if l in alph_list:
            position = alph_list.index(l)
            position = (position+letters) % 27
            print(alph_list[position],end = "")
        else:
            print(l, end = "")
print(" ")
print("-----------------------")

#Ejercicio 2
even_total = 0
odd_total = 0
while(True):
    even = 0
    odd = 0 
    num = int (input("Ingrese numeros positivos (para terminar ingrese 0): "))
    if (num == 0):
        break
    elif (num < 0):
        continue
    else:
        while(num > 0):
            dig = num % 10 
            num = num // 10
            if (dig % 2 == 0):
                even += 1
            else:
                odd += 1
    print("Pares: ", even)
    even_total += even
    print("Impares: ", odd)
    odd_total += odd

print("En total, los numeros pares son: ", even_total)
print("En total, los numeros impares son: ", odd_total)

