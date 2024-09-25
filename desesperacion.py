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

def primo_may(diccionario):
    for clave, valor in diccionario.items():
        b=0
        for dato in valor:
            if primo(dato):
                primoMay=dato
                b=1

        if b==1:
            for clave,valor in diccionario.items():
                for dato in valor:
                    if primo(dato) and dato > primoMay:
                        primoMay=dato
                        clave_primo=clave
    print(f"El primo mayor es {primoMay} con clave {clave_primo}")
    ##return primoMay, fibMenor
    
def fib_men(diccionario):
    for clave, valor in diccionario.items():
        b=0
        for dato in valor:
            if fibonacci(dato):
                fibMenor=dato
                b=1
        if b==1:
            for dato in valor:
               if fibonacci(dato) and dato < fibMenor:
                  fibMenor=dato
                  clave_fib=clave
    print(f"El fibonacci menor es {fibMenor} con clave {clave_fib}")
     
diccionario={1:[2,1,5,6],2:[4,2,1,5],3:[7,1,8,2],4:[9,1,3,6]}
#primoMay,fibMenor=primo_may_fib_men(diccionario)
# primo_may_fib_men(diccionario)

fib_men(diccionario)
primo_may(diccionario)
