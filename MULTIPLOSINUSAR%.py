def es_multiplo(a, b):
    if b == 0:
        return False
    if a == 0:
        return True
    contador = 0
    while contador <= a:
        if contador == a:
            return True
        contador += b
    return False
if es_multiplo(12, 3):
    print("si")
else:
    print("no")