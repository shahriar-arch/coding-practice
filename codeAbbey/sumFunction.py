
# writing the sum function for a a list
# It is unnecessary, because we can use built in sum() function to calculate the sum of a list 
def sumList(x):
    s = 0 #sum of the list 
    for i in x:
        s = s + i
    return s

# getting the input from a user and putting them in a list, also converting them from str to float / int 
nums = [float(a) for a in input().split()]

# printing the ans. 
print(sumList(nums))

