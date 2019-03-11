import random
A = random.uniform (1, 100)
N = input("Я загадал число. Попробуй отгадать с десяти попыток! Твой вариант? ", )
for i in range(10):
    if i == 9 and int(A)!= int(N):
        print ("Больше не осталось попыток. Загаданное число = ", int(A))
        break
    if int(N) > int(A):
        print ("Меньше. Осталось попыток: ", 9-i)
    if int(N) < int(A):
        print ("Больше. Осталось попыток: ", 9-i)
    if int(N) == int(A):
        print("Правильно! Загаданное число = ", int(A))
        break
    N = input ()
    i += 1
            
