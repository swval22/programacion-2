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
print("hola")
def columna_fibmenor(matriz):
    col=[]
    fibmenor=None
    for fila in matriz:
        c=0
        for dato in fila:
            c+=1
            if fibonacci(dato)==True:
                if fibmenor is None or dato<= fibmenor:
                    fibmenor=dato
            if dato==fibmenor:
                pos=c
    col = [fila[pos-1] for fila in matriz]
    return col
                        
def columna_primayor(matriz):
    col=[]
    primomay=None
    for fila in matriz:
        c=0
        for dato in fila:
            c+=1
            if primo(dato)==True:
                if primomay is None or dato>= primomay:
                    primomay=dato
            if dato==primomay:
                pos=c
    col = [fila[pos-1] for fila in matriz]
    return col

def ordenarlistasc(list):
    for i in range(len(list)-1):
        for j in range(len(list)-i-1):
            if list[j] > list[j+1]:
                aux=list[j]
                list[j]=list[j+1]
                list[j+1]=aux
    print(list)
    
def ordenarlistades(list):
    for i in range(len(list)-1):
        for j in range(len(list)-i-1):
            if list[j] < list[j+1]:
                aux=list[j]
                list[j]=list[j+1]
                list[j+1]=aux
    print(list)

m=[[4,7,8,9],[2,3,6,5],[8,23,6,4],[10,6,3,4]]

l2=columna_fibmenor(m)
l1=columna_primayor(m)
print(l1)
ordenarlistasc(l1)
print(l2)
ordenarlistades(l2)

