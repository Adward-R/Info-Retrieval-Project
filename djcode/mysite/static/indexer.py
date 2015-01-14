#############################################################################
#oh, no, I can not use chinese in this file ,sh*t
#index V0.1,
#read file start from 1.txt to *.txt
## added (use replace instand) ###no re lib
#--such as , . ; : ' " is in the index...   :(
#differ lower like 'a' and upper 'A'
## added ###did not use stop words
#did not use stemming
###########################################################################
import sys, os
stopwords = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also","although","always","am","among", "amongst", "amoungst", "amount",  "an", "and", "another", "any","anyhow","anyone","anything","anyway", "anywhere", "are", "around", "as",  "at", "back","be","became", "because","become","becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom","but", "by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven","else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own","part", "per", "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thickv", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the");


def read():
	print '###############start###########################################################'
	n= -1
	index= []
	path= sys.path[0]#.replace(':\\',':')
	#sum=open(path+ "/sum.txt","w")
	while 1:
		#open file ,if fail write back?
		n= n+1
		try:
			if (n==845):
				break
			else:
				f= open(path+ "/docs/"+str(n)+".txt","r")
		except IOError:
			continue
		print "analyzing the NO.%d doc"%n
		#read file
		i= 0

		line= f.readline()
		for line in f:
			i=i+1

			########################################################
			templine= line.lower() #change to lower
			templine= change(templine)
			#add delet ,.;':"@&(**^$%#$%@$#^*&( and so on
			templine= templine.replace('"',' ')
			templine= templine.replace("'",' ')
			templine= templine.replace(',',' ')
			templine= templine.replace('.',' ')
			templine= templine.replace(':',' ')
			templine= templine.replace(';',' ')
			templine= templine.replace('=',' ')
			templine= templine.replace('?',' ')
			templine= templine.replace('~',' ')
			templine= templine.replace('`',' ')
			templine= templine.replace('_',' ')
			templine= templine.replace('+',' ')
			templine= templine.replace('-',' ')
			templine= templine.replace('*',' ')
			templine= templine.replace('@',' ')
			templine= templine.replace('$',' ')
			templine= templine.replace('#',' ')
			templine= templine.replace('%',' ')
			templine= templine.replace('^',' ')
			templine= templine.replace('&',' ')
			templine= templine.replace('|',' ')
			templine= templine.replace('!',' ')
			templine= templine.replace('/',' ')
			templine= templine.replace('\\',' ')
			templine= templine.replace('(',' ')
			templine= templine.replace(')',' ')
			templine= templine.replace(']',' ')
			templine= templine.replace('[',' ')
			templine= templine.replace('}',' ')
			templine= templine.replace('{',' ')
			templine= templine.replace('<',' ')
			templine= templine.replace('>',' ')
			templine= templine.replace('0',' ')
			templine= templine.replace('1',' ')
			templine= templine.replace('2',' ')
			templine= templine.replace('3',' ')
			templine= templine.replace('4',' ')
			templine= templine.replace('5',' ')
			templine= templine.replace('6',' ')
			templine= templine.replace('7',' ')
			templine= templine.replace('8',' ')
			templine= templine.replace('9',' ')
			editline= templine.split()

			#################################################
			#start routine to read word
			for word in editline:
				try:
					#if in the stop words ,continue
					stopwords.index(word)
					continue
				except ValueError:
					try:
						#if word is in index,add [doc,place]
						k= index.index(word)
						index[k+1].append([n,i])
					except ValueError:
						#else add word,add [[doc,place]]
						index.append(word)
						index.append([[n,i]])

		f.close()
		#some information of the doc analyze
		#sum.write("doc %d "%n)
		#sum.write("has %d lines\n"%i)
	#sum.close()
	print "start to write the index file"
	#print the index in the result file
	i= 0

	if not os.path.exists('index'):
		os.mkdir('index')
	while 1:
		try:
			#read index such as ['a',[[1,2],[1,3]],.........
			word= index[i]
			newdoc= path + '/index/' + word
			print 'writing the index of '+ word
			f= open(newdoc,'w')
			post= index[i+1]  #post is [[1,2],[1,3],......
			i= i+2
			#f.write(word)
			#f.write('\n')
			#read post such as [[1,2],[1,3],......
			j= 0
			t= 0
			count= 0
			query =''
			while 1:
				try:
					#read point in post such as [1,2]
					node= post[j] #node is [1,2]
					a= node[0]
					b= node[1]
					if a==t:
						query= query+ ":%d"%b
						count= count+ 1
					else :
						if t!=0:
							f.write("%d:"%count)
							f.write(query)
							f.write("\n")
						query= "%d"%b
						f.write("%d:"%a)
						count =1
						t= a
					j=j+1

				except IndexError:
					#out of post, break
					f.write("%d:"%count)
					f.write(query)
					f.write("\n")
					#f.write('\n')
					#f.write(word)
					#f.write(' appear %d times' %j)
					break

			f.close()
		except IndexError:
			#out of index, break
			break

	#end.............
	print 'the work finish'
	print '###############finish###########################################################'

def change(str):
	newstr= ''
	for char in str:
		if ord(char)> 127:
			newstr+= ' '
		else:
			newstr+= char
	return newstr

def main():

	read()

if __name__ == '__main__':
	main()
