# This small program find the square root of a given input/number. 

s = float(input('The number you want to do squrt: '))

def squrt(x):
    g = 1.0
    n = 1
    while g * g != x:
        g = (g + (x / g))/2
        n = n + 1
        if n >= 1000:
            break

    return g

print(f'Square Root of {s} =    {round(squrt(s), 4)}')
