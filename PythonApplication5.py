
import collections 
import string

def unique(inputList):
    returnObject = []
    for x in inputList: 
        if removePunct(x) not in returnObject: 
            returnObject.append(removePunct(x))
    return returnObject

def removePunct(inputString):
    returnObject = inputString
    exclude = set(string.punctuation) 
    returnObject = ''.join(ch for ch in returnObject if ch not in exclude)
    return returnObject

# read in the movie from the file 

with open("./beeMovie.txt") as file: 
    script = file.read()
#create temp dict
temp = dict()

#get unique and count the number of those words
for x in unique(script.split()):
    temp["[" + str(x) + "] : "] = script.split().count(x)

#sort that shit 
temp = sorted(temp.items(),key=lambda x: x[1])

#count all the words used when stripped punc
counter = 0
for z in temp: 
    counter = counter + z[1]
#print all unique with count and then the ratio of (word count / total word count)
for y in temp:
    print(str(y) + " is " + str(y[1]/counter))

