#!/usr/local/bin/python3


rules = [
['\s+',' '],
['그곳에서','그 곳에서'],
['([이저그][런라]는?)게',r'\1 게'],
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
f2 = open(filename2, "wt", encoding="UTF8")

print( f'input file: {filename1}' )
print( f'output file: {filename2}' )
print( f'==================================' )

for line1 in f1:
    line2 = line1
    for rule in rules:
        line2 = re.sub(rule[0], rule[1], line2)
    if line1 != line2:
        print( f'>>> {line1} ==> {line2}' )
    f2.write( line2 + "\n" )

f1.close()
f2.close()

print( "=> Done..." )
