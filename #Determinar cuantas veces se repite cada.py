#Determinar cuantas veces se repite cada numero en una lista
def num_repite(lista):
    lista_rep=[]
    for i in lista:
        cont=0
        if i not in lista_rep:
            for j in lista:
                if  i==j:
                    cont+=1
                    lista_rep.append(i)
            print(f"El numero {i} se repite {cont}, veces")

        

#lista=[4,1,4,2,3,1,2,3,4,2,1] #1 repite: 3, 2 repite:3, 3 repite:2, 4 repite: 1
lista=[]
cd=int(input("Ingrese cantidad de datos"))
for i in range(cd):
    num=int(input(f"Ingrese el {i+1} dato:"))
    lista.append(num)
num_repite(lista)