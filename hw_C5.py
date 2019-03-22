n = input ()
k = input ()
Fnewb = []
Fmat = []
for i in range(int(n)):
	if i == 0 or i == 1:
		Fmat.append(1)
		Fnewb.append(0)
	else:
		Fnewb.insert(i, Fmat[int(i)-1]*int(k))
		Fmat.insert(i, Fmat[int(i-1)]+Fnewb[int(i-1)])
print(Fnewb[int(n)-1] + Fmat[int(n)-1])
