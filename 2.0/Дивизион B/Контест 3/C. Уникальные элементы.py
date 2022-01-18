numbers_list = list(map(int, input().split()))
numbers_dict = {}
for number in numbers_list:
    if number not in numbers_dict:
        numbers_dict[number] = 0
    numbers_dict[number] += 1
unique = []
for number in numbers_list:
    if numbers_dict[number] == 1:
        unique.append(number)
print(*unique)
