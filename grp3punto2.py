def primo(num):
        cd=0
        for divisor in range (1,num+1):
            if num%divisor==0:
                cd+=1
        if cd==2:
            return True
        else:
            return False

def multiplicar(a, b):
    result = 0
    for i in range(b):
        result += a
        
    return result

lista=[4,4,3,5,6]
fib1=0
fib2=0

for i in range(len(lista)):
    if primo(lista[i]):
        if i > 0:
            fib1 = lista[i - 1]
        else:
            print("No hay dato a la izquierda")
        if i < len(lista) - 1:
            fib2 = lista[i + 1]
        else:
            print("No hay dato a la derecha")
        break
resultado=multiplicar(fib1,fib2)
print(resultado)