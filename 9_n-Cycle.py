import math


# TODO nie działa dla dużych liczb - trzeba poprawić
def cycle(n):
    check_str = ''
    i = 4
    res = 1 / n
    print(res)

    res_str = str(res)
    print(res_str)
    rest = math.modf(res)[0]
    print(rest)

    while i < len(res_str):
        check_str = res_str[2:i]
        check_str_len = len(check_str)
        print('check_str = ', check_str)
        print('check_str_len = ', check_str_len)
        print('res_str[i:i+2]', res_str[i:i + check_str_len])
        if check_str == res_str[i:i + check_str_len]:
            return check_str_len
        i += 1
    return -1


# print(cycle(33))
# print(cycle(7))
# print(cycle(18118))
# print(cycle(37))
# print(cycle(197))

def cycle_2(n):
    check_str = ''
    i = 4
    result = 1 / n
    print(result)

    print(result * 10, ' ', int(result * 10))
    print(result * 100, ' ', int(result * 100))
    print(result * 1000, ' ', int(result * 1000))
    print(result * 10000, ' ', int(result * 10000))
    print(result * 100000, ' ', int(result * 100000))


print(cycle_2(33))
