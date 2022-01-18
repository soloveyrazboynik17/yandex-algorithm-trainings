phone_to_add = None
for i in range(4):
    phone = ''
    for char in input():
        if char.isdigit():
            phone += char
    if len(phone) == 7:
        phone = '495' + phone
    else:
        phone = phone[1:]
    if phone_to_add is None:
        phone_to_add = phone
    else:
        if phone_to_add == phone:
            print('YES')
        else:
            print('NO')
