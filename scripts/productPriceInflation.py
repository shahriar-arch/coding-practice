x = float(input("Enter Product Price: "))
y = float(input("Enter Inflation Rate: "))
z = float(input("Enter Period - Months: "))

price = x
irate = (y / 100) / 12
period = z
month = 1

print("")
while month <= period:
    iprice = price + (price * irate)
    price = iprice
    price = round(price)
    print("Price after month", month, "......", price)
    month += 1

print("")
print("thank you!")