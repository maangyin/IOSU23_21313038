def sol(niv, rest):
    if niv < 0 :
        return []
    if niv > rest :
        return []
    if rest == 0:
        return [""]
    else :
        return ["("+r for r in sol(niv + 1, rest - 1)] + [")" + r for r in sol(niv - 1, rest - 1)]

for n in [3, 9, 11, 8, 2] :
    print(sorted(sol(0,2 * n)))
