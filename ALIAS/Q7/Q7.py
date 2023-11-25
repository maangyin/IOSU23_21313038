def aux(l, n, res, acc):
    if (l == []):
        if(acc == n):
            return res
    else :
        r = aux(l[1:], n, res + '+', acc + l[0])
        if r != None :
            return r
        r = aux(l[1:], n, res + '-', acc - l[0])
        if r != None :
            return r
        r = aux(l[1:], n, res + '*', acc * l[0])
        if r != None :
            return r
    return None

def arithmetique(l, n) :
    return aux(l[1 :], n, '', l[0])

print(arithmetique([618,76,665,691,61,6,525,75,420,332,210,355,90], 2036333247891300))