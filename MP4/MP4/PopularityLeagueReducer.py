#!/usr/bin/env python3
import sys
#TODO

links = []
ranks = []
# input comes from STDIN
for line in sys.stdin:
    # TODO
    line = line.rstrip('\n')
    link, count = line.split('\t')
    links.append((link, count))
    ranks.append(int(count))

links.sort(key=lambda l: (int(l[0])), reverse=True)
ranks.sort()

for pair in links:
    link, count = pair
    rank = ranks.index(int(count))
    output = link + '\t' + str(rank)
    print(output)


#TODO
# print('%s\t%s' % (  ,  )) print as final output