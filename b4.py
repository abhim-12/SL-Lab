import sys
import os
from functools import reduce

mydict = {}
mylist=[]
wordLen = []

if(len(sys.argv) != 2):
	print ("Invalid Arguments")
	sys.exit()

if(not(os.path.exists(sys.argv[0]))):
	print ("Invalid File Path")
	sys.exit()

if(sys.argv[1].split('.')[-1] != "txt"):
	print ("Invalid File Format. Only TXT files allowed")
	sys.exit()

with open(sys.argv[1]) as f:
	s=f.read();
	mylist=s.split()
	for x in mylist:
		temp=mylist.count(x)
		mydict[x]=temp

print(mydict)

sortedDict = sorted(mydict.items(), key=lambda dictItem: dictItem[1], reverse=True)

for i in range(10):
	try:
		wordTuple = sortedDict[i]
		wordLen.append(len(wordTuple[0]))
		print (wordTuple[0], "	Frequency: " , wordTuple[1] , "	Length: " , len(wordTuple[0]))
	except IndexError:
		print ("File has less than 10 words")
		break

print ("Lengths of 10 most frequently occuring words:")
print (wordLen)

sum = reduce(lambda x,y: x+y, wordLen)
print ("Average length of words: " , sum/len(wordLen))

squares = [x**2 for x in wordLen if x%2 != 0]
print ("Squres of odd word lengths: ")
print (squares)