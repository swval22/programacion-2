""" 
Se tiene una cantidad de numeros dada, encontrar los tres
primeros fibonacci de acuerdo al orden de entrada y determinar
el promedio de los numeros pares que estan entre el mayor y el meno de
estos fibonacci. sin usar listas
"""

def fibonacci(dato):
    a=0
    b=1
    t=0
    while t < dato:
        t=a+b
        a=b
        b=t
    if t==dato:
        return True
    else:
        return False
    
def par(dato):
    if dato%2==0:
        return True
    else:
        return False

def tresFibonaccis():
    cd = int(input("Ingrese la cantidad de datos"))
    f1=0
    f2=0
    f3=0
    b=0
    for i in range(cd):
        dato = int(input("Ingrese un número: "))
        if fibonacci(dato):
            b+=1
            if b==1:
                f1=dato
            elif b==2:
                f2=dato
            elif b==3:
                f3=dato
    return f1,f2,f3

def mayor(dato1,dato2,dato3):
    if dato1 >= dato2 and dato1 >= dato3:
        datomayor=dato1
    elif dato2 >= dato1 and dato2 >= dato3:
        datomayor=dato2
    else:
        datomayor=dato3
    return datomayor

def menor(dato1,dato2,dato3):
    if dato1 <= dato2 and dato1 <= dato3:
        datomenor=dato1
    elif dato2 <= dato1 and dato2<= dato3:
        datomenor=dato2
    elif dato3 <= dato1 and dato3 <= dato2:
        datomenor=dato3
    return datomenor
    
def pares(men,mayor):
    sum=0
    cont=0
    while men<=mayor:
        if par(men):
            sum=sum+men
            cont+=1
            men+=1
        else:
            men+=1
    promedio=sum/cont
    print(f"El promedio de los pares es {promedio}")
    
fib1,fib2,fib3=tresFibonaccis()
datomayor=mayor(fib1,fib2,fib3)
datomenor=menor(fib1,fib2,fib3)

pares(datomenor,datomayor)
            
            
    
