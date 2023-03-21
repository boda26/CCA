#!/usr/bin/env python3
from operator import itemgetter
import sys

#TODO
wordmap = {}

# input comes from STDIN
for line in sys.stdin:
    # TODO
    line = line.rstrip('\n')
    line = line.split('\t')
    word, ct = line[0], line[1]
    if word not in wordmap:
        wordmap[word] = 1
    else:
        wordmap[word] += 1

for word, ct in wordmap.items():
    output = word + '\t' + str(ct)
    print(output)

# TODO
# print('%s\t%s' % (  ,  )) print as final output