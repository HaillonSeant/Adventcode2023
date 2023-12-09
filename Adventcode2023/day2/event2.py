import sys
filename = sys.argv[1]
input = open(filename,"r")
lines = input.readlines()
listcouleur=[("red",12),("green",13),("blue",14)]

nombre = ""
couleur=""
som=0

restot=[0,0,0]
res = [0,0,0]

for line in lines :
	line=line.strip()
	line+=";"
	founddeuxpoint = False

	for char in line:
		if not founddeuxpoint:
			if char == ":":
				founddeuxpoint = True
		elif char == ';':
			for couple in listcouleur: #pour aps que le dernier tirage saute
				if couleur == couple[0]:
					res[listcouleur.index(couple)]+= int(nombre)
					nombre =""
					couleur=""
			for i in range(3):
				if res[i] > restot[i]:
					restot[i] = res[i]
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
	
	som+=restot[0]*restot[1]*restot[2]
	res=[0,0,0]
	restot=[0,0,0]
	nombre=""
	couleur=""
print(som)