x = 199999
itersLeft = x
ans = 0
while itersLeft != 0:
    ans = ans + x
    itersLeft -= 1
print(f"{x} * {x} = {ans}")