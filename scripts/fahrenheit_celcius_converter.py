inp = input("Enter Fahrenheit Temperature: ")
try:
    fahr = float(inp)
    cel = round((fahr - 32.0) * 5.0 / 9.0)
    print(f"Celsius Temperature: {cel}")
except:
    print("Please enter a number!")
