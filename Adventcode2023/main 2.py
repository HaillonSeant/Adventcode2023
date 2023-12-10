import sys
import time
input=open(sys.argv[1],"r")
lines=input.read().strip()
lines=lines.split("\n")
def Creagrille(lines):
    grille=[]
    for i in range(len(lines)):
        grille.append([])
        for i2 in range(len(lines[i])):
            grille[i].append(lines[i][i2])       
def Spos(grille):
    for y in range(len(grille)):
        for x in range(len(grille[0])):
            if grille[y][x]=="S":
                return(y,x)
def Start(grille,spos):
    if grille[spos[0]][spos[1]-1] in "L-F" and spos[1]-1>=0:
        return (spos[0],spos[1]-1)
    if grille[spos[0]-1][spos[1]] in "F|7" and spos[0]-1>=0:
        return (spos[0]-1,spos[1])
    if grille[spos[0]][spos[1]+1] in "J7-":
        return (spos[0],spos[1]+1)
    if grille[spos[0]+1][spos[1]] in "|JL":
        return (spos[0]+1,spos[1])
def Avancer(npos,opos):
    if grille[npos[0]][npos[1]] == "L" and npos[1]<opos[1]:
        opos=(npos[0]-1,npos[1])
        return opos,npos



spos=Trouvs(grille)
