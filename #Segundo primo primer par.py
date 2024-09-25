#Segundo primo segundo par
import random
def esPar(list):
    pares=[]
    for num in list:
        if num%2==0:
            pares.append(num)
    return pares[2]


def esPirm(list):
    listaprimos=[]
    for num in list:
        cd=0
        for divisor in range (1,num+1):
            if num%divisor==0:
                cd+=1
        if cd==2:
            listaprimos.append(num)
    print("La lista de primos es: ",listaprimos)
    return listaprimos[1]
        
def prom(num1,num2):
    g=num1
    for i in range(num2-1 ):
        g=g+num1 #num1+=num1
        print(g)
    return g

lista=[]
cd=int(input("Ingrese la cantidad de numeros: "))
for  num in range (cd):
    lista.append(random.randint(1,10))
print(f"La lista es: {lista}")

segundo_primo=esPirm(lista)
print("El segundo primo es: ",segundo_primo)

segundopar=esPar(lista)
print("El segundo par es: ",segundopar)

promedio=prom(segundo_primo, segundopar)

print ("La multiplicacion es:",promedio)