import sys

accounts = {}


def deposit_or_withdraw(name, sum):
    if name not in accounts:
        accounts[name] = 0
    accounts[name] += sum


def balance(name):
    if name not in accounts:
        print('ERROR')
    else:
        print(accounts[name])


def transfer(name1, name2, sum):
    if name1 not in accounts:
        accounts[name1] = 0
    if name2 not in accounts:
        accounts[name2] = 0
    deposit_or_withdraw(name1, -sum)
    deposit_or_withdraw(name2, sum)


def income(p):
    for name in accounts:
        if accounts[name] > 0:
            accounts[name] = int(accounts[name] * (1+p/100))


for line in sys.stdin:
    info = line.split()
    operation = info[0]
    if operation == 'DEPOSIT':
        name, sum = info[1], int(info[2])
        deposit_or_withdraw(name, sum)
    elif operation == 'WITHDRAW':
        name, sum = info[1], int(info[2])
        deposit_or_withdraw(name, -sum)
    elif operation == 'BALANCE':
        name = info[1]
        balance(name)
    elif operation == 'TRANSFER':
        name1, name2, sum = info[1], info[2], int(info[3])
        transfer(name1, name2, sum)
    elif operation == 'INCOME':
        p = int(info[1])
        income(p)
