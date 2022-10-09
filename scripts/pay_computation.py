
def computepay(hours, rate):
    if hours <= 40:
        pay = round(hours * rate)
        print(f"Pay: {pay}")

    elif hours > 40:
        overtime = hours - 40
        overtime_rate = rate * 1.5
        general_pay = (hours - overtime) * rate
        overtime_pay = overtime * overtime_rate
        pay = general_pay + overtime_pay
        print(f"Pay: {pay}")


hours = input("Enter Hours: ")
rate = input("Enter Rate: ")

try:
    hours = float(hours)
    rate = float(rate)
    computepay(hours, rate)
except:
    print("Error, please enter numeric input!")
