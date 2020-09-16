import quantumrandom
# Monkey patching! Redifining create context as unverified one!!!!
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
# Monkye patching!  End of hack.


# Combinatorics background.
# Combination C(n,k)- the order of selection does not matter
# Permutaion P(n,k) -  k-permutations of n are the different ordered arrangements of a k-element subset of an n-set

# Cardinality of set A notation - |A|.
Cardinality = 20
Cardinality_Subset = 4
universe = []
sample = []
dice = 0
element = 0
# New Universe.
for i in range(1,Cardinality+1):
    universe.append(i)


for i in range(1,Cardinality_Subset + 1):
    Cardinality = len(universe)
    print("Universum (Cardinality = ", Cardinality, "):")
    print(universe)
    #print("Card of Universum = ", Cardinality)
    dice = round(quantumrandom.randint(1, Cardinality))
    element = universe[dice - 1]
    sample.append(element)
    print("====|||| Dice = ", dice, " ||||   Element selected {", element, "}")
    #print("Element selected {", element, "}")
    del universe[dice - 1]
    print("Universe after {", element, "} selected:")
    print(universe)

sample.sort()
print("Sample:")
print(sample)