import sys
import time
start=time.time()
lines=open(sys.argv[1],"r").read().strip().split('\n')
def Recupcas(lines):
	li=[]
	tmp=[]
	lines.append([])
	for i in range(len(lines)):
		if len(lines[i])==0:
			li.append(tmp)
			tmp=[]
		else:
			tmp.append(lines[i])
	return li
def Checkhori(cas):
	#recherche par en haut, stop avant de prendre la dernière ligne
	i=1
	tmp=tuple(cas[::])#liste des ligne du cas a chercher
	while i<len(tmp)/2:
		tmp2=tmp[i:i*2]
		tmp2=tuple(reversed(tmp2))
		if tmp[0:i]==tmp2:
			return i
		i+=1
	i=1
	tmp=tuple(reversed(tmp))#recherche par le bas 
	while i<len(tmp)/2:
		tmp2=tmp[i:2*i]
		tmp2=tuple(reversed(tmp2))
		if tmp[0:i]==tmp2:
			return len(cas)-i
		i+=1
	return 0
def Checkverti(cas):
	tmp=[]
	st=""
	for colonne in range(len(cas[0])):
		for ligne in range(len(cas)):
			st+=cas[ligne][colonne]
		tmp.append(st)
		st=""
	return Checkhori(tmp)
def Comptage(licas):
	som=0
	for cas in licas:
		t=Checkhori(cas)
		if t==0:
			t=Checkverti(cas)
			som+=t
		else:
			som+=t*100
	return som
lines=Recupcas(lines)
print(Comptage(lines))
tim=time.time()-start
print('temps partie 1 :',tim)
########PART2#########
def Checkhori2(cas,prevcas,pos):
	prevres=Checkhori(prevcas)
	i=1
	tmp=cas[::]
	while i<len(tmp)/2:
		tmp2=tmp[i:i*2]
		tmp2.reverse()
		if tmp[0:i]==tmp2:
			if i!=prevres:
				return i
		i+=1
	if pos==0 :
		return 0
	i=1
	tmp.reverse()
	while i<len(tmp)/2:
		tmp2=tmp[i:2*i]
		tmp2.reverse()
		if tmp[0:i]==tmp2:
			res=len(cas)-i
			if res !=prevres:
				return res
		i+=1
	return 0
def Checkverti2(cas,prevcas,pos):
	prevres=Checkverti(prevcas)
	tmp=[]
	st=""
	for colonne in range(len(cas[0])):
		for ligne in range(len(cas)):
			st+=cas[ligne][colonne]
		tmp.append(st)
		st=""
	return Checkhori(tmp)
def Comptagebourrin(licas):#mettre un n
	som=0
	tmp=[]
	t=0
	c=-1
	for cas in licas:
		c+=1
		run=True
		tmp=cas[::]
		for i in range(len(cas)):
			for i2 in range(len(cas[0])):
				if cas[i][i2]=="#":
					tmp[i]=cas[i][0:i2]+"."+cas[i][i2+1:len(cas[i])]
				else:
					tmp[i]=cas[i][0:i2]+"#"+cas[i][i2+1:len(cas[i])]
				t=Checkhori2(tmp,cas,i)			
				if t==0:
					t=Checkverti2(tmp,cas,i2)
					if t!=0 :
						som+=t
						run=False
						break	
				else:
					som+=t*100
					run=False					
					break
			if not run:
				break
			tmp=cas.copy()
	return som
def Lidiffligne(cas):
	li=[]
	diff=0
	for i in range(len(cas)):
		for i2 in range(i,len(cas)):
			for i3 in range(len(cas[0])):
				if cas[i][i3] != cas[i2][i3]:
					diff+=1
			if diff==1:
				for i3 in range(len(cas[0])):
					if cas[i][i3]!=cas[i2][i3]:
						li.append((i,i3))
			diff=0
	return tuple(li)	
def lidiffcol(cas):
	tmp=[]
	li=[]
	diff=0
	for colonne in range(len(cas[0])):
		st=""
		for ligne in range(len(cas)):
			st+=cas[ligne][colonne]
		tmp.append(st)
	for i in range(len(tmp)):
		for i2 in range(i,len(tmp)):
			for i3 in range(len(tmp[0])):
				if tmp[i][i3] != tmp[i2][i3]:
					diff+=1
			if diff==1:
				for i3 in range(len(tmp[0])):
					if tmp[i][i3]!=tmp[i2][i3]:
						li.append((i3,i))#transformation coor
			diff=0
	return tuple(li)		
def Comtage2(lines):
	som=0
	for cas in lines:
		tmp=cas[::]
		lidiff=Lidiffligne(cas)
		notfound=True
		if len(lidiff)!=0:
			for tup in lidiff:
				if tmp[tup[0]][tup[1]]==".":
					tmp[tup[0]]=tmp[tup[0]][0:tup[1]]+"#"+tmp[tup[0]][tup[1]+1:]
				else:
					tmp[tup[0]]=tmp[tup[0]][0:tup[1]]+"."+tmp[tup[0]][tup[1]+1:]
				res=Checkhori2(tmp,cas,tup[0])
				if res!=0:
					som+=res*100
					notfound=False
					break
		if notfound:
			lidiff=lidiffcol(cas)
			for tup in lidiff:
				if tmp[tup[0]][tup[1]]==".":
					tmp[tup[0]]=tmp[tup[0]][0:tup[1]]+"#"+tmp[tup[0]][tup[1]+1:]
				else:
					tmp[tup[0]]=tmp[tup[0]][0:tup[1]]+"."+tmp[tup[0]][tup[1]+1:]
				res=Checkverti2(tmp,cas,tup[0])
				if res!=0:
					som+=res
					break
	return som				
# lines=Recupcas(lines)		
# print(Comtage2(lines))