
def computegrade (score):
    if score >= 0.0 and score <= 1.0:
        if score >= 0.9:
            print("Grade: A")
        elif score >= 0.8:
            print("Grade: B")
        elif score >= 0.7:
            print("Grade: C")
        elif score >= 0.6:
            print("Grade: D")
        elif score <0.6:
            print("Grade: F")
    else:
        print("Give a valid score between 0.0 to 1.0")

s = input("Enter score: ")

try:
    s = float(s)
    computegrade (s)

except:
    print("Give a numeric score between 0.0 to 1.0")
