A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
if D > E:
    D, E = E, D
if A > B:
    A, B = B, A
if B > C:
    B, C = C, B
if A > B:
    A, B = B, A
if A <= D and B <= E:
    print('YES')
else:
    print('NO')
