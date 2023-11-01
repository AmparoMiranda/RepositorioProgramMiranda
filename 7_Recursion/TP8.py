from TP8funciones import*

#EJERCICIO 1
number = int(input("Ingrese un número positivo: "))
print(f"{number} tiene {return_digits(number)} dígito/s")

#EJERCICIO 2
n = int(input("Ingrese un número: "))
b = int(input("Ingrese otro número: "))
result = validate_power(n,b)
if result == False:
    print(f"¿Es {n} potencia de {b}? {result}")
else:
    print(f"¿Es {n} potencia de {b}? {result[0]} -> {b} ^ {result[1]} = {n}")

#EJERCICIO 3
phrase = input("Ingrese una frase: ")
substring = input("Ingrese una cadena a buscar: ")
print(return_positions(phrase,substring))