a = input()
S = 0
P = 1
for i in range(len(a)):
    S += int(a[i])
    P *= int(a[i])
print('сумма цифр в числе =', S, 'произведение цифр в числе =', P)
    
