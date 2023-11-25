def sum(n) :
    res = 0
    while(n >= 0):
        res += n
        n -= 1
    return res

def pizza(n) :
    return 1 + sum(n)

n = input()
while(n != "") :
    # print(pizza(int(n)))
    nn = int(n)
    print((nn*nn+nn+2)//2)
    n = input()