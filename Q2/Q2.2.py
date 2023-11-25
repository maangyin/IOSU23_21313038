def evaluate(s, n) :
    val = 0
    for p in range(len(s)):
        if s[len(s) - p - 1] == '1':
            val += (-2) ** p
    return abs(val - n)

def enbasemoinsdeux(n) :
    seeds = ["000000000000000000000000000000000000"]
    while True:
        # print(seeds)
        for i in range(len(seeds)) :
            for j in range(len(seeds[i])) :
                new = seeds[i][:j]
                if seeds[i][j] == '0' :
                    new += '1'
                else :
                    new += '0'
                new += seeds[i][j+1:]
                seeds.append(new)
        seeds = set(seeds)
        seeds = sorted(seeds, key = (lambda s : evaluate(s, n)))
        seeds = seeds[:40]
        if evaluate(seeds[0], n) == 0 :
            k = 0
            while (seeds[0][k] == '0') :
                k += 1
            if (len(seeds[0]) == k) :
                print('0')
            else :
                for k in range(k, len(seeds[0])):
                    print(seeds[0][k], end="")
                print()
            return

s = ""
s = input()
while(s != "") :
    enbasemoinsdeux(int(s))
    s = input()
        