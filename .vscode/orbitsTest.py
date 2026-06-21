import joansLib as c
import numpy as np
n = 3 #int(input("n?"))
e = 1 #int(input("num e?"))
aList = c.minSubStr(n)

checkList = []
out = []

for a in aList:
    if a and c.rev(a) and c.swap0n(a) and c.rev(c.swap0n(a)) not in checkList:
        checkList += [a]
        checkList += [c.swap0n(a)]
        checkList += [c.rev(a)]
        checkList +=[c.rev(c.swap0n(a))]
        out += [c.morphChunker(a)]

 
for o in out:
    for x in c.maxEParent(o, e):
        print(x)
    print()