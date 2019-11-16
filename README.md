# Instant-Markup
Create HTML program for plain text
#Problem
#You want to add some formatting to a plain text file.
#Instead of adding all the necessary tags manually, you want your program to do it 
#automatically.
#Your task is basically to classify various text elements, such as headlines and 
#emphasized text, and then clearly mark them.
#In the specific problem addressed here, you add HTML markup to the text, so the 
#resulting document can be displayed in a Web browser and used as a Web page. 


#Specific Goals
#The input shouldn’t be required to contain artificial codes or tags.
#You should be able to deal both with different blocks, such as headings, paragraphs, 
#and list items, as well as inline text, such as emphasized text or URLs.
#Although this implementation deals with HTML, it should be easy to extend it to other
#markup languages.

#Useful Tools
#You certainly need to read from and write to files or at least read from standard input (sys.stdin) and output with print. 
#You probably need to iterate over the lines of the input
#you need a few string methods
#perhaps you’ll use a generator or two
#you probably need the re module


#Preparations
#you need some way of assessing your progress; you need a test suite.
#a sample text that you want to mark up automatically.


#First Implementation
#One of the first things you need to do is split the text into paragraphs. 
#paragraphs are separated by one or more empty lines
#A better word than “paragraph” might be “block” because this name can apply to 
#headlines and list items as well.
#collect all the lines you encounter until you find an empty line,
#then return the lines you have collected so far. That would be one block.


#Adding Some Markup
#Print some beginning markup.
#For each block, print the block enclosed in paragraph tags.
#Print some ending markup.
