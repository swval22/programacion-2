#formar diccionario con los numeros primos y sus numeros de al lado
def primo(num):
        cd=0
        for divisor in range (1,num+1):
            if num%divisor==0:
                cd+=1
        if cd==2:
            return True
        else:
            return False

def sacarprimosdelistas(list1,list2):
    primos=[]
    alado=[]
    for i in range(len(list1)):
        if primo(list1[i]) or list1[i]==1:
            primos.append(list1[i])
            if i > 0:
                alado.append([list1[i-1], list1[i+1]])
            else:
                alado.append([None, list1[i+1]])
    for i in range(len(list2)):
        if primo(list2[i]) or list2[i]==1:
            primos.append(list2[i])
            if i > 0:
                alado.append([list2[i-1], list2[i+1]])
            else:
                alado.append([None, list2[i+1]])
    return primos, alado

l1=[4,3,6,7,3,10]
l2=[6,1,4,5,4,4]
d={}
claves,valores=sacarprimosdelistas(l1,l2)
for i in range (len(claves)):
    d[claves[i]]=valores[i]
print(d)

clavemayor=None
for clave,valor in d.items():
    if clavemayor is None or clave>=clavemayor:
        clavemayor=clave
print(clavemayor,d[clavemayor])