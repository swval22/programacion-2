#hallar un fibonacci que sea tambien primo, siendo el segundo fib de la columna del primo mayor
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
    
m=[[4,7,8,9],[2,3,6,5],[8,23,6,4],[10,5,3,4]]
nuevamat=columnasdematz(m)

primayor=None
columnaprimay=[]
ct=0
pos=0
for fila in nuevamat:
    ct+=1
    for dato in fila:
        if primo(dato):
            if primayor is None or dato>= primayor:
                primayor=dato
        if dato==primayor:
            pos=ct
columnaprimay=nuevamat[pos-1]
c=0
for dato in columnaprimay:
    if fibonacci(dato):
        c+=1
        if c==2:
            if primo(dato):
                print(dato)
