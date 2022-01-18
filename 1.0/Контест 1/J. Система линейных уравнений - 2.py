a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
if a == b == c == d == e == f == 0:
    print(5)
elif a == b == c == d == 0:
    print(0)
elif c == d == f == 0 and a != 0 and b != 0:
    print(1, -a/b, e/b)
elif a == b == e == 0 and c != 0 and d != 0:
    print(1, -c/d, f/d)
elif c != 0 and d != 0 and a/c == b/d and a*f/c == e:
    print(1, -a/b, e/b)
elif a == c == 0:
    if b == 0:
        print(4, f/d)
    elif d == 0:
        print(4, e/b)
    elif e/b == f/d:
        print(4, e/b)
    else:
        print(0)
elif b == d == 0:
    if a == 0:
        print(3, f/c)
    elif c == 0:
        print(3, e/a)
    elif f/c == e/a:
        print(3, f/c)
    else:
        print(0)
else:
    det = a * d - b * c
    if det == 0:
        print(0)
    else:
        det_x = e * d - b * f
        det_y = a * f - e * c
        x = det_x / det
        y = det_y / det
        print(2, x, y)
