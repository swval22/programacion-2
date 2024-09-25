def columnasdematz(matriz):
    col=[]
    mat=[]
    for fila in matriz:
        c=0
        for dato in fila:
            c+=1
            pos=c
            col = [fila[pos-1] for fila in matriz]
            if col not in mat:
                mat.append(col)
    return mat
    
m=[[4,7,8,9],[2,3,6,5],[8,23,6,4],[10,6,3,4]]
nuevamat=columnasdematz(m)
sumas=[]
for fila in nuevamat:
    sum=0
    for dato in range(len(fila)):
        sum=sum + fila[dato]
    sumas.append(sum)
print(sumas)
mayor=None
ct=0
for i in sumas:
    ct+=1
    if  mayor is None or i>= mayor:
        mayor = i
        pos=ct
print(mayor,pos)
list=nuevamat[pos-1]
print(list)
def ordenarlistades(list):
    for i in range(len(list)-1):
        for j in range(len(list)-i-1):
            if list[j] < list[j+1]:
                aux=list[j]
                list[j]=list[j+1]
                list[j+1]=aux
    print(list)
ordenarlistades(list)