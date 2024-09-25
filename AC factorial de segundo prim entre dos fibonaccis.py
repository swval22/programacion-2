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

def ranfib(list):
    c=0
    for i in list:
        if fibonacci(i):
            c+=1
            if c==2:
                fib1=i
            elif c == 3:
                fib2=i
    return fib1,fib2

def primodos(list, n1, n2):
    if n1>n2:
        n1,n2=n2,n1
    c=0
    for i in range(list[n1],n2+1):
        if primo(i):
            c+=1
            if c==2:
                return i
    return i

def factorial(num):
    multiplicador=num
    c=0
    cont=num
    while c < num-1:
        multiplicador = multiplicador - 1
        cont = cont * multiplicador
        c+=1
    return cont        
   
        
l1=[2,8,1,4,4,6,1]
l2=[7,4,5,8,7,3,5,11,5]

fib1,fib2 = ranfib(l1)

num=primodos(l2,fib1,fib2)

print(f"El numero factorial es: {factorial(num)}")
