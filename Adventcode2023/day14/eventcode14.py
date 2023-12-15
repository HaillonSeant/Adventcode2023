import sys
import time
start=time.time()
data=open(sys.argv[1],"r").read().strip().split('\n')
def Creagrille(lines):
    grille=[]
    for i in range(len(lines)):
        grille.append([])
        for i2 in range(len(lines[i])):
            grille[i].append(lines[i][i2]) 
    return grille
def pgi(gi):
	for li in gi:
		print("".join(li))
	print('\n') 
def Pushnorth(grille):
	for y in range(1,len(grille)):
		for x in range(len(grille[0])):
			if grille[y][x]=="O":
				y2=y
				while True:
					if grille[y2-1][x]=="." and y2>0:
						y2-=1
					else:
						grille[y][x]="."
						grille[y2][x]="O"
						break
def Pushsouth(grille):
	for y in range(-2,-len(grille)-1,-1):
		for x in range(len(grille[0])):
			if grille[y][x]=="O":
				y2=y
				while True:
					if grille[y2+1][x]=="." and y2<-1:
						y2+=1
					else:
						grille[y][x]="."
						grille[y2][x]="O"
						break	
def Pushwest(grille):
	for x in range(1,len(grille[0])):
		for y in range(len(grille)):
			if grille[y][x]=="O":
				x2=x
				while True:
					if grille[y][x2-1]=='.' and x2>0:
						x2-=1
					else:
						grille[y][x]="."
						grille[y][x2]="O"
						break						
def Pusheast(grille):
	for x in range(-2,-len(grille[0])-1,-1):
		for y in range(len(grille)):
			if grille[y][x]=="O":
				x2=x
				while True:
					if grille[y][x2+1]=='.' and x2<0:
						x2+=1
					else:
						grille[y][x]="."
						grille[y][x2]="O"
						break	
def Comptage(grille):
	l=len(grille)
	som=0
	for y in range(len(grille)):
		for char in grille[y]:
			if char=='O':
				som+=l-y
	return som
def Cycle(grille):
	ligrille=[]
	n=0
	tmp=[]
	gi=[]
	a=True
	for l in grille:
		gi.append(l[::])
	while True:
		Pushnorth(gi)
		Pushwest(gi)
		Pushsouth(gi)
		Pusheast(gi)
		n+=1
		if gi in ligrille:
			print(n,'tours')
			print(ligrille.index(gi),'indice premier')
			return gi
		for i in gi:
			tmp.append(i[::])
		ligrille.append(tmp)
		tmp=[]

def Cycle2(grille,n):
	grille2=[]
	for i in grille:
		grille2.append(i[::])
	while n>0:
		Pushnorth(grille2)
		Pushwest(grille2)
		Pushsouth(grille2)
		Pusheast(grille2)
		n-=1
	return(grille2)
def cycle3(grille):
	liscore=[]
	gi=grille[::]
	t=0
	while True :
		t+=1
		gi=Cycle2(gi,1)
		score=Comptage(gi)
		if score not in liscore:
			liscore.append(score)
		else:
			return t,liscore.index(score)+1
		
grille=Creagrille(data)
gi=Cycle(grille)
print(Comptage(gi))