import sys
from time import time as ti
start=ti()
data=open(sys.argv[1],"r").read().strip().split("\n")
def Convert_data():#matrice des pertes de chaleur
	res=[]
	tmp=[]
	for i in range(len(data)):
		for char in data[i]:
			tmp.append(int(char))
		res.append(tmp)
		tmp=[]
	return res
def Crea_matrice_poids():#matrice des poids des noeuds pour dij
	res=[]
	tmp=[]
	for i in range(len(data)):
		for i2 in range(len(data[0])):
			tmp.append(-1)#=infinie
		res.append(tmp)
		tmp=[]
	res[0][0]=0#poitn de depart
	return res
def Recup_min(liste):#renvoie la pos du noeud avec le plus peti poids
	mini=matrice[liste[0][0]][liste[0][1]]
	rpos=liste[0]
	for pos in liste[1:]:
		if matrice[pos[0]][pos[1]]<mini:
			rpos=pos
			mini=matrice[pos[0]][pos[1]]
	return rpos
def Verif_direction(y,x):#a verifier 
	base=dico_predecesseur[(y,x)]
	pred=base
	compt=0
	while compt<2:
		if pred=="b":
			pred=dico_predecesseur[(y+1,x)]	
			if pred != base:
				return "hgd"
			y=y+1
		elif pred=="h":
			pred=dico_predecesseur[(y-1,x)]
			if pred != base:
				return "bgd"
			y=y-1
		elif pred=="g":
			pred=dico_predecesseur[(y,x-1)]
			if pred != base:
				return "hbd"
			x=x-1
		elif pred=="d":
			pred=dico_predecesseur[(y,x+1)]
			if pred != base:
				return "hbg"
			x=x+1
		compt+=1
	if base in 'hb':
		return "gd"
	if base in 'gd':
		return "hb"
	if base=="None":#seul le point de depart respect cette condition
		return 'bd'
def dijkstrat():
	list_a_faire=[(0,0)]
	while True :
		y,x = Recup_min(list_a_faire)
		# print(y,x)
		# input("")
		if (y,x)==end:#la fin, sortie le plus petit a faire
			return matrice[y][x]
		list_a_faire.remove((y,x))
		li_direction=Verif_direction(y,x)
		for direction in li_direction:
			
			if direction == "h" and y!=0:
				if matrice[y-1][x]==-1:
					matrice[y-1][x]=data[y-1][x]+matrice[y][x]
					list_a_faire.append((y-1,x))
					dico_predecesseur[(y-1,x)]="b" #son pred est en bas
				elif data[y-1][x]+matrice[y][x]<matrice[y-1][x]:
					matrice[y-1][x]=data[y-1][x]+matrice[y][x]
					dico_predecesseur[(y-1,x)]="b"
			
			elif direction=="b" and y!=max_y:
				if matrice[y+1][x]==-1:
					matrice[y+1][x]=data[y+1][x]+matrice[y][x]
					list_a_faire.append((y+1,x))
					dico_predecesseur[(y+1,x)]="h" #son pred est en bas
				elif data[y+1][x]+matrice[y][x]<matrice[y+1][x]:
					matrice[y+1][x]=data[y+1][x]+matrice[y][x]
					dico_predecesseur[(y+1,x)]="h"

			elif direction=="g" and x!=0:
				if matrice[y][x-1]==-1:
					matrice[y][x-1]=data[y][x-1]+matrice[y][x]
					list_a_faire.append((y,x-1))
					dico_predecesseur[(y,x-1)]="d" #son pred est en bas
				elif data[y][x-1]+matrice[y][x]<matrice[y][x-1]:
					matrice[y][x-1]=data[y][x-1]+matrice[y][x]
					dico_predecesseur[(y,x-1)]="d"				

			elif direction=="d" and x!=max_x:
				if matrice[y][x+1]==-1:
					matrice[y][x+1]=data[y][x+1]+matrice[y][x]
					list_a_faire.append((y,x+1))
					dico_predecesseur[(y,x+1)]="g" #son pred est en bas
				elif data[y][x+1]+matrice[y][x]<matrice[y][x+1]:
					matrice[y][x+1]=data[y][x+1]+matrice[y][x]
					dico_predecesseur[(y,x+1)]="g"
		# for li in matrice:
		# 	print(li)
		# print("")
		# input("")
def Recup_chemin(y,x):
	while True:
		print(y,x)
		if dico_predecesseur[(y,x)]=="b":
			matrice[y][x]="^"
			y=y+1
		elif dico_predecesseur[(y,x)]=="h":
			matrice[y][x]="v"
			y=y-1
		elif dico_predecesseur[(y,x)]=="g":
			matrice[y][x]=">"
			x=x-1
		elif dico_predecesseur[(y,x)]=="d":
			matrice[y][x]="<"
			x+=1		
		elif dico_predecesseur[(y,x)]=="None":
			break

dico_predecesseur={}
dico_predecesseur[(0,0)]="None"#poitn de depart
data=Convert_data()
matrice=Crea_matrice_poids()
# for li in data:
# 	print(li)
# print("")
#coordonnée d'arrivée
max_x=len(data[0])-1
max_y=len(data)-1
end=(max_y,max_x)
print(dijkstrat())
for li in matrice:
	print(li)
print("")
matrice=Crea_matrice_poids()
Recup_chemin(max_y,max_x)
for li in matrice:
	print(li)