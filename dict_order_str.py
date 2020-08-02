def testBig(subs,k):
    permStr(subs,k)
    return words[0]

words = []
def permStr(subs,k):
    if(k>0):
        for i,ch in enumerate(subs):
            new_subs = subs[0:i] + subs[i+1:]
            #print(new_subs)
            permStr(new_subs,k-1)
    else:
        #print(subs)
        if (len(words) == 0):
            words.append(subs)
        else:
            temp = []
            temp.append(words[0])
            temp.append(subs)
            temp.sort()
            words[0] = temp[1]
            del temp

#x = 'zyxedcba'
x = 'rim'
z = testBig(x,2)
print("ip"+" "+x)
print('result')
print(z)
