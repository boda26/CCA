#!/usr/bin/env python3
import sys

linkmap = {}

# input comes from STDIN
for line in sys.stdin:
    # TODO
    line = line.rstrip('\n')
    src, dst = line.split('\t')
    if src != dst:
        linkmap[dst] = linkmap.get(dst, 0) + 1

links = list(linkmap.items())
links.sort(key=lambda l: (l[1], l[0]))

for link, count in links:
    output = link + '\t' + str(count)
    print(output)
