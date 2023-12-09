import sys
import time
start=time.time()
filename = sys.argv[1]
input = open(filename,"r")
lines = input.readlines()
ispart=False
machine=[] 
for line in lines:
	machine.append(line.strip()) #ca me saoule readlines, voila une liste de liste propre

xmax=len(machine[0]) #gauceh a droite
ymax=len(machine)#haut en bas
number='' #pour stocker les digits adjacents
som=0
#print(xmax,ymax)
def Testpart(x,y):
	for ix in range(-1,2):
		if 0<=x+ix<=(xmax-1):#indice max en x (xmax-1)
			for iy in range(-1,2):
				if 0<=y+iy<=(ymax-1):
					if not machine[y+iy][x+ix].isdigit() and machine[y+iy][x+ix]!=".":
						return True
	return False
for y in range(ymax):
	for x in range(xmax):
		if machine[y][x].isdigit(): #on touche pas les symboles
			number+=machine[y][x]
			#print(number)
			if not ispart and Testpart(x,y):
				ispart=True
		elif number!="":#tombe sur un symbole et on a deja un nombre donc c'est la fin de ce dernier

			if ispart:#si le nombre est une partie
				som+=int(number)
				ispart=False
			number=""
		if x==xmax-1 and number!="":
			if ispart:#si le nombre est une partie
				som+=int(number)
				ispart=False
			number=""			

print(som)
print(time.time()-start)

