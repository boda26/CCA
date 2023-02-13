#!/usr/bin/env python3
import sys


for line in sys.stdin:
  # TODO
  line = line.rstrip('\n')
  line = line.split(': ')
  src, dst = line[0], line[1].split()
  for d in dst:
    output = src + '\t' + d
    print(output)
  
  # print('%s\t%s' % (  ,  )) pass this output to reducer
