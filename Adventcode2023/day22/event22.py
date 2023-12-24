import sys
from time import time
f=open(sys.argv[1],"r")
briques=f.read().strip().split("\n")
f.close()
def recupbrique(briques):
    tmp=[]
    for brique in briques:
        cut=brique.index("~")
        start=brique[:cut].split(",")
        start=tuple(map(int,start))
        end=brique[cut+1:].split(",")
        end=tuple(map(int,end))
        tmp.append((start,end))
    return tmp
def modifbrique():#compresse l'information des briques
    for i in range((len(briques))):
        mod=False
        for i2 in range(3):
            if briques[i][0][i2]<briques[i][1][i2]:
                if i2==0:
                    char="x"
                elif i2==1:
                    char='y'
                else:
                    char='z'
                briques[i]=((briques[i][0]),(char,briques[i][1][i2]-briques[i][0][i2]))
                mod=True
                break 
        if not mod:
            briques[i]=((briques[i][0]),('u'))#u pour unique           
def recupz(briques):#classe les briques par hauteur croissante
    mini=0#impossible de toucher 0
    maxi=0
    tmp=[]
    nbriques=[]
    t=0
    for brique in briques:
        if brique[0][2]>maxi:
            maxi=brique[0][2]
            if mini==0:
                mini=maxi
        elif brique[0][2]<mini:
            mini=brique[0][2]
    while mini<maxi+1:
        for brique in briques:
            if brique[0][2]==mini:
                tmp.append(brique)
        mini+=1
        if len(tmp)!=0:
            nbriques.append(tmp)
            for brique in tmp:
                briques.remove(brique)
        tmp=[]
    return nbriques
def creamatrice():
    matrice=[]
    t=10
    i=0
    tmp=[]
    while i<306:
        while t>0:
            tmp.append([0]*10)
            t-=1
        matrice.append(tmp)
        i+=1
        t=10
        tmp=[]
    return matrice
def remplimatrice(briques) :
    i=1  
    for briquez in briques:#briquez sont les brique a une hauteur z
        z=briquez[0][0][2]-1
        for brique in briquez:
            pos=brique[0]
            long=brique[1]
            if long[0]=="x":
                for x in range(pos[0],pos[0]+long[1]+1):
                    matrice[z][x][pos[1]]=i
            elif long[0]=="y":
                for x in range(pos[1],pos[1]+long[1]+1):
                    matrice[z][pos[0]][x]=i
            elif long[0]=="z":
                for x in range(z,z+long[1]+1):
                    matrice[x][pos[0]][pos[1]]=i
            elif long[0]=="u":
                matrice[z][pos[0]][pos[1]]=i
            i+=1  
def recupxyminmax(briques):
    mini=0#impossible de toucher 0
    maxi=0
    tmp=[]
    nbriques=[]
    t=0
    for brique in briques:
        if brique[0][0]>maxi:
            maxi=brique[0][0]
            if mini==0:
                mini=maxi
        elif brique[0][0]<mini:
            mini=brique[0][0]
    xmin=mini
    xmax=maxi
    mini=0#impossible de toucher 0
    maxi=0
    tmp=[]
    nbriques=[]
    t=0
    for brique in briques:
        if brique[0][1]>maxi:
            maxi=brique[0][1]
            if mini==0:
                mini=maxi
        elif brique[0][1]<mini:
            mini=brique[0][1]
    print(xmin,xmax,'x',mini,maxi,'y')#plus utilisé c'etait pour le recup a la main
def fall():
    for briquez in briques[1:]:#briquez sont les briques a une hauteur z
        print(briquez)
        for brique in briquez:
            z1=briquez[0][0][2]-1
            z2=z1
            pos=brique[0]
            axe=brique[1][0]
            rang=brique[1][1]
            stop=False
            if axe=='x':#on regarde dans le plan y=pos[1]
                y=pos[1]
                while z1>1:
                    z1-=1
                    for x in range(pos[0],pos[0]+rang+1):
                        if matrice[z][x][y]!=0:
                            stop=True
                            for x in range(pos[0],pos[0]+rang+1):
                                matrice[z2][x][y]=0    

                    



            
start=time()
briques=recupbrique(briques)
modifbrique()#compression
briques=recupz(briques)#tri par hauteur
matrice=creamatrice()
remplimatrice(briques)
print(time()-start)
fall()