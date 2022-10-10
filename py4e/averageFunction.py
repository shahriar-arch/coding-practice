#calculating average without list

total = 0
num = 0

# taking multiline input, while look ends when blank input occurs. 
while True: 
    x = input()
    if x:
        x = float(x)
        total = total + x
        num = num + 1
    else:
        break 

avg = round(total / num, 2)

print('Average: ', avg)
