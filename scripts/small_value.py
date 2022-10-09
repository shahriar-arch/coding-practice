my_list = [9, 41, 12, 3, 74, 15]
# i need to find out the smallest value from the list.

smallest_value = None

for i in my_list:
    if smallest_value is None:
        smallest_value = i 
    elif i < smallest_value:
        smallest_value = i
    print("so far small value is:", smallest_value)

print("smallest value from the list is:", smallest_value)

print("Done")
