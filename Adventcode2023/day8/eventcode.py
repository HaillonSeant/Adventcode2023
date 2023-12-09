import sys
import time
start = time.time() 
part=start
input=open(sys.argv[1],"r")
lines=input.readlines()
dico={}
som=0
LR = lines[0].replace("\n","")
def Creadico(lines):
	for line in lines[2:]:
		cle = line[:3]
		dico[(cle)] = (line[7:10],line[12:15])
def Comptage():
	fin = True
	pos="AAA"
	res=0
	while fin :
		for i in range(len(LR)):
			res+=1
			if LR[i] == "L":
				pos=dico[pos][0]
			else:
				pos=dico[pos][1]
			if pos == "ZZZ":
				fin = False
				break
	return res
Creadico(lines)
print(Comptage())
print(time.time()-start)
def RecupA():
	lista=[]
	for line in lines[2:]:
		if line[2] == "A":
			lista.append(line[:3])
	return lista
lista=RecupA()
def Comptage2():
	fin = True
	res=0
	tous= False
	while fin :
		for i in range(len(LR)):
			for i2 in range(len(lista)):
				if LR[i]=="L":
					lista[i2]=dico[lista[i2]][0]
				else:
					lista[i2]=dico[lista[i2]][1]
			tous=True
			res+=1
			for pos in lista:
				if pos[2] != "Z":
					tous=False
					break
			if tous:
				fin=False
				break
	return res
print(Comptage2())






