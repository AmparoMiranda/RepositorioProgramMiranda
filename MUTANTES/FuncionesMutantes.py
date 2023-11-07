def is_mutant(dna):

    count = 0
    for i in range(6):
        for j in range(6):
            # Obtengo letra
            letter = dna[i][j]
            # Busco secuencia horizontal
            if j < 3 and letter == dna[i][j+1] == dna[i][j+2] == dna[i][j+3]:
                count += 1
            # Busco secuencia vertical 
            if i < 3 and letter == dna[i+1][j] == dna[i+2][j] == dna[i+3][j]:
                count += 1
            # Busco secuencia diagonal DESCENDENTE 
            if i < 3 and j < 3 and letter == dna[i+1][j+1] == dna[i+2][j+2] == dna[i+3][j+3]:
                count += 1
            # Busco secuencia diagonal ASCENDENTE 
            if i > 2 and j < 3 and letter == dna[i-1][j+1] == dna[i-2][j+2] == dna[i-3][j+3]:
                count += 1
    if count > 1:
        return True
    else:
        return False