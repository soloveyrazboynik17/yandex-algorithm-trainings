numbers_list = list(map(int, input().split()))
numbers_set = set()
for number in numbers_list:
    if number not in numbers_set:
        print('NO')
        numbers_set.add(number)
    else:
        print('YES')
