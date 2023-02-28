import sys

def socmed_mapper():
	for line in sys.stdin:
		data = line.strip().split("\t")
		socmed, date, count = data		
		print("%s\t%s\t%s" % (socmed, date, count))