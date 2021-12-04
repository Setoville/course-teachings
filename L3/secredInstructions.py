user_input = input()
# "57234"
while user_input != '99999':
    direction_total = int(user_input[0]) + int(user_input[1])
    if direction_total % 2 == 0:
        direction = 'right'
    # technically incomplete. we're missing a case here.
    else:
        direction = 'left'
    steps = int(user_input[2:5])  # 234
    print(direction, steps)
    user_input = int(input())
