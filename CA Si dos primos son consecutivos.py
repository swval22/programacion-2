def primo(num):
        cd=0
        for divisor in range (1,num+1):
            if num%divisor==0:
                cd+=1
        if cd==2:
            return True
        else:
            return False

cd = int(input("Ingrese la cantidad de datos"))
primo1=0
primo2=0
c=0
for i in range(cd):
    dato = int(input("Ingrese un número: "))
    if primo(dato):
        c+=1
        if c==2:
            primo1=dato
        elif c==4:
            primo2=dato
dif=0
if primo1>primo2:
    primo1=primo2
    primo2=primo1
cont=0
for num in range(primo1+1,primo2):
    if primo(num):
        cont+=1
if cont >=1:
    print("no son consecutivos")
else:
    print("son consecutivos")
