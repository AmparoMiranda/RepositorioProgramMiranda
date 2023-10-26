#Ejercicio 1
word = input("Ingrese una palabra que sera mostrada 10 veces: ")
for i in range(10):
    print(word)

#Ejercicio 2
age = int(input("Ingrese su edad: "))
for i in range(1, age + 1):
    print(i)

#Ejercicio 3
num = int(input("Escriba un numero entero positivo:"))
for i in range(1, num + 1):
    if(i % 2 != 0):
        print(i, end = ",")
        
print("")

#Ejercicio 4
num=int(input("Escriba un numero entero positivo: "))
for i in range(num,-1,-1):
    print(i, end = ",")