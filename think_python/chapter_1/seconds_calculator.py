def seconds_calculator(input_year, input_month, input_day, input_hour, input_min, input_seconds):
    """ A function to calculate seconds"""
    
    total_month = input_year * 12 # converting input year to month
    total_day = (total_month + input_month) * 30.4375 # converting total month to day, assuming a 4 year cycle 
    total_hour = (total_day + input_day) * 24 # converting total day to hour
    total_min = (total_hour + input_hour) * 60 # convering total hour to min 
    total_seconds = ((total_min + input_min) * 60) + input_seconds # converting total min to seconds
    
    return total_seconds


# take inputs from the user

year = float(input("Year: "))
month = float(input("Month: "))
day = float(input("Day: "))
hour = float(input("Hour: "))
min = float(input("Minute: "))
sec = float(input("Second: "))

final_output = seconds_calculator(year, month, day, hour, min, sec)

print("Total Seconds:", final_output)
