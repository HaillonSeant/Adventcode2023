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
	tmp=cas[::]
	while i<len(tmp)/2:
		tmp2=tmp[i:i*2]
		tmp2.reverse()
		if tmp[0:i]==tmp2:
			return i
		i+=1
	i=1
	tmp.reverse()#recherche par le bas 
	while i<len(tmp)/2:
		tmp2=tmp[i:2*i]
		tmp2.reverse()
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
	i=1
	while i<len(tmp)/2:
		tmp2=tmp[i:i*2]
		tmp2.reverse()
		if tmp[0:i]==tmp2:
			return i
		i+=1
	i=1
	tmp.reverse()
	while i<len(tmp)/2:
		tmp2=tmp[i:2*i]
		tmp2.reverse()
		if tmp[0:i]==tmp2:
			return len(tmp)-i
		i+=1
	return 0
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
	i=1
	while i<len(tmp)/2:
		tmp2=tmp[i:i*2]
		tmp2.reverse()
		if tmp[0:i]==tmp2:
			if i !=prevres:
				return i
		i+=1
	if pos==0:
		return 0
	i=1
	tmp.reverse()
	while i<len(tmp)/2:
		tmp2=tmp[i:2*i]
		tmp2.reverse()
		if tmp[0:i]==tmp2:
			res=len(tmp)-i
			if res!=prevres:
				return res
		i+=1
	return 0
def Comptagebourrin(licas):#mettre un n
	som=0
	tmp=[]
	t=0
	for cas in licas:
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
print(Comptagebourrin(lines))
fin=time.time()
print('temps partie2 :',fin-(tim+start))
print('temps total :',fin-start)