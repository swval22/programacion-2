#Determinar cual es el dato que mas se repite
def numeros_repiten(lista): #Funcion para contar los numeros que se repiten en una lista
    lista_repetidos=[] #lista que guarde repetidos para evitar realizar el ciclo nuevamente 
    contadoresr=[]
    for i in lista: #ciclo para recorrer la lista
        c=0
        
        if i not in lista_repetidos:
            for j in lista: #ciclo para contar los numeros repetidos
                if i==j:
                    c+=1
                    
                    lista_repetidos.append(i) #agregar el numero repetido a la lista
            contadoresr.append(c)
    return contadoresr
                    

def cont_mayor(contadoresr, lista_repetidos):
    for i in contadoresr:
        if i==max(contadoresr):
            numas= lista_repetidos[i]
            print(numas)
    return numas

def lista_repiten(lista): #Funcion para contar los numeros que se repiten en una lista
    lista_repetidos=[] #lista que guarde repetidos para evitar realizar el ciclo nuevamente 
    contadoresr=[]
    for i in lista: #ciclo para recorrer la lista
        c=0
        
        if i not in lista_repetidos:
            for j in lista: #ciclo para contar los numeros repetidos
                if i==j:
                    c+=1
                    
                    lista_repetidos.append(i) #agregar el numero repetido a la lista
    return lista_repetidos


lista=[1,2,3,1,2,3,4,2,1,1,1]#El numero que mas se repite en esta lista es 1
print(numeros_repiten(lista)) #imprimir la lista de contadores de repetidos
print(lista_repiten(lista))
repetidoss=lista_repiten(lista)
contadoresx= numeros_repiten(lista)
nummas= cont_mayor(contadoresx, repetidoss)
print(nummas)