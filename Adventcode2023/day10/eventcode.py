import sys
import time
start=time.time()
input=open(sys.argv[1],"r")
lines=input.read().strip()
lines=lines.split("\n")
def Creagrille(lines):
    grille=[]
    for i in range(len(lines)):
        grille.append([])
        for i2 in range(len(lines[i])):
            grille[i].append(lines[i][i2]) 
    return grille      
def Spos(grille):
    for y in range(len(grille)):
        for x in range(len(grille[0])):
            if grille[y][x]=="S":
                return(y,x)
def Start(grille,spos):
    if grille[spos[0]][spos[1]-1] in "L-F" :
        return (spos[0],spos[1]-1),"G"
    if grille[spos[0]-1][spos[1]] in "F|7" :
        return (spos[0]-1,spos[1]),"H"
    if grille[spos[0]][spos[1]+1] in "J7-" :
        return (spos[0],spos[1]+1),"D"
    if grille[spos[0]+1][spos[1]] in "|JL":
        return (spos[0]+1,spos[1]),"B"
def Avancer(npos,direct):
    # print(npos,direct)
    if grille[npos[0]][npos[1]] == "L" and direct=="G":
        return (npos[0]-1,npos[1]),"H"
    if grille[npos[0]][npos[1]] == "L" and direct=="B":
        return (npos[0],npos[1]+1),"D"
    
    if grille[npos[0]][npos[1]] == "-" and direct=="G":
        return (npos[0],npos[1]-1), "G"
    if grille[npos[0]][npos[1]] == "-" and direct=="D":
        return (npos[0],npos[1]+1),"D"
    
    if grille[npos[0]][npos[1]] == "F" and direct=="G":
        return (npos[0]+1,npos[1]),"B"
    if grille[npos[0]][npos[1]] == "F" and direct=="H":
        return (npos[0],npos[1]+1),"D"
   
    if grille[npos[0]][npos[1]] == "|" and direct=="H":
        return (npos[0]-1,npos[1]),"H"
    if grille[npos[0]][npos[1]] == "|" and direct=="B":
        return (npos[0]+1,npos[1]),"B"
    
    if grille[npos[0]][npos[1]] == "J" and direct=="B":
        return (npos[0],npos[1]-1),"G"
    if grille[npos[0]][npos[1]] == "J" and direct=="D":
        return (npos[0]-1,npos[1]),"H"
    
    if grille[npos[0]][npos[1]] == "7" and direct=="D":
        return (npos[0]+1,npos[1]),"B"
    if grille[npos[0]][npos[1]] == "7" and direct=="H":
        return (npos[0],npos[1]-1),"G"    
def Comptage(grille,spos,pos_direct):
    run = True
    t=1
    #istart=0
    while run:
        # Start(grille,spos,istart)
        t+=1
        pos_direct=Avancer(pos_direct[0],pos_direct[1])
        if grille[pos_direct[0][0]][pos_direct[0][1]] == "S":
            return t//2 #en raison du problème, on peut jsute compter la taille de la boucle total et diviser par deux
grille=Creagrille(lines)
spos=Spos(grille)
pos_start= Start(grille,spos)
print(Comptage(grille,spos,pos_start))
print(time.time()-start)
#######part2###########
def Recupminmax(grille,spos,pos):
    xmin=pos[0][1]
    xmax=pos[0][1]
    ymin=pos[0][0]
    ymax=pos[0][0]
    posloop=[(pos[0][0],pos[0][1])]#rejoute premier point
    while True :
        pos=Avancer(pos[0],pos[1])
        posloop.append((pos[0][0],pos[0][1]))
        if int(pos[0][0]) > ymax:
            ymax=int(pos[0][0])
        elif int(pos[0][0]) < ymin :
            ymin=int(pos[0][0])
        
        if int(pos[0][1])>xmax:
            xmax=int(pos[0][1])
        elif int(pos[0][1])<xmin:
            xmin=int(pos[0][1])
        
        if grille[pos[0][0]][pos[0][1]]=="S":
            break
    return (ymin,xmin),(ymax,xmax),posloop
def Sortposloopy(grille,pmin,pmax,posloop):
    sortposloop=[]
    liligne=[]
    ligne=pmin[0]
    run=True
    t=0
    while run:  
        for pos in posloop:
            if pos[0] == ligne:
                liligne.append(pos)#ajout a la liste de la ligne
                # posloop.remove(pos)
        sortposloop.append(liligne)
        liligne=[]#clear marche pas
        ligne+=1
        if ligne > pmax[0]:
            run = False
    return sortposloop
def Sortposloopx(grille,pmin,pmax,posloop):
    sortposloop=[]
    licolonne=[]
    colonne=pmin[1]
    ligne=pmin[0]
    mini=(0,1000)
    run=True
    while run:
        while len(posloop[ligne])!=0:  
            for pos in posloop[ligne]:
                if pos[1] < mini[1] :
                    mini=pos
            licolonne.append(mini)
            posloop[ligne].remove(mini)
            mini=(0,1000)
        ligne+=1
        sortposloop.append(licolonne)
        licolonne=[]
        if ligne > pmax[0]:
            run=False
    return sortposloop
# def Intvalide(grille,pmin,pmax,posloop):
#     invalide=[]
#     for ligne in range(pmin[0]+1,pmax[0]):
        



pmin = Recupminmax(grille,spos,pos_start)[0]
pmax=Recupminmax(grille,spos,pos_start)[1]
posloop=Recupminmax(grille,spos,pos_start)[2]
#pmin,pmax,posloop=Recupminmax(grille,spos,pos_start)
posloop=Sortposloopy(grille,pmin,pmax,posloop)
posloop=Sortposloopx(grille,pmin,pmax,posloop)

print(posloop[0])



