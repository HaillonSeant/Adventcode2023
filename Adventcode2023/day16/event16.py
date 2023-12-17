import sys
import time
grille=open(sys.argv[1],"r").read().strip().split('\n')
lienergize=[]
libeam=[(0,-1,0,1)]#tuple (y,x,vy,vx) 
libeamsave=[]
som=0
def Nextile(beam):
	global som
	if beam[2]==-1:
		if beam[0]-1<0:
			return 0
		if (beam[0]-1,beam[1]) not in lienergize:
			som+=1
			lienergize.append((beam[0]-1,beam[1]))
		return grille[beam[0]-1][beam[1]]
	if beam[2]==+1:
		if beam[0]+1==len(grille):
			return 0
		if (beam[0]+1,beam[1]) not in lienergize:
			som+=1
			lienergize.append((beam[0]+1,beam[1]))
		return grille[beam[0]+1][beam[1]]
	if beam[3]==-1:
		if beam[1]-1<0:
			return 0
		if (beam[0],beam[1]-1) not in lienergize:
			som+=1
			lienergize.append((beam[0],beam[1]-1))
		return grille[beam[0]][beam[1]-1]
	if beam[3]==1:
		if beam[1]+1==len(grille[0]):
			return 0
		if (beam[0],beam[1]+1) not in lienergize:
			som+=1
			lienergize.append((beam[0],beam[1]+1))
		return grille[beam[0]][beam[1]+1]
def Mouvement(beam):
	nextile=0
	while True:
		nextile=Nextile(beam)
		if nextile==0:
			del libeam[0]
			break
		elif nextile=='.':
			beam=(beam[0]+beam[2],beam[1]+beam[3],beam[2],beam[3])
		elif nextile=='\\':
			if beam[2]!=0:#vitesse verticale
				if beam[2]==-1:#monte
					beam=(beam[0]+beam[2],beam[1]+beam[3],0,-1)
				else:
					beam=(beam[0]+beam[2],beam[1]+beam[3],0,1)
			else:
				if beam[3]==-1:#vers la gauche 
					beam=(beam[0]+beam[2],beam[1]+beam[3],-1,0)
				else:
					beam=(beam[0]+beam[2],beam[1]+beam[3],1,0)
		elif nextile=='/':
			if beam[2] !=0:#vitesse verticale
				if beam[2]==-1:#monte
					beam=(beam[0]+beam[2],beam[1]+beam[3],0,1)
				else:
					beam=(beam[0]+beam[2],beam[1]+beam[3],0,-1)
			else:
				if beam[3]==-1:#vers la gauche 
					beam=(beam[0]+beam[2],beam[1]+beam[3],1,0)
				else:
					beam=(beam[0]+beam[2],beam[1]+beam[3],-1,0)
		elif nextile=='-':
			if beam[2] !=0:#verif en x ! et split
				if beam[1]-1>=0:
					nbeam=(beam[0]+beam[2],beam[1]+beam[3],0,-1)
					if nbeam not in libeamsave:
						libeam.append(nbeam)
						libeamsave.append(nbeam)
				if beam[1]+1!=len(grille[0]):
					nbeam=(beam[0]+beam[2],beam[1]+beam[3],0,1)
					if nbeam not in libeamsave:
						libeam.append(nbeam)
						libeamsave.append(nbeam)
				del libeam[0]
				break
			else:
				beam=(beam[0]+beam[2],beam[1]+beam[3],beam[2],beam[3])
		elif nextile=='|':
			if beam[3]!=0:#vit hori
				if beam[0]-1>=0:
					nbeam=(beam[0]+beam[2],beam[1]+beam[3],-1,0)
					if nbeam not in libeamsave:
						libeam.append(nbeam)
						libeamsave.append(nbeam)
				if beam[1]+1!=len(grille[0]):
					nbeam=(beam[0]+beam[2],beam[1]+beam[3],1,0)
					if nbeam not in libeamsave:
						libeam.append(nbeam)
						libeamsave.append(nbeam)
				del libeam[0]
				break				
			else:
				beam=(beam[0]+beam[2],beam[1]+beam[3],beam[2],beam[3])
def Comptage():
	while len(libeam)!=0:
		Mouvement(libeam[0])
def Test():#marche pas, pourquoi ? mmême chose mais endehors fonction en bas.1
	res=0
	lx=len(grille[0])
	ly=len(grille)
	for i in range(len(grille)):#lignes vers droite
		libeamsave=[]
		lienergize=[]		
		libeam.append((i,-1,0,1))
		Comptage()
		if som>res:
			res=som
		som=0
	for i in range(len(grille)):#lignes vers gauche
		libeamsave=[]
		lienergize=[]
		libeam.append((i,lx,0,-1))
		# print(libeam)
		Comptage()
		if som>res:
			res=som
		som=0
	for i in range(len(grille[0])):#colonnes vers bas
		libeamsave=[]
		lienergize=[]
		libeam.append((-1,i,1,0))
		Comptage() 
		if som>res:
			res=som
		som=0
	for i in range(len(grille[0])):#colonnes vers hauts
		libeamsave=[]
		lienergize=[]		
		libeam.append((ly,i,-1,0))
		Comptage() 
		if som>res:
			res=som
		som=0
	print(res)	
start=time.time()
Comptage()
end=time.time()
print(som)
print("Partie 1 :",end-start)
start=time.time()
som=0
res=0
libeam=[]
#.1 c'est la même chose ici ! 
for i in range(len(grille)):#lignes vers droite
	libeamsave=[]
	lienergize=[]		
	libeam.append((i,-1,0,1))
	Comptage()
	if som>res:
		res=som
	som=0
for i in range(len(grille)):#lignes vers gauche
	libeamsave=[]
	lienergize=[]
	libeam.append((i,110,0,-1))
	# print(libeam)
	Comptage()
	if som>res:
		res=som
	som=0
for i in range(len(grille[0])):#colonnes vers bas
	libeamsave=[]
	lienergize=[]
	libeam.append((-1,i,1,0))
	Comptage() 
	if som>res:
		res=som
	som=0
for i in range(len(grille[0])):#colonnes vers hauts
	libeamsave=[]
	lienergize=[]		
	libeam.append((110,i,-1,0))
	# print(libeam)
	Comptage() 
	# print((110,i,-1,0),som)
	# input("")
	if som>res:
		res=som
	som=0
end=time.time()
print(res)
print("Partie 2 de la honte absolue :",end-start)
