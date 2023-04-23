def get_expected_cost (beds, baths, has_basement):
    value = 80000 + (30000 * beds) + (10000 * baths) + (40000 * has_basement)
    return(value)

house_price = get_expected_cost(1, 1, False)
print(house_price)

house_price2 = get_expected_cost(2, 1, True)
print(house_price2)

