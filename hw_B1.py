s = input ()
u = []
for i in s:
    if i=="A": u.append(i)
    if i=="C": u.append(i)
    if i=="G": u.append(i)
    if i=="T": u.append("U")
for elem in u:
    print(elem, end = '')

