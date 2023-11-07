
from FuncionesMutantes import*

print("    👽  <MAGNETO ESTÁ RECLUTANDO MUTANTES PARA LUCHAR CONTRA LOS X-MENS>  👽    ")
print("")
print("    🧬  Realiza este test de ADN y descubre si puedes ser parte de esta lucha 🧬    ")
print("----------------------------------------------------------------------------------------------------------------------")
print("Ingrese los valores de la matriz de ADN de 6x6, separados por comas y sin espacios. Las letras deben ser A, T, C o G.")
dna = []

for i in range(6):
  while(True):
    row = input(f"Ingrese la fila {i+1}: ")
    row = row.upper()
    row = row.split(",")
    # Verifico que la fila tenga 6 elementos
    if len(row) != 6:
      valid = False
    # Verifico que los valores sean válidos
    valid = True
    for letter in row:
      if letter not in ["A", "T", "C", "G"]:
        print("La letra debe ser A, T, C o G.")
        valid = False
        continue
    # Si la fila es válida la agrego a la matriz
    if valid:
      dna.append(row)
      break
    else:
      print("La fila debe tener 6 elementos.")
      print("Las letras deben ser A, T, C o G.")
      continue

print("----------------------------------------------------------------------------------------------------------------------")

# Matriz válida -> aplico la función y muestro el resultado
result = is_mutant(dna)
if result:
  print("👽  El ADN ingresado pertenece a un MUTANTE  👽")
  print(" ")
  print("😁  ¡Bienvenido a la hermandad de mutantes liderada por Magneto!  😁")
else:
  print("Lo siento, el ADN ingresado no es de un mutante.")
  print("Mejor vete con los X-mens😡")



