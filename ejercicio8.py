cd=int(input("dijite cantidad de datos "))
ln=[]
for i in range(cd):
    ln.append(int(input(f"dijite el dato [{i}]")))

lp=[]

for i in range (cd):
    cand=0
    for c in range(1,ln[i]+1):
        if ln[i]%c==0:
            cand=cand+1
    if cand==2:
        lp.append(ln[i])           

pmenor=lp[0] 
posmenor=0
pmayor=lp[0]
posmayor=0

for j in range (len(lp)):
    if lp[j]<pmenor:
        pmenor=lp[j]
        posmenor=j
    if lp[j]>pmayor:
        pmayor=lp[j]
        posmayor=j


if posmenor< posmayor:
    parmenor=0
    for i in range(pmenor,pmayor):
        if ln[i]%2==0:
            parmenor=ln[i]
            

if posmayor<posmenor:
    parmenor=0 
    for i in range(pmayor,pmenor):
        if ln[i] %2==0:
            parmenor==0
    
      
    
print(f"en el rango de {pmenor} y {pmayor} esta el par menor {parmenor}")


