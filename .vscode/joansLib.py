#this function returns P(n,n). 
# #x is either 1 (which returns the member of P(n,n) that begins with 1), 2 (which returns the member that begins with 0),
#or 0 (which returns a ist of both)(technically anything != 1 or 2 would work here but I like 0)
def rr(x, n):
    r = int(n)
    firstList = []
    secondList = []
    i = 0
    while i < r:
        if len(firstList) < r:
            firstList.append(1)
        if len(firstList) < r:
            firstList.append(0)
        i += 1
    i = 0
    while i < r:
        if len(secondList) < r:
            secondList.append(0)
        if len(secondList) < r:
            secondList.append(1)
        i += 1
    finalList = [firstList, secondList]
    if x == 1:
        return firstList
    if x == 2:
        return secondList
    else:
        return dupeElim(finalList)
    
#does what it says on the tin. takes in a list and eliminated the duplicates
def dupeElim(list):
    out = []
    i = 0 
    while i < len(list):
        if list[i] in out:
            i += 1
        else:
            out.append(list[i])
            i += 1
    return(out)
#takes a list in and returns a list of a the input list with num inserted at various indicies
def numInsert(list, num):
    out = []
    i = 0 
    while i <= len(list):
        out += [list.copy()]
        #print(out)
        #print(out[i])
        i += 1
    j = 0
    while j < len(out):
        out[j].insert(j,num)
        #print(out[j])
        #print(out)
        j+=1
    return(out)
#takes a list of lists and applies the numInsert function to them
def recNumIns(list, num):
    out = []
    i = 0
    for c in list:
        out += numInsert(list[i], num)
        i += 1
    return dupeElim(out)
#takes us from P(a, b) to P(a+1, b)
def rCBoth(list):
    out = []
    out += recNumIns(list, 0)
    out += recNumIns(list, 1)
    return dupeElim(out)
def Ngine(list):
    out = []
    out += recNumIns(list, 0)
    #print(out)
    out += recNumIns(list, 1)
    #print(out)
    out += recNumIns(list, "e")
    #print(out)
    return dupeElim(out)

def parent(r, maxE):
    R = rr(0, r)
    i = 0
    eList = R.copy()
    while i < maxE:
        eList = recNumIns(eList, "e")
        i += 1
    return(eList)

def charIndexer(pList, str):
    dexList = []
    d = -1
    for string in pList:
        k = 0
        #print(string)
        if k%2 == 0:
            dexList.append([])
            d += 1
        for memb in string:
            if memb == str:
                dexList[d].append(k)
            k += 1
    j = 0 
    out = []
    while j < len(pList):
        out.append([pList[j], dexList[j]])
        j += 1
    return out

def swapper(list, i, j):
    temp = list[i]
    list[i] = list[j]
    list[j] = temp
    return(list.copy())

def involDexer(listlist):
    if type(listlist[0]) != list or type(listlist[0]) != list:
        return("ERROR: Input is not list of lists")
    out = []
    i = 0
    temp = []
    while i < len(listlist[0]) - 1:
        temp = [swapper(listlist[0].copy(), i, i+1), listlist[1].copy()]
        temp[1].append(i)
        out += [temp]
        i += 1
    return(out)

def involRecur(listoflistlist):
    out = []
    for x in listoflistlist:
        out += involDexer(x)
    return(out)

def inverCounter(list):
    count = 0 
    for x in list:
        for y in list:
            if x > y and list.index(x) < list.index(y):
                count += 1
    return count

def inverFilter(listoflistlist, i):
    out = []
    for x in listoflistlist: 
        if inverCounter(x[0]) >= i:
            out += [x.copy()]
    return(out)

def aNgine(n):
    mxInver = 0
    i0 = 0
    w0 = [[],[]] #[[string],[involution hist]]
    while i0 <= n:
        w0[0].append(i0)
        mxInver += n - (i0)
        i0 += 1    
    i1 = 0 
    temp = involDexer(w0)
    out = []
    while i1 < mxInver:
        #print(temp.copy())
        out = temp.copy()
        temp = inverFilter(involRecur(temp), i1 + 1)
        i1 += 1
    return(out)

def minSubStr(n):
    out = []
    for x in aNgine(n):
        out += [x[1]]
    return(out)

#TODO write functions identity,

def rev(list):
    out = []
    for x in list:
        out.insert(0,x)
    return out

def swap0n(list):
        out = []
        n = -1 
        for x in list:
            if type(x) == int and x > n:
                n = x
        for x in list:
            if x == 0:
                out.append(n)
            elif x == n:
                out.append(0)
            else:
                out.append(x)
        return out

def listPair(list, listP):
    return [list, listP]

def maxEParent(list, maxE):
    out = list
    i = 0
    while i < maxE:
        out = recNumIns(out.copy(), 'e')
        i += 1
    return out

def proginy(list):
    out = []
    endex = []
    #all w/ 1st e replaced  up to nth e replaced
    i = 0
    maxN = -1
    for x in list:
        if x == 'e':
            endex.append(i)
        if type(x) == int and x > maxN:
            maxN = x
        i += 1
    for x in endex:
        temp = list.copy()
        temp.pop(x)
        print(temp)
        j = 0
        while j <= maxN:
           tmp = temp.copy()
           tmp.insert(x, j)
           out += [tmp]
           print(tmp)
           j += 1
        print()
    return out

def morphChunker(list):
    return [list, swap0n(list), rev(list), swap0n(rev(list))]

def childCheck(p1, p2):
    c1 = []
    