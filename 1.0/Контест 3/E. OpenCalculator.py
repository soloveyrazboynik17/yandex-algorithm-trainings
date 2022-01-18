buttons = set(map(int, input().split()))
for char in input():
    digit = int(char)
    if digit not in buttons:
        buttons.add(digit)
print(len(buttons)-3)
