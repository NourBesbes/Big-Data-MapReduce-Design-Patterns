#!/usr/bin/python
import sys
import string

last_author_id = None
cur_parent_id = "-"
cur_id ="-"
cur_title= "-"
cur_tagnames= "-"
cur_node_type= "-"
cur_parent_id= "-"
cur_abs_parent_id= "-"
cur_added_at= "-"
cur_score= "-"
cur_reputation= "-"
cur_gold= "-"
cur_silver= "-"
cur_bronze= "-"

for line in sys.stdin:
	line = line.strip()
	id ,title,tagnames,author_id,node_type,parent_id,abs_parent_id,added_at,score,reputation,gold,silver,bronze = line.split("\t")

	if not last_author_id or last_author_id != author_id:
		last_author_id = author_id
		cur_parent_id = parent_id
		cur_id =id
		cur_title= title
		cur_tagnames= tagnames
		cur_node_type= node_type
		cur_parent_id= parent_id
		cur_abs_parent_id= abs_parent_id
		cur_added_at= added_at
		cur_score=score
		cur_reputation= reputation
		cur_gold= gold
		cur_silver= silver
		cur_bronze= bronze
	elif author_id == last_author_id:
		parent_id=cur_parent_id
		id=cur_id
		title=cur_title
		tagnames=cur_tagnames
		node_type=cur_node_type
		parent_id=cur_parent_id 
		abs_parent_id=cur_abs_parent_id
		added_at=cur_added_at
		score=cur_score
		reputation=cur_reputation
		gold=cur_gold
		silver=cur_silver
		bronze=cur_bronze 
		print "{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\t{10}\t{11}\t{12}".format(id,title,tagnames,author_id,node_type,parent_id,abs_parent_id,added_at,score,reputation,gold,silver,bronze)









