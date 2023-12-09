import sys
import time
start = time.time()
filename = sys.argv[1]
input = open(filename,"r")
lines = input.readlines()
listcouleur=[("red",12),("green",13),("blue",14)]
nombre = ""
couleur=""
som=0
bonneligne=True
res = [0,0,0]
def Idgame(line): #ok
	res=""
	for char in line[5:]:
		if char == ":" :
			return int(res)
		else:
			res+=char
for line in lines :
	line=line.strip()
	line+=";"
	founddeuxpoint = False
	for char in line:
		if not founddeuxpoint:
			if char == ":":
				founddeuxpoint = True
		elif char == ';':
			#on met le resutat dans res et on test
			for couple in listcouleur:
				if couleur == couple[0]:
					res[listcouleur.index(couple)]+= int(nombre)
					nombre =""
					couleur=""
			for i in range(3):
				if res[i] > listcouleur[i][1] :
					bonneligne = False
			res=[0,0,0]
		elif char == ',':
			#on passe a une auttre couleur potentiel
			for couple in listcouleur :
				if couleur == couple[0]:
					res[listcouleur.index(couple)] += int(nombre)
					nombre=""
					couleur=""
		elif char != " ":
			if char.isdigit():
				nombre+=char
			else :
				couleur+=char
	if bonneligne:
		som+=Idgame(line)
	res=[0,0,0]
	bonneligne=True
	nombre=""
	couleur=""
print(som)
end=time.time()
print(end-start)