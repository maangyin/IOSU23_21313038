def parenthese(s) :
    cnt = 0
    for i in range(len(s)):
        if s[i] == '(' :
            cnt+=1
        else :
            cnt-=1
        if cnt < 0 :
            return False
    return cnt == 0

s = ""
s = input()
while(s != "") :
    print(parenthese(s))
    s = input()