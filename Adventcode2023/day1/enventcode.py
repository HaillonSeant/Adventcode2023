import time
import sys
filename = sys.argv[1]
firstdigit = 0
lastdigit = 0
compteur = 0 #onlyfirst = False
som = 0 
t=1
start = time.time()
input = open(filename,"r")
lines = input.readlines()
for line in lines :
	for char in line :
		if char.isdigit() : #si c'est un entier
			if compteur == 0 : #si c'est le premier de la ligne
				firstdigit = char
				compteur+=1 
			else :
				lastdigit = char
				compteur+=1
	if compteur == 1  :
		som += int(firstdigit+firstdigit)
	else:
		som += int(firstdigit+lastdigit)	
	compteur=0	
print(som)
end = time.time()
print(end-start)





