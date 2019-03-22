a = input()
a = list(a.split())
for i in range(len(a)):
    k = [len(a[i]) for i in range(len(a))]
k.sort()
print(k[0])
