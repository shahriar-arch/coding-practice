"""

Now we are given several pairs of values and we want to calculate sum for each pair.

Input data will contain the total count of pairs to process in the first line.
The following lines will contain pairs themselves - one pair at each line.
Answer should contain the results separated by spaces.

data:
3
100 8
15 245
1945 54

answer:
108 260 1999

"""
# 1st Solution 

# When the number of input is given in the first input

#taking input for no of pair
numPair = int(input())
numInp = 1 #no of input 
numList = []

# taking input for the numbers by using while loop and storing them in a list by nested lists 
while numInp <= numPair:
    x = [int(a) for a in input().split()]
    numList.append(x)
    numInp = numInp + 1

#taking the sum of the nested lists and creating a new list 

sumList = [] # creating a new list for taking the sums of the previous list 

for i in numList:
    s = sum(i) # taking sum of every nested lists 
    sumList.append(s) # inserting the sum in the final list 

#printing the sumlist in a single line by a for loop 
for i in sumList:
    print(i, end = ' ')



"""
#suppose we don't want to use the num of pairs / it is not given 

# this program will work if the last entry is blank. 

# Solution 2

numLine = input() # if the number of input is given in the 1st input

# taking inputs of multiple values across multiple line and storing them in a list and nested lists

numList = []

while True:
    x = [int(a) for a in input().split()]
    if x:
        numList.append(x)
    else:
        break

sumList = []

for i in numList:
    x = sum(i)
    sumList.append(x)

for i in sumList:
    print(i, end = ' ')

"""



