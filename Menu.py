def funcionpunto3():
     pass

def funcionpunto4():
    def columnasdematz(matriz):
        col=[]
        mat=[]
        for fila in matriz:
            c=0
            for dato in fila:
             c+=1
             pos=c
             col = [fila[pos-1] for fila in matriz]
             if col not in mat:
                  mat.append(col)
        return  mat
    m=[[4,7,8,9],[2,3,6,5],[8,23,6,4],[10,6,3,4]]
    diccionario={}
    nuevamat=columnasdematz(m)
    sumas=[]
    for fila in nuevamat:
      sum=0
      for dato in range(len(fila)):
            sum=sum + fila[dato]
            sumas.append(sum)
    print(sumas)
    for i in range(len(sumas)):
        diccionario[sumas[i]] = nuevamat[i]
    print(diccionario)
    clavespares=[]
    for clave,valor in diccionario.items():
         if clave%2==0:
              clavespares.append(clave)


def parcial_1():
    print("Escoge entre el punto 3 y 4 del primer parcial")
    opcion = int(input("Ingresa  el número del punto: "))
    if opcion == 3:
         funcionpunto3()
    elif opcion == 4:
         funcionpunto4()
    
def parcial_2():
    pass

def parcial_3():
    pass


print(" Menu principal")
print("-------------------------")
print(" 1. PRIMER PARCIAL ")
print(" 2. SEGUNDO PARCIAL ")
print(" 3. TERCER PARCIAL")
print(" 4. Exit")
print("-------------------------")

opcion=int(input("Opcion = "))
if opcion==1:
    parcial_1()
elif opcion ==2:
    parcial_2()      
elif opcion ==3:
    parcial_3()
elif opcion ==4:
    exit
else:
        print("Opcion no valida")
