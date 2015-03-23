# Code for Word Count that counts all the words from text files contained in a directory named wc_input and outputs the count (in alphabetical order)to a
# file named wc_results.txt which is placed in the directory named wc_output
# for this code to work there should be two directories 'wc_input - All input files are placed' and 'wc_output' should be created in 'D' Drive
# I have used print statement everywhere to check my results which are not necessary.
# packages Used
import os
import fileinput
import glob
# Changig Directory
os.chdir('wc_input')
#print os.getcwd()
# Ordering the files in the directory in alphabetical order
filenames=[]
for file in sorted(glob.glob('*.txt')):    #  Sorts the files in alphabetical order
    filenames.append(file)
#print filenames
# Concatenating the text in all files
concatenate="".join([open(f).read() for f in filenames])
#print concatenate
#Creating a dictionary of all words with the no. of times it appeared
wordcount={}
for word in concatenate.split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] +=1
#print wordcount
# Writing the dictionary to a text file in output directory
with open('wc_output/wc_results.txt','w+') as out_file:
    for word in sorted(wordcount.items()):
        out_file.write("%s:%s\n" % word)
