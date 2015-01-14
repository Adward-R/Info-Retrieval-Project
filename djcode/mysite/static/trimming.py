import os
def main():
	toBeDeleted = []
	for i in range(845):
		for j in range(i+1,845):
			if (j in toBeDeleted) or (i in toBeDeleted):
				continue
			fr1 = open('./docs/'+str(i)+'.txt','r')
			fr2 = open('./docs/'+str(j)+'.txt','r')
			vect = {}
			for line in fr1:
				tmpline = line.replace('"',' ').replace("'",' ').replace('-',' ').replace(',',' ').replace('.',' ').replace('(',' ').replace(')',' ').replace('<',' ').replace('>',' ').replace('\n',' ').replace('\t',' ')
				for word in tmpline.split():
					if vect.has_key(word):
						vect[word][0] += 1
					else:
						vect[word] = [1,0]
			for line in fr2:
				tmpline = line.replace('"',' ').replace("'",' ').replace('-',' ').replace(',',' ').replace('.',' ').replace('(',' ').replace(')',' ').replace('<',' ').replace('>',' ').replace('\n',' ').replace('\t',' ')
				for word in tmpline.split():
					if vect.has_key(word):
						vect[word][1] += 1
					else:
						vect[word] = [0,1]
			fr1.close()
			fr2.close()
			length1 = 0
			length2 = 0
			innerProduct = 0
			for key in vect.keys():
				innerProduct += vect[key][0] * vect[key][1]
				length1 += vect[key][0] * vect[key][0]
				length2 += vect[key][1] * vect[key][1]
			simi = innerProduct*innerProduct*1.0 / (length1*length2)
			print str(i)+' '+str(j)+' '+str(simi)
			if simi>0.7:
				toBeDeleted.append(j)
	#print toBeDeleted
	for i in toBeDeleted:
		os.remove('./docs/'+str(i)+'.txt')
	
if __name__ == '__main__':
	main()