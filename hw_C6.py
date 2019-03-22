a, t = input(), input()
s = []
for i in range(len(a) - len(t) + 1):
	s.append(a[i:i+len(t)])
K = 0
for i in range(len(s)):
	if s[i] == t:
		K = i+1
		print(K, end = " ")
