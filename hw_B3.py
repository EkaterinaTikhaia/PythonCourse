s = input ()
t = input ()
D = 0
for i in range(len(s)):
    if s[i]!=t[i]:
        D = D + 1
print (D)

