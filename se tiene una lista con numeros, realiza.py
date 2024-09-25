#se tiene una lista con numeros, realizar con un menu las siguientes acciones, leer l1sta, ordenar lista, obtener may y men de la lista, promedio de los numeros primos y promedio de los fibonaccis


def leerlista():
    l=[7,2,8,4,9,6,2,7,5]
    return l

def ordenarlista(l):
    print("Lista ascendente")
    l.sort()
    print (l)
    print("Lista descendente")
    l.sort(reverse=True)
    print (l)
    
def mayormenor(l):
    print(l)
    print(f"menor lista {min(l)}")
    print(f"mayor lista {max(l)}")
    
def promprimos(l):
    def determinarprimo(l):
        for num in l:
           cd=0
           for divisor in range (1,num+1):
               if num%divisor==0:
                cd+=1
           if cd==2:
               return True      
    sp=0
    cp=0
    for num in l:
        if determinarprimo(num)==True:
            sp+=num
            cp+=1
    if cp>0:
        pp=sp/cp
        print("Promedio primo ", pp)
    else:
        print("No hay primos")
        
def promfibonacci(l):
    a, b = 0, 1
    while b < max(l):
        a, b = b, a + b
    for num in l:
        if num == b:
            cf += 1
            sf += num
        while b < num:
            a, b = b, a + b
        if num == b:
            cf += 1
            sf += num
    if cf == 0:
        print("No hay fibonaccis")
    else:
        promf = sf / cf
        print(f"promedio de los fibonaccis es {promf}")
        
def listasinrep(l):
    lsr=[]
    for num in l:
        b1= num in lsr
        if b1==False:
            lsr.append(num)
    print(l)
    print("lista sin repetidos")
    print(lsr)
    


b=0

while True:
    print(" Menu principal")
    print("-------------------------")
    print(" 1. Leer lista ")
    print(" 1. Odenar lista ")
    print(" 3. Mayor menor de lista")
    print(" 4. Promedio primos")
    print(" 5. Promedio fibonacci")
    print(" 6. Lista sin repetidos")
    print(" 7. SALIR")
    print("-------------------------")
    
    opcion=int(input("Opcion = "))
    if opcion==1:
        l=leerlista()
        b=1
    elif opcion ==2:
        if b==1:
            ordenarlista(l)
        else:
            print("Primero debes leer la lista")
    elif opcion ==3:
        if b==1:
            mayormenor(l)
    elif opcion ==4:
        if b==1:
            promprimos(l)
    elif opcion ==5:
        if b==1:
            promfibonacci(l)
    elif opcion ==6:
        break
    else:
        print("Opcion no valida")

