#!/usr/bin/python
import sys
for line in sys.stdin:
    # Setting some defaults
	author_id = ""
	parent_id = "-"
	id ="-"
	title= "-"
	tagnames= "-"
	node_type= "-"
	parent_id= "-"
	abs_parent_id= "-"
	added_at= "-"
	score= "-"
	reputation= "-"
	gold= "-"
	silver= "-"
	bronze= "-"

	line = line.strip()
	splits = line.split("\t")
	if len(splits) == 19: # forum_users have 5 columns 
		id = splits[0]
		tagnames= splits[2]
		author_id = splits[3]
		parent_id= splits[6]
		abs_parent_id= splits[7]
		added_at= splits[8]
		score=splits[9] 		
		
	if len(splits) == 5:
		author_id = splits[0]
		reputation = splits[1]
		gold= splits[2]
		silver= splits[3]
		bronze= splits[4]
		
		                
	print "{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\t{10}\t{11}\t{12}".format(id,title,tagnames,author_id,node_type,parent_id,abs_parent_id,added_at,score,reputation,gold,silver,bronze)
