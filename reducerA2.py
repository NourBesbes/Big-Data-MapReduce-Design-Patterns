#!/usr/bin/python
import sys

nbOccurances = 0
oldWord = None
listNodes = []

for line in sys.stdin: 
	data = line.strip().split("\t")
	thisWord, thisNode = data


	if oldWord and oldWord.lower() != thisWord.lower():
		listNodes.sort(key=lambda listNodes:(str)(listNodes))
		print "{0}\t{1}\t{2}".format(oldWord,nbOccurances,listNodes)
        	listNodes = []
        	nbOccurances = 0
	oldWord = thisWord
	nbOccurances += 1
	if thisNode not in listNodes:
		listNodes.append(thisNode);	
	

if oldWord != None:
    listNodes.sort(key=lambda listNodes:(str)(listNodes))
