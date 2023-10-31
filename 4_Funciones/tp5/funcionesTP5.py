#Ejercicio1
def valid_dni(dni):
    #dni a string para contar la longitud
    if len(str(dni)) < 7 or len(str(dni)) > 8:   
        return False  #el dni no está entre 7 y 8, no es válido -> retorna falso
    else:
        return True
    
#Ejercicio 2  
def last_word_length(phrase):
    #volteo la frase para encontrar más rapido la última palabra
    phrase = phrase[::-1]   
    #extraigo la última palabra y saco la longitud
    word_length = len(phrase[:phrase.find(" ")])   
    return word_length

#Ejercicio 4
def multiple_or_not(num1,num2):
    if num1 % num2 == 0:
        return True
    else:
        return False