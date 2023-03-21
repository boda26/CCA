#!/usr/bin/env python3
import sys


leaguePath = sys.argv[1]
#TODO

league = set()
with open(leaguePath) as f:
	#TODO
       for line in f:
              line = line.rstrip('\n')
              league.add(line)


for line in sys.stdin:
       #TODO
       line = line.rstrip('\n')
       link, count = line.split('\t')
       if link in league:
              output = link + '\t' + count
              print(output)


       # print('%s\t%s' % (  ,  )) pass this output to reducer
