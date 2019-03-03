import re
import copy
class transcation:
	def __init__(self,id,size,fee):
		self.id = id
		self.size = size
		self.fee = fee

def addfee(used,id,cursize,fee,a,MAX_SIZE):
	used.append(id)
	MAX_FEE = 0
	for i in range(id,len(a)):
	 	if a[i].id not in used:
	 		if cursize + a[i].size < MAX_SIZE:
	 			curfee = addfee(copy.copy(used),a[i].id,cursize + a[i].size,fee+a[i].fee,a,MAX_SIZE)
	 			print(cursize)
	 			if curfee > MAX_FEE:
	 				MAX_FEE=fee
	return fee + MAX_FEE

MAX_SIZE =  1000000 
MAX_FEE = 0

with open('input-for-the-quiz.txt') as f:
	line = f.readline()
	a = []
	while line :
		line = f.readline()
		elements = re.split("\\s+",line);
		if(len(elements)>=3):
			t = transcation(int(elements[0]),int(elements[1]),float(elements[2]))
			a.append(t)
used = []
for i in range(0,len(a)):
	fee = addfee(copy.copy(used),a[i].id, a[i].size,a[i].fee,a,MAX_SIZE)
	if fee > MAX_FEE:
		MAX_FEE = fee

print (MAX_FEE +12.5)