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
    
def buscar_primos(matriz):
    listaPirmos=[]
    cont=0
    for i in matriz:
        for j in i:
            if primo(j) is True:
                cont+=1
                listaPirmos.append(j)
                if cont==2:
                    return listaPirmos
    #None
    print("No hay suficientes primos, se termina el ejercicio")
    return None

def buscar_fibonaccis(vector,listaprimos):
    cont=0
    for index in range(listaprimos[0],listaprimos[1]):
        num=vector[index]
        if  fibonacci(num) is True:
            cont+=1
            if  cont==2:
                print(f"El segundo fibonacci es: {num}, en la posicion {index}")

v=[2,3,1,4,5,6,2,3,4]
m=[[2,4,6],[8,7,9],[4,6,2]]

listaprimos=buscar_primos(m)
if listaprimos is not None:
    buscar_fibonaccis(v,listaprimos)
