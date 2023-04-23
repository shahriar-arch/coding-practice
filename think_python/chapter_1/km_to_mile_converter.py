# Define a function that converts kilometer to mile 

def km_to_mile(input_km):
    mile = input_km * (1 / 1.61)
    return mile 

km = 10
mile = km_to_mile(km)
print(mile)