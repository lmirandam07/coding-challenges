def reverseString(self, s):
    mid = len(s) // 2
    for i in range(mid):
        tmp = s[i]
        s[i] = s[-(i+1)]
        s[-(i+1)] = tmp

    print(s)
