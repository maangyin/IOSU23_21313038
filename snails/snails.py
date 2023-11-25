import sys

def snail(inp):
    # print(len(inp), len(inp[0]))
    outp = []
    l = len(inp)
    # print(l)
    for p in range(l // 2):
        for i in range(l - p - 1, p, -1) :
            outp.append(inp[i][p])
        # outp.append(-1)
        for i in range(p, l - p - 1) :
            outp.append(inp[p][i])
        # outp.append(-1)
        for i in range(p, l - p - 1) :
            outp.append(inp[i][l - p - 1])
        # outp.append(-1)
        for i in range(l - p - 1, p, -1):
            outp.append(inp[l - p - 1][i])
        # outp.append(-1)
        # print("p=",p,outp)
    if (l % 2 == 1):
        outp.append(inp[l // 2][l // 2])
    print(' '.join(str(x) for x in outp))


inp = []
for line in sys.stdin:
    if line == "\n" :
        snail(inp)
        inp = []
    else :
        inp.append(line.split())
# snail(inp)