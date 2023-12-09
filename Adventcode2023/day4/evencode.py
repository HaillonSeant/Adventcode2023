import sys
import time
start = time.time() 
filename=sys.argv[1]
input=open(filename,"r")
lines=input.readlines()

def Setgagnant(line):
	setgagnant=set() #aller de 10 a 38
	found=False
	number=""
	for char in line:
		if found :
			if char.isdigit():
				number+=char
			elif char == " " and number!="":
				setgagnant.add(number)
				number=""
			elif char == "|":
				break
		elif char==":":
			found=True
	return setgagnant

def Combiengagnant(line,setgagnant):
	number=""
	res=0
	line = line.strip()+" "
	for i in range(42,117):
		if line[i].isdigit():
			number+=line[i]
		elif line[i]==" " and number!="":
			if number in setgagnant :
				res+=1
			number=""
	return res

def Pointwin(lines) :
	som=0
	for line in lines :
		setgagnant=Setgagnant(line)
		combiengagnant = Combiengagnant(line,setgagnant)
		if combiengagnant != 0:
			som+= 2**(combiengagnant-1)
	return som

# def Cardwin(line):
# 	setgagnant = Setgagnant(line)
# 	return Combiengagnant(line,setgagnant)
print(time.time()-start)
print(Pointwin(lines))

########### PART 2 ############### #recursivite $
start=time.time()
listcardwin=[]
listnumber=[]#combien de copie
som=0
for line in lines :
	setgagnant=Setgagnant(line)
	listcardwin.append(Combiengagnant(line,setgagnant))
	listnumber.append(1)

for i in range(len(listcardwin)):
	for i2 in range(i+1,i+listcardwin[i]+1):
		if i2 <= len(listnumber)-1:
			listnumber[i2]+=listnumber[i]

for i in range(len(listnumber)):
	som+=listnumber[i]
print(time.time()-start)
print(som)