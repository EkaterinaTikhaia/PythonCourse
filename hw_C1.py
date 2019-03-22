a = input()
a = list(a.split())
for i in range(len(a)):
    if i == len(a)-1:
        break
    if int(a[i]) < int(a[i+1]):
        print(a[i+1], end = (' '))
