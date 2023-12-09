import sys
import time
start = time.time() 
part=start
input=open(sys.argv[1],"r")
lines=input.readlines()
listforcestr="23456789TJQKA"#on se sert des indoce pour savoir qui est le plus fort
listmain=[]
def Combiencarac(main):
	res=0
	listdejavu=[]
	for char in main :
		if char not in listdejavu:
			listdejavu.append(char)
			res+=1
	return res
def Ordre(main1,main2):
	"""return 1 pour la main 1 plus grande sinon 2"""
	for i in range(5):
		if listforcestr.index(main1[i]) > listforcestr.index(main2[i]):
			return 1
		elif listforcestr.index(main1[i]) < listforcestr.index(main2[i]):
			return 2
	return 2 #si il sont egaux on considere que main2 est plus grand (plus facile pour le tri bulle)
def Typemain3(main):
	"""retrun True pour pour un Brelan et False pour une double pair"""
	for char in main :
		if main.count(char) == 3 :
			return True
		elif main.count(char) == 2 :
			return False
def Typemain2(main):
	"""True pour Full et False pour Four of kind"""
	for char in main :
		if main.count(char)==2 or main.count(char) == 3:
			return True
		elif main.count(char) == 4 or main.count(char) ==1:
			return False
def Crealistmain(lines):
	for line in lines:
		main = line[0:5]
		bid = line[6:].replace(" ","")
		bid = bid.replace("\n","")
		listmain.append((main,bid))
	return listmain
def Tribulle(listmain) :
	l=len(listmain)#indice final
	for t in range(len(listmain)-1):
		main1=listmain[0][0]
		iold=0
		for i in range(1,l):
			if Ordre(main1,listmain[i][0]) == 2 :#listmain[i] plus > ou =
				listmain.insert(i,listmain[iold])
				del(listmain[iold])
				iold=i
				main1=listmain[i][0]
			elif i == l-1:
				listmain.insert(i+1,listmain[iold])
				del(listmain[iold])
		l-=1
	return listmain
def Tritypemain(listmain):
	# global listFive, listFour, listFull, listThree, list2Pair, listPair, listHigh
	for main in listmain:
		# print(main[0])
		if Combiencarac(main[0]) == 5 :
			listHigh.append(main)
		elif Combiencarac(main[0]) == 4 :
			listPair.append(main)
		elif Combiencarac(main[0]) == 1 :
			listFive.append(main)
		elif Combiencarac(main[0]) == 3 : #ici deux possibilites
			if Typemain3(main[0]) :#brelan
				listThree.append(main)
			else:
				list2Pair.append(main)
		elif Combiencarac(main[0]) == 2 : #ici deux possibilites aussi
			if Typemain2(main[0]) :#Full
				listFull.append(main)
			else :
				listFour.append(main)
listmain = Crealistmain(lines)
listFive, listFour, listFull, listThree, list2Pair, listPair, listHigh = [],[],[],[],[],[],[]
som=0
Tritypemain(listmain)
listHigh=Tribulle(listHigh)
listPair=Tribulle(listPair)
list2Pair=Tribulle(list2Pair)
listThree = Tribulle(listThree)
listFull=Tribulle(listFull)
listFour=Tribulle(listFour)
listFive=Tribulle(listFive)
listmain2 = listHigh+listPair+list2Pair+listThree+listFull+listFour+listFive
for i in range(len(listmain2)):
	som+=int(listmain2[i][1])*(i+1)
print(som)
print("Durée part1 : %s" % (time.time()-part))
part=time.time()
#part2
listFive, listFour, listFull, listThree, list2Pair, listPair, listHigh = [],[],[],[],[],[],[]
som=0
listforcestr='J23456789TQKA'
def Combiencarac2(main):
	if "J" not in main :
		return Combiencarac(main)#ok
	else :
		main = main.replace("J","")
		return Combiencarac(main)
def Typemain2_2(main):
	if "J" not in main :
		return Typemain2(main)
	else :
		countj = main.count("J")
		if countj==1:
			for char in main :
				if main.count(char) == 3:
					return False
			return True
		return False
def Typemain3_2(main):
	if "J" not in main:
		return Typemain3(main)
	else:
		return True #forcement un brelan
def Tritypemain2(listmain):
	global listFive, listFour, listFull, listThree, list2Pair, listPair, listHigh
	for main in listmain:
		if Combiencarac2(main[0]) == 5 :
			listHigh.append(main)
		elif Combiencarac2(main[0]) == 4 :
			listPair.append(main)
		elif Combiencarac2(main[0]) == 1 :
			listFive.append(main)
		elif Combiencarac2(main[0]) == 3 : #ici deux possibilites
			if Typemain3_2(main[0]) :#brelan
				listThree.append(main)
			else:
				list2Pair.append(main)
		elif Combiencarac2(main[0]) == 2 : #ici

			if Typemain2_2(main[0]) :#Full
				listFull.append(main)
			else :
				listFour.append(main)

		elif Combiencarac2(main[0])==0:
			listFive.append(main)	
Tritypemain2(listmain)
listHigh=Tribulle(listHigh)
listPair=Tribulle(listPair)
list2Pair=Tribulle(list2Pair)
listThree = Tribulle(listThree)
listFull=Tribulle(listFull)
listFour=Tribulle(listFour)
listFive=Tribulle(listFive)
listmain2 = listHigh+listPair+list2Pair+listThree+listFull+listFour+listFive
for i in range(len(listmain2)):
 	som+=int(listmain2[i][1])*(i+1)
print(som)
start = time.time()-start
print("Durée part2 : %s" % (time.time()-part))
print("Durée totale : %s" % (start))
