import sys
import time
start = time.time()
filename = sys.argv[1]
input = open(filename,"r")
lines = input.readlines()
machine=[] 
for line in lines:
	machine.append(line.strip()) #ca me saoule readlines, voila une liste de liste propre
xmax=len(machine[0]) #gauche a droite
ymax=len(machine)#haut en bas
number='' #pour stocker les digits adjacents
som=0
listcoorgear=[] #liste de liste avec  [[coor,number1,number2],[coor,number1]] on cherceh juste les liste de longueur 3
coornumber=[]#[x du premier digit,x du dernier,y]
l=0
for y in range(ymax):
	for x in range(xmax):
		if machine[y][x] == "*":
			listcoorgear.append([(x,y)])

def Testgear(coornumber,number,l):
	'''Verifie si number touche un * et ajoute dans listcoorgear la valeur dans la bonne liste'''
	global listcoorgear
	coorplace=[]
	#print(coornumber)
	for xdigit in range(coornumber[0],coornumber[1]):
		# if l==96:
		# 	print(xdigit)
		#print("xdigit "+number+" "+str(xdigit))
		for ix in range(-1,2):
			if 0<=xdigit+ix<=(xmax-1):#indice max en x (xmax-1)
				for iy in range(-1,2):
					if 0<=coornumber[2]+iy<=(ymax-1): #coornumber[2] = y du nombre
						if machine[coornumber[2]+iy][xdigit+ix]=="*":
							for li in listcoorgear:#pas opti faudrait une liste pour coor * et une liste avec les nombres
								if (xdigit+ix,coornumber[2]+iy) in li and (xdigit+ix,coornumber[2]+iy) not in coorplace:
									li.append(number)
									coorplace.append((xdigit+ix,coornumber[2]+iy))#on evite les doublons avec ca					
for y in range(ymax):
	for x in range(xmax):
		if machine[y][x].isdigit(): #on touche pas les symboles
			number+=machine[y][x]
			if len(coornumber) == 0:#on rentre la premiere coordonnée en x
				coornumber.append(x)
		elif number!="":#tombe sur un symbole et on a deja un nombre donc c'est la fin de ce dernier
			coornumber.append(x)#on le x d'avant
			coornumber.append(y)
			Testgear(coornumber,number,l)
			coornumber=[]
			number=""
		if x==xmax-1 and number!="": #utilise or dans la ligne au dessus
			coornumber.append(x+1) #ancienne version problème potentiel ici
			coornumber.append(y)
			# if y == 96 : 
			# 	print(coornumber)
			# 	l=96
			Testgear(coornumber,number,l)
			coornumber=[]
			number=""
for gear in listcoorgear :
	if len(gear)==3:
		som+=int(gear[1])*int(gear[2])
print(som)
print(time.time()-start)


