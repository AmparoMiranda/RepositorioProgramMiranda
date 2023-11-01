def validator_card(item, card, row):
    
    if item in row:
        return True

    for row in card:
        for num in row:
            if item == num: # Numero repetido 
                return True


def random_validator(num, matrix):
    for i in range(0,5):
        row = matrix[i]
        for j in range(0,5):
            if num == row[j]: 
                print("-------------")
                print(f"MATCH CON {num}")
                row[j] = "X"

                #Imprimir carton
                for row in matrix:
                    print(row)
                print("-------------")
                return matrix 
            
    return matrix 


def row_validator(matrix):
    # Buscar coincidencia linea vertical
    for i in range(0,5):
        row = matrix[i]  
        match = True
        for j in range(0,5):  
            if row[j] != "X":
                match = False  

        if match:
            return True
        else:
            continue
    return False


def column_validator(matrix):
    # Buscar coincidencia linea horizontal
    for column in range(0, 5):  
        match = True
        for row in matrix: 
            if row[column] != "X":
                match = False  

        if match:
            return True
        else:
            continue
    return False


def diagonal_validator(matrix):
    # Buscar coincidencia en diagonal principal
    match = True
    for i in range(0, 5):
        row = matrix[i] 
        if row[i] != "X": 
            match = False  

        if not match:
            return False
        
    return True
