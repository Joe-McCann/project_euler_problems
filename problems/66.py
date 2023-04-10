import math
import importantFunctions as impf

squares = set([x**2 for x in range(1, 40)])
D_lim = 1001
maxx = 0
maxD = 0
maxy = 0
for D in range(2, D_lim):
    if D in squares:
        continue
    cf = impf.generateSqrtContFraction(D)
    cycle = cf[1]
    if len(cycle) % 2 == 1:
        cycle += cycle
    cycle.pop()
    frac = [1, cycle[~0]]
    for i in range(1, len(cycle)):
        frac = impf.addFractions([cycle[~i], 1], frac)
        frac = frac[::-1]
    frac = impf.addFractions([cf[0], 1], frac)
    print(f"{frac[0]}^2-{D}*{frac[1]}^2=1")
    if frac[0] > maxx:
        maxx = frac[0]
        maxD = D
        maxy = frac[1]

print("\nMaximum Equation")
print(f"{maxx}^2-{maxD}*{maxy}^2=1")

