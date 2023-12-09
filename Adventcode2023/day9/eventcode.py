import sys
import time
start = time.time() 
input=open(sys.argv[1],"r")
lines=input.read().strip()
lines = lines.split("\n")
for i in range(len(lines)):
	lines[i]=lines[i].split(" ")
def Convertstr():
	for line in lines:
		for i in range(len(line)):
			line[i]=int(line[i])
def Step(line):
	listep=[]
	for i in range(len(line)-1):
		listep.append(line[i+1]-line[i])
	return listep

def Crealistep(line):
	listep=[]
	listep.append(line)
	i=0
	while True:
		step = Step(listep[i])
		if step.count(0) == len(step):
			listep.append(step)
			break
		i+=1
		listep.append(step)
	return listep

def Resultatstep(listep):
	listep.reverse()
	for i in range(len(listep)-1):
		listep[i+1].append(listep[i][-1]+listep[i+1][-1])
	return listep[len(listep)-1][-1]
def Sommation(lines):
	som=0
	for line in lines:
		som+=Resultatstep(Crealistep(line))
	return som
Convertstr()
print(Sommation(lines))

#part2###
def Resultatstep2(listep):
	listep.reverse()
	for i in range(len(listep)-1):
		listep[i+1].insert(0,listep[i+1][0]-listep[i][0])
		print(listep)
	return listep[len(listep)-1][0]
def Sommation2(lines):
	som=0
	for line in lines:
		som+=Resultatstep2(Crealistep(line))
	return som
print(Sommation2(lines))




