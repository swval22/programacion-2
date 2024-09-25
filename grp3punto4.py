m=[[4,7,8,9],[2,3,6,5],[8,23,6,4],[10,6,3,4]]
diccionario={}
claves=[]
for fila in m:
    mayor=None
    for dato in fila:
        if  mayor is None or dato>= mayor:
            mayor = dato
    claves.append(mayor)
    
for i in range(len(claves)):
    diccionario[claves[i]] = m[i]
print(diccionario)
sumasdevalores=[]
for clave,valor in diccionario.items():
    suma=0
    for dato in valor:
        suma=suma+dato
    sumasdevalores.append(suma)
print(sumasdevalores)
mayorrr=None
cc=0
poss=0
for dato in sumasdevalores:
    cc+=1
    if  mayorrr is None or dato>= mayorrr:
        mayorrr = dato
    if dato==mayorrr:
        poss=cc
ccd=0
for clave,valor in diccionario.items():
    ccd+=1
    if  ccd==poss:
        print(clave,valor)

        
