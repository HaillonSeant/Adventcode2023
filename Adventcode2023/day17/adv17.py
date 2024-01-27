import sys
from time import time as ti
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
def Crea_matrice():#matrice des poids des noeuds pour dij
	res=[]
	tmp=[]
	for i in range(len(data)):
		for i2 in range(len(data[0])):
			tmp.append([-1])#=infinie
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
def dijkstrat():
	list_a_faire=[(0,0)]
	while True :
		y,x = Recup_min(list_a_faire)
		if y==0:
			if matrice[y+1][x]==-1:
				matrice[y+1][x]=data[y+1][x]+matrice[y][x]
				list_a_faire.append((y,x))
			elif data[y+1][x]+matrice[y][x]<matrice[y+1][x]:
				matrice[y+1][x]=data[y+1][x]+matrice[y][x]
		elif y==max_y:
			if matrice[y-1][x]==-1:
				matrice[y-1][x]=data[y-1][x]+matrice[y][x]
				list_a_faire.append((y,x))
			elif data[y-1][x]+matrice[y][x]<matrice[y-1][x]:
				matrice[y-1][x]=data[y-1][x]+matrice[y][x]		
		else:
			if data[y+1][x]+matrice[y][x]<matrice[y+1][x]:
				matrice[y+1][x]=data[y+1][x]+matrice[y][x]
				if (y+1,x) not in list_fait:
					tmp.append(y+1,x)		
			if data[y-1][x]+matrice[y][x]<matrice[y-1][x]:
				matrice[y-1][x]=data[y-1][x]+matrice[y][x]
				if (y-1,x) not in list_fait:
					tmp.append(y-1,x)
		if x==0:
			if data[y][x+1]+matrice[y][x]<matrice[y][x+1]:
				matrice[y][x+1]=data[y][x+1]+matrice[y][x]
		elif x==max_x:
			if data[y][x-1]+matrice[y][x]<matrice[y][x-1]:
				matrice[y][x-1]=data[y][x-1]+matrice[y][x]
		else:
			if data[y][x+1]+matrice[y][x]<matrice[y][x+1]:
				matrice[y][x+1]=data[y][x+1]+matrice[y][x]
			if data[y][x-1]+matrice[y][x]<matrice[y][x-1]:
				matrice[y][x-1]=data[y][x-1]+matrice[y][x]

data=Convert_data()
matrice=Crea_matrice()
for li in matrice:
	print(li)
#coordonnée d'arrivée
max_x=len(data[0])
max_y=len(data)
end=(max_y,max_x)
