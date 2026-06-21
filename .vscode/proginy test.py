import joansLib as j

out = []

#detect highest member == k
#swap e's w/ 0 to k

aList = [1,0,2,'e',1,0,2]
i = -1
count = 0

for x in aList:
    if x == 'e':
        count += 1
    else:
        if x > i:
            i = x



print(i)
print("count")
print(count)
