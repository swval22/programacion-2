def par(dato):
    if dato%2==0:
        return True
    else:
        return False

def sacarparesyrepetidos(list1,list2):
    pares=[]
    repiten=[]
    for dato in list1:
        if par(dato)== True:
            if dato not in pares:
                pares.append(dato)
    for dato in list2:
        if par(dato)== True:
            if dato not in pares:
                pares.append(dato)
    for i in pares:
        c=0
        for j in list1:
            if i==j:
                c+=1
        for n in list2:
            if i==n:
                c+=1
        repiten.append(c)
    return pares, repiten
    
l1=[6,6,5,2,4,8]
l2=[4,6,9,6,7,7]

lpares,lvecesrepiten=sacarparesyrepetidos(l1,l2)

d={}   
for i in range(len(lpares)):
    d[lpares[i]] = lvecesrepiten[i]
print(d)
mayorvalor=None
for clave,valor in d.items():
    if mayorvalor is None or valor>=mayorvalor:
        mayorvalor=valor
    if valor == mayorvalor:
        print(f"El valor que mas se repite es {clave}, se repite {mayorvalor} veces")
    
