import time
import sys
filename = sys.argv[1]
firstdigit = "0"
lastdigit = "0"
firstfound = False 
som = 0 
strmaybe=""
start = time.time()
input = open(filename,"r")
lines = input.readlines()

strcorrect_list = ["one","two","three","four","five","six","seven","eight","nine"] #liste des chaines corrects
char_pos_correct = [[],[],[],[],[]] #5 listes qui contienne chaque lettre des nombres ecrit en str selon leur position

def Poslettre(strcorrect_list,char_pos_correct): #la liste de toute les liste des n ième lettre correct
	for strcorrect in strcorrect_list: #on prends "one" "two" etc...
		for i in range(len(strcorrect)):
			if strcorrect[i] not in char_pos_correct[i]: # on evite les doublons
				char_pos_correct[i].append(strcorrect[i])
	return char_pos_correct 

char_pos_correct = Poslettre(strcorrect_list,char_pos_correct)

def Cheskcharstr(strmaybe,char_pos_correct):
	for i in range(len(strmaybe)):
		if strmaybe[i] not in char_pos_correct[i]:
			return ""
	return strmaybe
def Cheskcharstrinverse(strmaybe,char_pos_correct):
	strmaybe="".join(reversed(strmaybe))
	print(strmaybe)
	for i in range(len(strmaybe)):
		if strmaybe[i] not in char_pos_correct[i]:
			return ""
	return strmaybe

def Cheskstr(strmaybe,strcorrect_list):
 	#if len(strmaybe) < 3 :
 		#return False
 	for strcorrect in strcorrect_list:
 		if strmaybe == strcorrect:
 			return True
 	return False
def Cheskstrinverse(strmaybe,strcorrect_list):
 	strmaybe = "".join(reversed(strmaybe))
 	for strcorrect in strcorrect_list:
 		if strmaybe == strcorrect:
 			return True
 	return False 	

for line in lines :
	line=line.strip()
	for char in line :
		if not firstfound: 
			if char.isdigit() : #si c'est un entier
				firstdigit = char
				firstfound = True
				strmaybe=""
				break
			else : #pas un char
				#print(firstfound)#bug 
				#print('False normalement')
				strmaybe+=char
				strmaybe=Cheskcharstr(strmaybe,char_pos_correct)
				if Cheskstr(strmaybe,strcorrect_list) :
					#print("coucou")
					firstdigit = str(strcorrect_list.index(strmaybe)+1)
					firstfound = True #pUAITNsdf 
					strmaybe=""
					break
	line="".join(reversed(line))
	for char in line :
		if char.isdigit():
			lastdigit = char
			break #on coupe tout
		else:
			strmaybe+=char
			#print(strmaybe)
			strmaybe=Cheskcharstrinverse(strmaybe,char_pos_correct)
			if Cheskstrinverse(strmaybe,strcorrect_list):
				strmaybe = "".join(reversed(strmaybe))
				lastdigit = str(strcorrect_list.index(strmaybe)+1)
				break
	som+= int(firstdigit+lastdigit)
	strmaybe=""
	firstfound = False	
print(som)
end = time.time()
print(end-start)
