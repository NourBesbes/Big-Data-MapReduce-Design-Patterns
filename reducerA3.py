#!/usr/bin/python
import sys
nb= 0
oldDay = None
salesTotal = 0

for line in sys.stdin: 
	data = line.strip().split("\t")
	if len(data) != 2:
		continue
	thisDay, thisSale= data
	if oldDay and oldDay != thisDay:
		print "{0}\t{1}".format(oldDay,salesTotal/nb)
		salesTotal = 0
		nb= 0
        
	oldDay = thisDay
	salesTotal += float (thisSale)	
	nb += 1
if oldDay!= None:
	print oldDay,"\t", (salesTotal/nb)
