import sys
import time
start=time.time()
data=open(sys.argv[1],"r").read().strip().split(',')
end = time.time()
print("Time to read the file : " + str(end - start)+"\n")
def Hashvalue(seq):
	som=0
	for char in seq:
		som+=ord(char)
		som*=17
		som=som%256
	return som
def Comptage(data):
	som=0
	for seq in data:
		som+=Hashvalue(seq)
	print(som)
def Creabox():
	libox=[]
	t=0
	while t<256:
		libox.append([]) 
		t+=1
	return libox
def Operate(data):
	t=0
	for seq in data:
		t+=1
		if '=' in seq:
			done=False
			label=seq[:seq.index("=")]
			focal=int(seq[seq.index('=')+1:])
			box=Hashvalue(label)
			for lens in libox[box]:
				if lens[0]==label:
					i=libox[box].index(lens)
					libox[box][i]=(label,focal)
					done=True
					break
			if not done :
				libox[box].append((label,focal))
		else:#j'ai un "-""
			label=seq[:seq.index("-")]
			box=Hashvalue(label)
			for lens in libox[box]:
				if lens[0]==label:
					i=libox[box].index(lens)
					libox[box].remove(lens)
def Comptage2(libox):
	som=0
	for ibox in range(len(libox)):
		for ilens in range(len(libox[ibox])):
			som+=libox[ibox][ilens][1]*(ilens+1)*(ibox+1)
	print(som)
solutionStart = time.time()
separ="=-"
libox=Creabox()
Operate(data)
Comptage(data)
end = time.time()
print("Part 1 : ", )
print("Solution 1 time : " + str(end - solutionStart)+"\n")
solutionStart = time.time()
Comptage2(libox)
end = time.time()
print("Part 2 : ", )
print("Solution 2 time : " + str(end - solutionStart))
print("Total time : " + str(end - start))

