x = input("Monthly Savings: ")
y = input("Annual Interest Rate: ")
q = input("Desired Years: ")
r = input("Reporting Breakdown (Months): ")

r = float(r)
q = 12 * (float(q))
p = 0
total_savings = 0
monthly_savings = float(x)
t_bill = 0
interest_rate_annual =( float(y)) / 100
interest_rate_monthly = interest_rate_annual / 12
monthly_interest = 0
hand_cash = 0

print("")
while p <= q:
    p = p + 1
    monthly_interest = round(t_bill * interest_rate_monthly)
    hand_cash = round(hand_cash + monthly_savings + monthly_interest)
    if hand_cash > 100000:
        t_bill = t_bill + 100000
        hand_cash = hand_cash - 100000
    total_savings = round(hand_cash + t_bill)
    if p % r == 0:
        print(f"After Month {p},")
        print("Monthly Interest:", monthly_interest)
        print("Hand Cash:", hand_cash)
        print("Total Investment:", t_bill)
        print("")

print("")
print("Program Finished, Thank You!")
print("")