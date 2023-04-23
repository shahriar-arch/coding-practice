# We need to import sys  to stope the code in the middle if the inputs are not right 
import sys

# write a function that will check if you are prepare for rain or not.
def prepared_for_rain(have_umbrella, rain_level, have_hood, is_workday):
    output = (
        have_umbrella
        or ((rain_level < 5 and have_hood)
            or (not (rain_level > 0 and is_workday)))
    )
    return output


# take the input from the user
umbrella_status = (input("Have umbrella?(Ture or False): "))
hood_status = (input("Have hood? (True or False) :"))
workday_status = (input("Is it workday? (True or False): "))
rain_status = int(input("Give the forcasted rain level (0 to 10): "))

# convert the True or False values to bollean
# write a function to convert the string True or False to bool True or False
def get_bool(input):
    output = None 
    """A function that takes input string True or False and returns bool True or False"""
    if input == "True":
        output = True
    elif input == "False":
        output = False
    # if the input value is not true or false the function will return None
    return output 

# convert the input values to bools 
umbrella_status = get_bool(umbrella_status)
hood_status = get_bool(hood_status)
workday_status = get_bool(workday_status)

# we have to check if any of the value have none value 
# to check we have to compare the variable with a none variable 
# creating a none variable 
x = None 

# now check the type of variables

if type(x) == type(umbrella_status):
    sys.exit("Invalid Input")
if type(x) == type(hood_status):
    sys.exit("Invalid Input")
if type(x) == type(workday_status):
    sys.exit("Invalid Input") 


# if everyting alright, run the given values in the function
rain_preparation = prepared_for_rain(umbrella_status, rain_status, hood_status, workday_status)

# Display the result
if rain_preparation:
    print("You are ready for rain.")
else:
    if rain_status < 5:
        print("You are not ready for rain, get yourself a hood.")
    else:
        print("You are not ready for rain, get an umbrella.")
