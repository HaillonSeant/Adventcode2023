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
    for brique in briques:
        if brique[0][1]>maxi:
            maxi=brique[0][1]
            if mini==0:
                mini=maxi
        elif brique[0][1]<mini:
            mini=brique[0][1]
    print(xmin,xmax,'x',mini,maxi,'y')#plus utilisé c'etait pour le recup a la main
def creadico():#dico des briques (quelle brique elle soutienne et combien la soutienne)
    dicobriques={}
    for i in range(1,1301):#1300 briques
        dicobriques[i]=[set(),0]
    return dicobriques 
def fall():
    for briquez in briques[1:]:#briquez sont les briques a une hauteur z
        z1=briquez[0][0][2]-1
        for brique in briquez:
            z2=z1-1
            pos=brique[0]
            axe=brique[1][0]
            bid=matrice[z1][pos[0]][pos[1]]#id de la brique etudie
            run=True
            stopfall=False
            if axe=='x':#on regarde dans le plan y=pos[1]
                rang=brique[1][1]
                y=pos[1]
                while run:
                    for x in range(pos[0],pos[0]+rang+1):
                        if matrice[z2][x][y]!=0:
                            for i in range(pos[0],pos[0]+rang+1):#suprime ancienne pos et cree nouvelle pos
                                matrice[z1][i][y]=0
                                matrice[z2+1][i][y]=bid
                            stopfall=True
                            break
                    if stopfall:
                        run=False
                        lid=0
                        for x in range(x,pos[0]+rang+1):#garde de l'ancienne boucle for
                            id=matrice[z2][x][y]#recup id de la brique qui bloque
                            if lid != id and id!=0: #pour pas compter 2 fois la même brique
                                dicobriques[bid][1]+=1
                                dicobriques[id][0].add(bid)#la brique id soutient la bid
                            lid=id
                    elif z2==0:
                        run=False
                        for i in range(pos[0],pos[0]+rang+1):
                            matrice[z1][i][y]=0
                            matrice[z2][i][y]=bid
                    z2-=1            
            elif axe=='y':#on regarde dans le plan y=pos[1]
                rang=brique[1][1]
                x=pos[0]
                while run:
                    for y in range(pos[1],pos[1]+rang+1):
                        if matrice[z2][x][y]!=0:
                            for i in range(pos[1],pos[1]+rang+1):#suprime ancienne pos et cree nouvelle pos
                                matrice[z1][x][i]=0
                                matrice[z2+1][x][i]=bid
                            stopfall=True
                            break
                    if stopfall:
                        run=False
                        lid=0
                        for y in range(y,pos[1]+rang+1):#garde de l'ancienne boucle for
                            id=matrice[z2][x][y]#recup id de la brique qui bloque
                            if lid != id and id!=0: #pour pas compter 2 fois la même brique
                                dicobriques[bid][1]+=1
                                dicobriques[id][0].add(bid)#la brique id soutient la bid
                            lid=id
                    elif z2==0:
                        run=False
                        for i in range(pos[0],pos[0]+rang+1):
                            matrice[z1][x][i]=0
                            matrice[z2][x][i]=bid
                    z2-=1     
            elif axe=="z":
                rang=brique[1][1]
                x=pos[0]
                y=pos[1]
                while run:
                    if matrice[z2][x][y]!=0:
                        for i in range(rang+1):
                            matrice[z1+i][x][y]=0
                            matrice[z2+1+i][x][y]=bid
                            stopfall=True
                    if stopfall:
                        run=False
                        id=matrice[z2][x][y]
                        dicobriques[bid][1]=1
                        dicobriques[id][0].add(bid)
                    elif z2==0:
                        run=False
                        for i in range(rang+1):
                            matrice[z1+i][x][y]=0
                            matrice[z2+1+i][x][y]=bid
                    z2-=1
            else:
                x=pos[0]
                y=pos[0]
                while run:
                    if matrice[z2][x][y]!=0:
                        matrice[z1][x][y]=0
                        matrice[z2+1][x][y]=bid
                        stopfall=True
                    if stopfall:
                        run=False
                        id=matrice[z2][x][y]
                        dicobriques[bid][1]=1
                        dicobriques[id][0].add(bid)
                    elif z2==0:
                        run=False
                        matrice[z1][x][y]=0
                        matrice[z2][x][y]=bid
                    z2-=1          
def validdestru():
    som=0
    for key in dicobriques:
        destru=True
        for key2 in dicobriques[key][0]:
            if dicobriques[key2][1]==1:
                destru=False
                break
        if destru:
            som+=1
    print(som)
start=time()
briques=recupbrique(briques)
modifbrique()#compression
briques=recupz(briques)#tri par hauteur
matrice=creamatrice()
remplimatrice(briques)
dicobriques=creadico()
fall()
validdestru()