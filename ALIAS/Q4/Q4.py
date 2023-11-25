def fraction(k):
    # res = []
    # for x in range(1, 10**5):
    #     if (x != k and (k*x)%(x - k) == 0 and (k*x)//(x - k) >= 0) :
    #         y= (k*x)//(x - k)
    #         if(x >= y) :
    #             res.append("1/" + str(k) + " = 1/" + str(x) + " + 1/" + str(y))
    # for i in range(len(res) - 1, -1, -1) :
    #     print(res[i])

    for y in range(k+1, 2*k + 1):
        if (k*y) % (y-k) == 0 :
            print("1/" + str(k) + " = 1/" + str((k*y) // (y-k)) + " + 1/" + str(y))
    print()



s = input()
while(s != "") :
    fraction(int(s))
    s = input()