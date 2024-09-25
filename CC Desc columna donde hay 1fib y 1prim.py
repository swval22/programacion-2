def primo(num):
        cd=0
        for divisor in range (1,num+1):
            if num%divisor==0:
                cd+=1
        if cd==2:
            return True
        else:
            return False
    
def fibonacci(dato):
    a=0
    b=1
    t=0
    if  dato==1:
        return True
    while t < dato:
        t=a+b
        a=b
        b=t
    if t==dato:
        return True
    else:
        return False
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

for fila in nuevamat:
    b1=0
    b2=0
    for dato in fila:
        if primo(dato):
            b1+=1
        elif fibonacci(dato):
            b2+=1
    if b1>=1 and b2>=1:
        lista=fila
    break
        
def ordenarlistades(lista):
    for i in range(len(lista)-1):
        for j in range(len(lista)-i-1):
            if lista[j] < lista[j+1]:
                aux=lista[j]
                lista[j]=lista[j+1]
                lista[j+1]=aux
    print(lista)
ordenarlistades(lista)
