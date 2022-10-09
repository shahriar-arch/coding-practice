x = 1.0
y = 2.0
a = 3.0
b = 4.0
c = 5.0
d = 6.0

x = float(input("Enter a number: "))
y = float(input("Guess the sqrt: "))

while y * y != x:
    a = x / y
    y =( a + y) / 2
    print("Auto next guess:", y)

y = str(y)
print(" " + y + " is the correct guess!")


