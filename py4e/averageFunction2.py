# using a list

numList = []


# taking inputs from multiline and closing the loop with a blank input. 

while True: 
    x = input()
    if x:
        x = float(x)
        numList.append(x)
    else:
        break

avg = round(sum(numList) / len(numList), 2)

print('Average: ', avg)