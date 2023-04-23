
# if you run a 10 kilometer race in 42 minutes 42 seconds, 
# what is your average pace (time per mile in minutes and seconds)
# What is your average speed in miles per hour? 

# convert km to mile 
def km_to_mile(input_km):
    mile = input_km * (1 / 1.61)
    return mile 

# conver min and second to second 
def min_and_sec_to_sec(min, sec):
    second = (min * 60) + sec
    return second

# convert second to min and second 
def sec_to_min_and_sec(sec):
    minute = sec // 60
    second = round(sec % 60, 2)
    return minute, second

# convert sec to hour
def sec_to_hour(sec):
    hour = sec * ((1 / 60) / 60)
    return hour

# from the exercise data
distance_km = 10 # given distance in km
g_min, g_sec = 42, 42 # given min and sec

#calculation
#What is your average pace per mile in minutes and seconds
averace_pace_sec_per_mile = min_and_sec_to_sec(g_min, g_sec) / km_to_mile(distance_km)
o_min, o_sec = sec_to_min_and_sec(averace_pace_sec_per_mile) #converting seconds to min and seconds 
#output
print(f"Average time for 1 mile = {o_min} min and {o_sec} sec.")


# what is your average speed in miles per hour
# define a function to calculate avg mile per hour
def avg_speed_mile_per_hour(mile, hour):
    miles_per_hour = mile / hour
    return miles_per_hour

avg_speed = round(avg_speed_mile_per_hour(km_to_mile(distance_km), sec_to_hour(min_and_sec_to_sec(g_min, g_sec))), 2) # Using multiple function in one function
print(f"Average speed per hour = {avg_speed} miles.")



