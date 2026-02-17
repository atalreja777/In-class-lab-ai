
def bayesRule(aGivenC, bGivenC, aGivenNotC, bGivenNotC, c):
    num = aGivenC * bGivenC * c
    denom = num + aGivenNotC * bGivenNotC * (1 - c)
    return num / denom


def conIndependence(o1GivenG, g, o1GivenNotG, o2GivenG, o2GivenNotG):
    gGiveno1 = (o1GivenG * g) / ((g * o1GivenG) + ((1 - g) * o1GivenNotG))
    notGGiveno1 = (o1GivenNotG * (1 - g)) / ((g * o1GivenG) + ((1 - g) * o1GivenNotG))
    return o2GivenG * gGiveno1 + o2GivenNotG * notGGiveno1


def format(x, decimals=3):
    if decimals == 5:
        return "{:.5f}".format(x)
    if decimals == 4:
        return "{:.4f}".format(x)
    return "{:.3f}".format(x)


# testing*********************************************************************

# givens from user input (defaulted to quiz)
g = .9
notG = .1

o1GivenG = .5
o1GivenNotG = .05

o2GivenG = .75
o2GivenNotG = .25

print("\nBAYESIAN NETWORK PROBABILITY CALCULATOR \n")

print("   G   ")
print(" /   \\  ")
print("o1   o2 \n")

# user inputs (overwrites the values above)
g = float(input("P(g): "))
notG = 1 - g

o1GivenG = float(input("P(o1|g): "))
o1GivenNotG = float(input("P(o1|~g): "))

o2GivenG = float(input("P(o2|g): "))
o2GivenNotG = float(input("P(o2|~g): "))



# a) P(o2|g,~o1) = P(o2|g)
print("a) P(o2 | g, ~o1)")
print("Step 1: P(o2|g,~o1) = P(o2|g)")
print("Result: " + format(o2GivenG))
print("\n---\n")

# b) P(g|o1,o2)
num_b = o1GivenG * o2GivenG * g
den_b = o1GivenNotG * o2GivenNotG * (1 - g)
res_b = bayesRule(o1GivenG, o2GivenG, o1GivenNotG, o2GivenNotG, g)

print("b) P(g | o1, o2)")
print("Step 1: P'(g|o1,o2) = P(o1|g)P(o2|g)P(g) = (" + format(o1GivenG) + ")(" + format(o2GivenG) + ")(" + format(g) + ") = " + format(num_b, 4))
print("Step 2: P'(~g|o1,o2) = P(o1|~g)P(o2|~g)P(~g) = (" + format(o1GivenNotG) + ")(" + format(o2GivenNotG) + ")(" + format(1 - g) + ") = " + format(den_b, 5))
print("Step 3: P(g|o1,o2) = " + format(num_b, 4) + " / (" + format(num_b, 4) + " + " + format(den_b, 5) + ") = " + format(res_b))
print("Result: " + format(res_b))
print("\n---\n")

# c) P(g|~o1,o2)
num_c = (1 - o1GivenG) * o2GivenG * g
den_c = (1 - o1GivenNotG) * o2GivenNotG * (1 - g)
res_c = bayesRule(1 - o1GivenG, o2GivenG, 1 - o1GivenNotG, o2GivenNotG, g)

print("c) P(g | ~o1, o2)")
print("Step 1: P'(g|~o1,o2) = P(~o1|g)P(o2|g)P(g) = (" + format(1 - o1GivenG) + ")(" + format(o2GivenG) + ")(" + format(g) + ") = " + format(num_c, 4))
print("Step 2: P'(~g|~o1,o2) = P(~o1|~g)P(o2|~g)P(~g) = (" + format(1 - o1GivenNotG) + ")(" + format(o2GivenNotG) + ")(" + format(1 - g) + ") = " + format(den_c, 4))
print("Step 3: P(g|~o1,o2) = " + format(num_c, 4) + " / (" + format(num_c, 4) + " + " + format(den_c, 4) + ") = " + format(res_c))
print("Result: " + format(res_c))
print("\n---\n")

# d) P(g|~o1,~o2)
num_d = (1 - o1GivenG) * (1 - o2GivenG) * g
den_d = (1 - o1GivenNotG) * (1 - o2GivenNotG) * (1 - g)
res_d = bayesRule(1 - o1GivenG, 1 - o2GivenG, 1 - o1GivenNotG, 1 - o2GivenNotG, g)

print("d) P(g | ~o1, ~o2)")
print("Step 1: P'(g|~o1,~o2) = P(~o1|g)P(~o2|g)P(g) = (" + format(1 - o1GivenG) + ")(" + format(1 - o2GivenG) + ")(" + format(g) + ") = " + format(num_d, 4))
print("Step 2: P'(~g|~o1,~o2) = P(~o1|~g)P(~o2|~g)P(~g) = (" + format(1 - o1GivenNotG) + ")(" + format(1 - o2GivenNotG) + ")(" + format(1 - g) + ") = " + format(den_d, 5))
print("Step 3: P(g|~o1,~o2) = " + format(num_d, 4) + " / (" + format(num_d, 4) + " + " + format(den_d, 5) + ") = " + format(res_d))
print("Result: " + format(res_d))
print("\n---\n")

# e) P(o2|o1)
p_o1 = (g * o1GivenG) + ((1 - g) * o1GivenNotG)
gGiveno1 = (o1GivenG * g) / p_o1
notGGiveno1 = (o1GivenNotG * (1 - g)) / p_o1
res_e = conIndependence(o1GivenG, g, o1GivenNotG, o2GivenG, o2GivenNotG)

print("e) P(o2 | o1)")
print("Step 1: P(o1) = P(g)P(o1|g) + P(~g)P(o1|~g) = (" + format(g) + ")(" + format(o1GivenG) + ") + (" + format(1 - g) + ")(" + format(o1GivenNotG) + ") = " + format(p_o1, 3))
print("Step 2: P(g|o1) = P(o1|g)P(g)/P(o1) = (" + format(o1GivenG) + ")(" + format(g) + ")/" + format(p_o1, 3) + " = " + format(gGiveno1, 3) +
      " ,  P(~g|o1) = (" + format(o1GivenNotG) + ")(" + format(1 - g) + ")/" + format(p_o1, 3) + " = " + format(notGGiveno1, 4))
print("Step 3: P(o2|o1) = P(o2|g)P(g|o1) + P(o2|~g)P(~g|o1) = (" + format(o2GivenG) + ")(" + format(gGiveno1, 3) + ") + (" + format(o2GivenNotG) + ")(" + format(notGGiveno1, 4) + ") = " + format(res_e, 3))
print("Result: " + format(res_e))
print()

