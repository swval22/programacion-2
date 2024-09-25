def swap_filas(matrix):
    n = len(matrix)
    fila_max_primo = -1
    fila_min_primo = -1
    max_primo = -1
    min_primo = 1000000

    for i in range(n):
        for j in range(n):
            if es_primo(matrix[i][j]):
                if matrix[i][j] > max_primo:
                    max_primo = matrix[i][j]
                    fila_max_primo = i
                elif matrix[i][j] < min_primo:
                    min_primo = matrix[i][j]
                    fila_min_primo = i

    for j in range(n):
        matrix[fila_max_primo][j], matrix[fila_min_primo][j] = matrix[fila_min_primo][j], matrix[fila_max_primo][j]

    return matrix

def es_primo(num):
    if num <= 1:
        return False
    for i in range(2, int(num / 2) + 1):
        if num % i == 0:
            return False
    return True

#-----------------------------------------------------------------------------------------------------------------
def swap_filas(matrix, i, j): #i y j indices de las filas
    n = len(matrix)
    for k in range(n):
        matrix[i][k], matrix[j][k] = matrix[j][k], matrix[i][k]
    return matrix