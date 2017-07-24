position_x = 1
position_y = 2

y = 2 * position_x + 1

position_str = "(" + str(position_x) + ", " + str(position_y) + ")"

if position_y > y:
    print(position_str + "은 직선의 위쪽에 있습니다.")
elif position_y == y:
    print(position_str + "은 직선 위의 점입니다.")
else:
    print(position_str + "은 직선의 아래쪽에 있습니다.")
