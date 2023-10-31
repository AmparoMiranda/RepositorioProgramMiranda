import funcionesTP5

#EJERCICIO 1
dni = int(input("Ingrese su DNI: "))
outcome = funcionesTP5.valid_dni(dni)
print(f"¿El DNI es válido? {outcome}")


#EJERCICIO 2
phrase = input("Ingrese una frase: ").strip()   
print(f"La longitud de la última palabra en la frase '{phrase.upper()}' es de: {funcionesTP5.last_word_length(phrase)+1} carac.")


#EJERCICIO 3
counter = 1
while True:
    print("Ingrese el SOCIO Nº", counter)
    counter += 1
    name = input("***Para salir ingrese ENTER***\nNombre en formato [Nombre1, Nombre2,  Apellido] (sin comas): ").strip()
    if name == "":  
        break

    dni = int(input("DNI: "))

    while (funcionesTP5.valid_dni(dni) == False):   
        dni = int(input("DNI: "))

    print(f"ID -> ", name[0:name.find(' ')], funcionesTP5.last_word_length(name), str(dni)[0:3], sep = " ") 

#EJERCICIO 4
num1 = int(input("Número entero 1: "))
num2 = int(input("Número entero 2: "))
print(f"¿Es {num1} múltiplo de {num2}? {funcionesTP5.multiple_or_not(num1,num2)}")