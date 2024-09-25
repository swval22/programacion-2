#NUMEROS SOBRE Y BAJO LA DIAGONAL PRINCIPAL---------------------------
def avg_diagonal(matrix):
    n = len(matrix)
    sum_below = 0
    sum_above = 0
    count_below = 0
    count_above = 0

    for i in range(n):
        for j in range(n):
            if i > j:
                sum_below += matrix[i][j]
                count_below += 1
            elif i < j:
                sum_above += matrix[i][j]
                count_above += 1

    avg_below = sum_below / count_below
    avg_above = sum_above / count_above

    return avg_below, avg_above

#NUMEROS SOBRE Y BAJO LA DIAGONAL SECUNDARIA---------------------------

def avg_secundaria(matrix):
    n = len(matrix)
    sum_below_secundaria = 0
    sum_above_secundaria = 0
    count_below_secundaria = 0
    count_above_secundaria = 0

    for i in range(n):
        for j in range(n):
            if i + j < n - 1:
                sum_below_secundaria += matrix[i][j]
                count_below_secundaria += 1
            elif i + j > n - 1:
                sum_above_secundaria += matrix[i][j]
                count_above_secundaria += 1

    avg_below_secundaria = sum_below_secundaria / count_below_secundaria
    avg_above_secundaria = sum_above_secundaria / count_above_secundaria

    return avg_below_secundaria, avg_above_secundaria

#PROM DIAGONAL PRINCIPAL Y SECUNDARIA ---------------------
def avg_diagonales(matrix):
    n = len(matrix)
    sum_principal = 0
    sum_secundaria = 0
    count_principal = 0
    count_secundaria = 0

    for i in range(n):
        for j in range(n):
            if i == j:
                sum_principal += matrix[i][j]
                count_principal += 1
            elif i + j == n - 1:
                sum_secundaria += matrix[i][j]
                count_secundaria += 1

    avg_principal = sum_principal / count_principal
    avg_secundaria = sum_secundaria / count_secundaria

    return avg_principal, avg_secundaria

