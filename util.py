#split the text into block
#collect all the lines you encounter until you find an empty line, and then return the lines you have collected so far. 
#That would be one block. Then, you could start all over again. You needn’t bother collecting empty lines, and you won’t return empty 
#blocks (where you have encountered more than one empty line).

from __future__ import generators

#The lines generator is just a utility that tucks an empty line onto the end of the file.
def lines(file):
  for line in file: yield line 
    yield '\n'
    
def blocks(file): 
  block = []
  for line in lines(file): 
    if line.strip():
      block.append(line) 
    elif block:
      yield ''.join(block).strip() #gives you a single string representing the block, with excessive whitespace at either end 
      #(such as list indentations or newlines) removed.
      block = []


# you should make sure that the last line of the file is empty; otherwise you won’t know when the last block is finished. 
