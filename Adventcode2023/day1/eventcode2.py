import sys
filename = sys.argv[1]
firstdigit = 0
lastdigit = 0 
firstfound=False
som = 0 
strnumber=["one",'two','three','four','five','six','seven','eight','nine']
input = open(filename,'r')
lines=input.readlines()

for line in lines:
	line=line.strip()
	for i in range(len(line)):
		if line[i].isdigit():
			firstdigit=line[i]
			# lastdigit=char
			firstfound=True
		else :
			for number in strnumber:

				if line[i:i+len(number)] == number:
					firstdigit=str(strnumber.index(number)+1)
					firstfound=True
					break
		if firstfound :
			#print('coucou')
			firstfound=False
			break

	for i in range(len(line)-1,-1,-1):
		if line[i].isdigit():
			lastdigit=line[i]
			firstfound=True
		else :
			for number in strnumber:
				if line[i:i+len(number)] == number:
					lastdigit=str(strnumber.index(number)+1)
					firstfound=True
					#print("trouver")
					break
		if firstfound:
			break
	print(firstdigit+lastdigit)
	som+=int(firstdigit+lastdigit)
	firstdigit='0'
	lastdigit='0'
	firstfound=False

print(som)


