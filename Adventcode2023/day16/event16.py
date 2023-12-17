import sys
import time
start=time.time()
grille=open(sys.argv[1],"r").read().strip().split('\n')
lienergize=[]
libeam=[(0,-1,0,1)]#tuple (y,x,vy,vx) 
libeamsave=[]
som=0
def Nextile(beam):
	global som
	global lienergize
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
	global libeam
	nextile=0
	grille2=[]
	for li in grille:
		grille2.append(li[::])
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
		# if t==1:
		# 	for li in grille2:
		# 		for en in lienergize:
		# 			if grille2[en[0]][en[1]]!="1":
		# 				grille2[en[0]]=grille2[en[0]][0:en[1]]+"1"+grille2[en[0]][en[1]+1:]
		# 	for li in grille2:
		# 		print(li)
		# 	print('')
		# 	input("")

def Comptage():
	global libeam
	while len(libeam)!=0:
		Mouvement(libeam[0],libeam)
def Test():
	global som
	global lienergize
	global libeam
	ly=len(grille)-1
	lx=len(grille[0])-1
	#les quatres coin d'abord
	#haut gauche vers la droite
	libeam2=[(0,-1,0,1)]
	Comptage()
	res=som
	som=0
	libeamsave=[]
	lienergize=[]
	libeam([(-1,0,1,0)])
	#haut gauche vers le bas
	Comptage()
	print(som)
	input("")
	if som > res:
		res=som
	som=0
	libeamsave=[]
	lienergize=[]
	#bas gauche vers la droite 
	Comptage([(ly,-1,0,1)])
	if som > res:
		res=som
	som=0
	libeamsave=[]
	lienergize=[]
	#bas gauche vers le haut
	Comptage([(ly+1,0,-1,0)])
	if som > res:
		res=som
	som=0
	libeamsave=[]
	lienergize=[]
	#bas droit vers gauche
	Comptage([(ly,lx+1,0,-1)])
	if som > res:
		res=som
	som=0
	libeamsave=[]
	lienergize=[]
	#bas droit vers haut
	Comptage([(ly+1,lx,-1,0)])
	if som > res:
		res=som
	som=0
	libeamsave=[]
	lienergize=[]
	#bas haut vers gauche
	Comptage([(0,lx+1,0,-1)])
	if som > res:
		res=som
	som=0
	libeamsave=[]
	lienergize=[]
	#bas droit vers bas
	Comptage([(-1,lx,1,0)])
	if som > res:
		res=som
	som=0
	libeamsave=[]
	lienergize=[]
	for i in range(len(grille)):#lignes gauches
		Comptage([(i,-1,0,1)])
		if som>res:
			res=som
		som=0
		libeamsave=[]
		lienergize=[]
	for i in range(len(grille)):
		Comptage([(i,lx+1,0,-1)])#lignes droites
		if som>res:
			res=som
		som=0
		libeamsave=[]
		lienergize=[]
	for i in range(len(grille[0])):
		Comptage([(-1,i,1,0)])#colonnes hauts 
		if som>res:
			res=som
		som=0
		libeamsave=[]
		lienergize=[]	
	for i in range(len(grille[0])):
		Comptage([(ly+1,i,-1,0)])#colonnes hauts 
		if som>res:
			res=som
		som=0
		libeamsave=[]
		lienergize=[]
	print(res)	




# Comptage(libeam)
# print(som)
# print(time.time()-start)
start2=time.time()
libeamsave=[]
lienergize=[]
som=0
Test()
print(time.time()-start2)


