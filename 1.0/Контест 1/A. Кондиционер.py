t_room, t_cond = map(int, input().split())
op_mode = input()
if op_mode == 'freeze':
    if t_room < t_cond:
        print(t_room)
    else:
        print(t_cond)
elif op_mode == 'heat':
    if t_room < t_cond:
        print(t_cond)
    else:
        print(t_room)
elif op_mode == 'auto':
    print(t_cond)
elif op_mode == 'fan':
    print(t_room)
