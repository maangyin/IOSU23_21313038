def sumFact(n) :
    res = 0
    prod = 1

    i = 1
    while(i <= n):
        prod = prod*i
        res += prod
        i += 1
    return res

s = input()
while(s != "") :
    print(sumFact(int(s)))
    s = input()