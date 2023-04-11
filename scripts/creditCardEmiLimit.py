
def purchase_limit(rLimit, iRate):
    purchase_amount = 0
    pur_limit = 0
    while pur_limit < rLimit:
        purchase_amount = purchase_amount + 1
        pur_limit = purchase_amount * (1 + iRate)
    return(purchase_amount)

remaining_limit = float(input("Enter your credit card remaining balance: "))
interest_rate = (float(input("Enter interest rate: "))) / 100

x = purchase_limit(remaining_limit, interest_rate)
print(f'you can purchase up to {x} taka.')