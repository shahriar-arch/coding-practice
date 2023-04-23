def cost_of_project(engraving, solid_gold):
    if solid_gold:
        cost = 100 + (len(engraving) * 10)
    else:
        cost = 50 + (len(engraving) * 7)
    return cost

ring_princ = cost_of_project("Charlie+Denver", True)
print(ring_princ)

