import quantumrandom
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
Cardinality = 4
Cardinality_Subset = 2
universe = []
sample = []
dice = 0
element = 0
# New Universe.
for i in range(1,Cardinality+1):
    universe.append(i)

for i in range(1,Cardinality_Subset + 1):
    print("Universum:")
    print(universe)
    Cardinality = len(universe)
    print("Card of Universum = ", Cardinality)
    dice = round(quantumrandom.randint(1, Cardinality))
    print("====|||| Dice = ", dice)
    element = universe[dice - 1]
    sample.append(element)
    print("Element selected {", element, "}")
    del universe[dice - 1]
    print("Universe after {", element, "} selected.")
    print(universe)

sample.sort()
print("Sample:")
print(sample)