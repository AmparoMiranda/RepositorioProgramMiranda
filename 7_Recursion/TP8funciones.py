def return_digits(n, quant = 1):
    if n < 10:  #caso base: si el número es o llega a ser de 1 dígito...
        return quant    #se retorna la cantidad final (en el caso de que se ingrese un número de 1 dígito, se retorna el valor inicial que es 1)
    else:
        return return_digits(n//10, quant+1)

def validate_power(n,b, counter = 1):
    if n < b:   #caso base: si n es menor que b entonces no puede ser la potencia, retorna false
        return False
    elif n == b:    #si o cuando (n) y (b) son iguales, se retorna true ya que sí es potencia, y se retorna el contador de potencias 
        return True, counter
    else:   #mientras (n) sea mayor a (b), se llama a la función, dividiendo a (n) por (b) e incrementando el contador de potencias
        return validate_power(n//b, b, counter+1)

def return_positions(phrase,substring, ind = 0):    #se le agrega otro parámetro a la función, un indice para que siempre se retorne la posición correcta aunque phrase se vaya acortando
    if not phrase or len(phrase) < len(substring):  # caso base: si phrase está vacío o es más corto que substring, se retorna un vacío
        return []
    
    elif phrase[:len(substring)] == substring:  # si el primer segmento de phrase es igual a substring
        return [ind] + return_positions(phrase[len(substring):], substring, ind+len(substring))   # se agrega la posición actual (0) a la lista de resultados y se llama a la función con el resto de phrase, el substring y el nuevo índice
    
    else:   #si el primer segmento de phrase no es igual a substring
        return return_positions(phrase[1:], substring, ind+1)   # se llama a la función con el resto de phrase, el substring y el índice de la posición siguiente en la frase