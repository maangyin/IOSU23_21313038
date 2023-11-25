def dfs(digit, sum, dic, s) :
    if digit == -1 :
        dic[sum] = s
    else :
        dfs(digit - 1, sum + (-2) ** digit, dic, s+"1")
        dfs(digit - 1, sum, dic, s+"0")

dic = dict()
dfs(10, 0, dic, "")
for i in range(1000):
    print('{:-3}'.format(i), dic[i])