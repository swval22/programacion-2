# 3.Se tiene un diccionario con la siguiente información
#Clave numero entero
#Valor lista de números
#Formar dos conjuntos asi:
#Conjunto 1 con los número pares de la lista valor de aquellas claves que son primos 
#Conjunto 2 con los número pares de la lista valor de aquella claves que son fibonacci
#Con estos dos conjuntos formar dos cadenas
#Cadena1 con los pares comunes
#Cadena2 con la unión de los pares sin elementos comunes

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

def paresdeprim(diccionario):
    conjunto1=set()
    for clave, valor in diccionario.items():
        if primo(clave):
            for num in valor:
                if par(num):
                    conjunto1.add(num)
    return conjunto1
    
def paresdefib(diccionario):
    conjunto2=set()
    for clave,valor in diccionario.items():
        if fibonacci(clave):
            for num in valor:
                if par(num):
                    conjunto2.add(num)
    return conjunto2

diccionario={8:[2,1,5,6],7:[4,2,1,5],21:[7,1,8,2],17:[9,1,3,6]}

cj1=set()
cj2=set()

cj1=paresdeprim(diccionario)
cj2=paresdefib(diccionario)

print(cj1)
print(cj2)

cd1=cj1.intersection(cj2)
cd2=cj1.symmetric_difference(cj2)

print(cd1)
print(cd2)