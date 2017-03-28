#!/usr/bin/python
import sys
from datetime import datetime

day = 0

for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) == 6:
		date, time, store, item, cost, payment = data
		day = datetime.strptime(date,"%Y-%m-%d").weekday()
        	print "{0}\t{1}".format(day,cost)
