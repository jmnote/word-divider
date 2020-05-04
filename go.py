#!/usr/local/bin/python3


rules = [
['\s+',' '],
['그곳에서','그 곳에서'],
]

import re
import sys

if len(sys.argv) != 3:
  print('Usage:')
  print("$ python3 go.py 1.txt 2.txt\n")
  quit()

filename1 = sys.argv[1]
filename2 = sys.argv[2]

f1 = open(filename1, "rt", encoding="UTF8")
f2 = open(filename2, "w")

print( f'=> input file: {filename1}' )
print( f'=> output file: {filename2}' )

for line in f1:
  for rule in rules:
    line = re.sub(rule[0], rule[1], line)
  print( line )
  f2.write(line + "\n")

f1.close()
f2.close()

print( "=> Done...\n" )

