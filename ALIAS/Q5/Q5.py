def parenthesage(s):
    if (len(s) % 2 == 1):
        return -1

    cpt = 0
    res = 0
    for e in s :
        if (e == '('):
            cpt+=1
        if (e == ')'):
            cpt+= -1
            if(cpt < 0):
                cpt += 2
                res += 1
    if(cpt > 0) :
        res += cpt // 2
    return res

s = ""
s = input()
while(s != "") :
    print(parenthesage(s))
    s = input()