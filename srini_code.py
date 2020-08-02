def getMinIns(first,second):
    ind = 0
    ins = 0
    l = len(first)
    s = len(second)
    for item in second:
        if (item in first[ind:]):
            ind = first.index(item)+1
            l -= 1
            if (ind == s):
                ins += l
                break
        else:
            ins += 1
            l-=1
    return ins

def getMinInsMod(first,second):
    ind = 0
    ins = 0
    l = len(first)
    s = len(second)
    for item in second:
        if (item in first[ind:]):
            ind = first.index(item)+1
            l -= 1
            if (ind == s):
                ins += l
                break
        else:
            if (ind>0):
                ins+=l
                break
            else:
                ins += 1
                l-=1
    return ins

def testcase1():
    lim = 10000000
    x = [i for i in range(0,lim)]
    y = [i for i in range(lim+1,lim+300)] 
    z = getMinIns(x,y)
    print(z)
def testcase2():
    x = [4,5,1,7,8]
    y = [4,8,7,9,5,1]
    z = getMinIns(x,y)
    print(z)

#testcase1()
testcase2()
