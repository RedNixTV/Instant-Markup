from __future__ import generators
import sys, re
from util import *

#Print some beginning markup.
print ('<html><head><title>...</title><body>')

title = 1
#For each block, print the block enclosed in paragraph or heading tags.
for block in blocks(sys.stdin):
	block = re.sub(r'\*(.+?)\*', r'<em>\1</em>', block) #replace any text enclosed in asterisks with emphasized text (using em tags). 
  #enclose the first block in heading tags
	if title:
		print ('<h1>') 
		print (block)
		print ('</h1>')
		title = 0
  #enclose all other block in paragraph tags
	else:
		print ('<p>')
		print (block) 
		print ('</p>')
    
#Print some ending markup.
print ('</body></html>')
