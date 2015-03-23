# Code for calculating running median for number of words per line for each line in the wc_input directory.
# The resulting running median is then outputted to a text file named med_results in the wc_output directory

# To run the code please create three folders named 'temp', 'wc_output' and 'wc_input' in C folder of your computer
# without which the code generates error

# Packages used for executing the following code
import os
import fileinput
import glob
import heapq    # used for heap sort (Data Structure)

os.chdir('wc_input')  # Changing input directory to wc_input where all input text files are present
# print os.getcwd() # Prints the present directory

filenames=[]
for file in sorted(glob.glob('*.txt')):    #  Sorts the files in alphabetical order
    filenames.append(file)
#print filenames
concatenate="\n".join([open(f).read() for f in filenames])  # Concatenates the text of all files in new lines every time
#print concatenate

text_file=open("wc_output",'w+')  # Creating a text file of all the concatenated text from all text files in the put directory to temp folder in C drive
text_file.seek(0)
text_file.write(concatenate) # Writing text in concatenate
text_file.close()

# Genarating a list for number of words in each line
words=[]
with open('wc_output','r') as in_file:
    for line in in_file.readlines():
       words.append(len(line.split(' ')))
#print words

# Function for Heap sort (Data Structure)
def heapsort(iterable):
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for i in range(len(h))]

# Function for calculating median of a list of numbers
def medi(lst):
    if len(lst) < 1:
            return None
    if len(lst) %2 == 1:
            return lst[((len(lst)+1)/2)-1]
    if len(lst) %2 == 0:
            return float(sum(lst[(len(lst)/2)-1:(len(lst)/2)+1]))/2.0

# Creating a dictionary which holds the numbers in incremental order for which running median is calculated
myDict={}
counter=0
for inte in range(0,len(words)):
    myList=[]
    median=0
    for no in range(0,inte+1):
        myList.append(words[no])
    myDict[counter]=heapsort(myList)
    counter+=1
#print myDict
#creating list of running Medians
medianList=[]
for key in range(0,len(myDict)):
    temp=myDict[key]
    medianList.append(medi(temp))
#print medianList
# Writing the list of running medians wc_output in directory
counter=0
with open('wc_output','w+') as out_file:
    for item in medianList:
        out_file.write(str(medianList[counter])+"\n")
        counter +=1
out_file.close()




