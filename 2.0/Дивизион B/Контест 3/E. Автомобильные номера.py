M = int(input())
statements = []
for _ in range(M):
    statements.append(set(input()))
N = int(input())
car_numbers = []
for _ in range(N):
    car_number = input()
    car_numbers.append([car_number, set(car_number)])
max_statements = 0
for i in range(len(car_numbers)):
    count_statemets = 0
    for statement in statements:
        if statement.issubset(car_numbers[i][1]):
            count_statemets += 1
    car_numbers[i].append(count_statemets)
    if count_statemets > max_statements:
        max_statements = count_statemets
for i in range(len(car_numbers)):
    if car_numbers[i][2] == max_statements:
        print(car_numbers[i][0])
