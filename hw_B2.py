s = input ()
sc = []
for i in s:
    if i=="A":
        sc.append("T")
    if i=="T":
        sc.append("A")
    if i=="C":
        sc.append("G")
    if i=="G":
        sc.append("C")
list.reverse(sc)
for elem in sc:
    print(elem, end='')
