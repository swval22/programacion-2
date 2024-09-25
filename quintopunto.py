def primo(num):
        cd=0
        for divisor in range (1,num+1):
            if num%divisor==0:
                cd+=1
        if cd==2:
            return True
        else:
            return False
print("hols")        
def tercerprimo():
    cd = int(input("Ingrese la cantidad de datos"))
    prim3=0
    cont=1
    c=0
    for i in range (cd):
        num = int(input("Ingrese un número: "))
        if primo(num):
            c+=1
            if c==3:
                prim3=num
        if num==prim3:
            cont+=1
    return cont

numero=tercerprimo()
c=0
for i in range (10):
    c+=1
    mult=numero*c
    print(mult)