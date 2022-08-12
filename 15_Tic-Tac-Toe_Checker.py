def is_solved(board):
    sum_row_list = []
    sum_column_list = []
    win_status = -1
    zero_flag = False
    c = 0
    for row in board:
        for element in row:
            sum_row_list.append(element)
        if sum(sum_row_list) == 6 and 0 not in sum_row_list:
            return 2
        elif sum(sum_row_list) == 3 and 0 not in sum_row_list:
            return 1
        else:
            if 0 in sum_row_list:
                zero_flag = True  # not finished yet
            else:
                win_status = 0  # draw
        sum_row_list = []

    while c < len(board[0]):
        for row in board:
            sum_column_list.append(row[c])
        if sum(sum_column_list) == 6 and 0 not in sum_column_list:
            return 2
        elif sum(sum_column_list) == 3 and 0 not in sum_column_list:
            return 1
        else:
            if 0 in sum_column_list:
                zero_flag = True  # not finished yet
            else:
                win_status = 0  # draw
        c += 1
        sum_column_list = []



    if zero_flag:
        return -1
    else:
        return win_status


board = [[2, 0, 2],
         [2, 1, 1],
         [1, 2, 1]]

print(is_solved(board))
