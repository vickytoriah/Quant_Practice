
def solution(E, L):
    # Implement your solution here
    if E == L:
        start = 0
    else:
        start = 5

    entry_hr = int(E[:2])
    entry_min = int(E[-2:])

    leave_hr = int(L[:2])
    leave_min = int(L[-2:])
    # min_diff = abs(leave_min - entry_min)

    if entry_min > leave_min:
        min_to_next_hr = 60 - entry_min + leave_min
    # elif entry_min == 0:
    #     min_to_next_hr = leave_min
    else:
        min_to_next_hr = leave_min - entry_min
    hrs_ = leave_hr - entry_hr - 1
    add_min = min_to_next_hr % 60
    add_hr = (min_to_next_hr // 60)
    # print(add_hr, add_min)
    # and min_to_next_hr >= 60
    if add_min != 0 and add_hr > 0:
        add_hr = add_hr + 1
    elif add_min != 0 and add_hr == 0:
        add_hr = 1
    elif add_min == 0 and add_hr != 0:
        add_hr = add_hr - 1
    # if min_diff >= 60:
    #     extra_hrs = hrs_ + add_hr
    # else:
    #     extra_hrs = 0
    # print(hrs_, add_hr)
    total_cost = start + 4 * (hrs_ + add_hr)

    return total_cost
    # Implement your solution here
    # if E == L:
    #     start = 0
    # else:
    #     start = 5
    #
    # # extra_hrs = 0
    #
    # entry_hr = int(E[:2])
    # entry_min = int(E[-2:])
    #
    # leave_hr = int(L[:2])
    # leave_min = int(L[-2:])
    #
    # if entry_min > 0:
    #     min_to_next_hr = 60 - entry_min + leave_min
    # else:
    #     min_to_next_hr = leave_min
    # hrs_ = leave_hr - entry_hr - 1
    #
    # add_min = min_to_next_hr % 60
    # if add_min > 0:
    #
    #     add_hr = (min_to_next_hr // 60) + 1
    #     # add_hr = min_to_next_hr // 60
    # else:
    #     # add_hr = (min_to_next_hr // 60) -1
    #     add_hr = 0
    # # add_min = mins % 60
    #
    #
    # # stay_sec = datetime.timedelta(
    # #     hours=int(leave_hr - entry_hr),
    # #     minutes=int(60 - entry_min + leave_min),
    # # ).__str__()
    # total_cost = start + 4 * (hrs_ + add_hr)
    #
    # # total_cost = 2 + one_hr * 3 + extra_hrs * 4
    # # print(total_cost)
    #
    # return total_cost
