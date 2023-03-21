#!/usr/bin/env python3
import sys


#TODO

linkmap = {}

for line in sys.stdin:
  # TODO
  line = line.rstrip('\n')
  src, dst = line.split('\t')
  if src not in linkmap:
    linkmap[src] = False
  if src != dst:
    linkmap[dst] = True

res = []
for src, visited in linkmap.items():
  if not visited:
    res.append(int(src))
res.sort()
for r in res:
  print(r)

#TODO
# print(xx) print as final output