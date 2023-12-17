import sys
import time
data=open(sys.argv[1],"r")
grille=data.read().strip().split('\n')
data.close()
#dir 0 gauche 1 droite 2 en haut 3 en bas
def Creagrille(grille):
	tmp=[]
	for y in range(len(grille)):
		tmp.append([])
		for x in range(len(grille[0])):
			tmp[y].append(int(grille[y][x]))
	return tmp
def Avancer(pos,direct,comp):
	x=pos[1]
	y=pos[0]
	som=0
	if direct ==0:
		for num in grille[y][x-comp:x]:
			som+=num
		return som
	elif direct==1:
		for num in grille[y][x+1:x+comp+1]:
			som+=num		
		return som
	elif direct==2:
		for i in range(y-comp,y):
			print(i)
			som+=grille[i][x]
		return som
	elif direct==3:
		for i in range(y+1,y+comp+1):
			som+=grille[i][x]
		return som

grille=Creagrille(grille)
for li in grille:
	print(li)
print(Avancer((0,12),0,2))