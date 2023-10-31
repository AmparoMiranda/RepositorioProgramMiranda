def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers


#Ejercicio 1
numbers= []
input("Ingrese 5 numeros enteros, deje el primer espacio vacio: ")
for i in range(5):
    number = int(input())
    numbers.append(number)
print("Lista sin ordenar: ", numbers)
print("Lista ordenada en forma ascendente: ", bubble_sort(numbers))


def selection_sort(words):
    length = len(words)  
    for i in range(length - 1):  
        min_index = i  
        for j in range(i + 1, length):  
            if words[j] < words[min_index]:  
                min_index = j  
        
        words[i], words[min_index] = words[min_index], words[i]  
    return words

#Ejercicio 2
words= []
input("Ingrese 5 palabras, deje el primer espacio vacio:")
for i in range(5):
    word = input()
    words.append(word)
print("Lista desordenada:", words)
result = selection_sort(words)
print("Lista ordenada en forma ascendente:", result)

#Ejercicio 4
def insertion_sort(orations):
    for i in range(1, len(orations)):
        key = orations[i]
        j = i - 1
        while j >= 0 and len(orations[j]) > len(key):
            orations[j + 1] = orations[j]
            j -= 1
        orations[j + 1] = key
    return orations

orations= []
input("Ingrese 5 oraciones, deje el primer espacio vacio:")
for i in range(5):
    oration = input()
    orations.append(oration)
print("Lista desordenada:",orations)
result = insertion_sort(orations)
print("Lista ordenada en forma ascendente:",result)