#!/usr/bin/python
import sys
import re
for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 19:
        node_id, title,tagnames,author_id, body, node_type, parent_id, abs_parent_id, added_at, score, state_string, last_edited_id, last_activity_by_id, last_activity_at,   active_revision_id, extra, extra_ref_id, extra_count, marked = data
        words=re.findall("[\w]+|[.,!?;]",body)
        for word in words:
		if word not in ('.','!','?','#','$','[',']','/','<','>','=','-',':',';','(',')',','):
            		print "{0}\t{1}".format(word,node_id)



