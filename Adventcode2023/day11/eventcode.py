import sys
import time
from math import factorial as fac
start=time.time()
input=open(sys.argv[1],"r")
lines=input.read().strip()
lines=lines.split("\n")
def Creagalaxie(lines):
    grille=[]
    for i in range(len(lines)):
        grille.append([])
        for i2 in range(len(lines[i])):
            grille[i].append(lines[i][i2]) 
    return grille 
def Crealiempty(univ):
	liligne=[]
	licolo=[]
	li=[]
	for i in range(len(univ)):
		if "#" not in univ[i]:
			liligne.append(i)
	for colonne in range(len(univ[0])):
		for ligne in range(len(univ)):
			li.append(univ[ligne][colonne])
		if "#" not in li :
			licolo.append(colonne)
		li=[]
	return liligne,licolo
def Recupstars(univ):
	listars=[]
	for y in range(len(univ)):
		for x in range(len(univ[y])):
			if univ[y][x] == "#":
				listars.append((y,x))
	return listars
def Dist(gala1,gala2):
	dx=abs(gala1[1]-gala2[1])
	dy=abs(gala1[0]-gala2[0])
	return dx+dy
def Expendligne(univ,liligne):
	t=0
	for i in liligne:
		univ.insert(i+t,univ[i+t])
		t+=1
	return univ
def Expendcolonne(univ,licolo):
	t=0
	for i in licolo :
		# print(univ[4])
		for ligne in range(len(univ)):
			# print(univ[4],ligne)
			univ[ligne].insert(i+t,".")
		t+=1
	return univ
def Comptage(listars):
	som=0
	while len(listars) > 1 :
		i=0
		for i2 in range(1,len(listars)):
			som+=Dist(listars[i],listars[i2])
		del listars[0]
	return som
univ=Creagalaxie(lines)
liligne,licolo=Crealiempty(univ)
#si je fais univ=Expendligne(univ,liligne) puis univ=Expendcolonne(univ,licolo) bug dans Expendcolonne 
univ=Expendcolonne(univ,licolo)
univ=Expendligne(univ,liligne)
listars=Recupstars(univ)
print(Comptage(listars))
####Part2######
univ=Creagalaxie(lines)
listars=Recupstars(univ)
def Transformpos(gala):
	t=-1
	y1=0
	x1=0
	for i in range(-1,-len(liligne)-1,-1):
		t+=1
		if gala[0] > liligne[i]:
			y1=len(liligne)-t
			break
	t=-1
	for i in range(-1,-len(licolo)-1,-1):
		t+=1
		if gala[1] > licolo[i]:
			x1=len(licolo)-t
			break
	return (gala[0]+y1*999999,gala[1]+x1*999999)
for i in range(len(listars)):
	listars[i]=Transformpos(listars[i])
print(Comptage(listars))
print(time.time()-start)
