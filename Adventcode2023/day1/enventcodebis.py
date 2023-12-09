import time
import sys
filename = sys.argv[1]
firstdigit = 0
lastdigit = 0
onlyfirst= True 
foundfirstdigit = False
som = 0 
start = time.time()
input = open(filename,"r")
lines = input.readlines()
for line in lines :
	for char in line :
		if char.isdigit() : #si c'est un entier
			if foundfirstdigit == False : #si c'est le premier de la ligne
				firstdigit = char
				foundfirstdigit = True 
			else :
				lastdigit = char
				if onlyfirst :
					 onlyfirst = False
	if onlyfirst :
		print(firstdigit+firstdigit)
		som += int(firstdigit+firstdigit)
	else:
		print(firstdigit+lastdigit)
		som += int(firstdigit+lastdigit)
	onlyfirst=True
	foundfirstdigit = False

print(som)
end = time.time()
print(end-start)