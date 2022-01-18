a = int(input())
b = int(input())
c = int(input())
if c < 0:
    print('NO SOLUTION')
elif a == 0:
    if b == c**2:
        print('MANY SOLUTIONS')
    else:
        print('NO SOLUTION')
else:
    x = (c**2 - b) / a
    if x - int(x) == 0.0:
        print(int(x))
    else:
        print('NO SOLUTION')
