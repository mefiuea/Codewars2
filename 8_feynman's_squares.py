from datetime import datetime


def count_squares(n):
    start_time = datetime.now()
    total = 0
    i = 0
    for _ in range(n):
        total += pow(n - i, 2)
        i += 1
    end_time = datetime.now()
    print((end_time - start_time))

    return total


def count_squares_2(n):
    start_time = datetime.now()
    res = (n * (n + 1) * ((2 * n) + 1)) // 6
    end_time = datetime.now()
    print((end_time - start_time))

    return int(res)


# print(count_squares(5))
print('count_squares', count_squares(10000000))
print('count_squares_2', count_squares_2(10000000))
