import math
from decimal import Decimal, getcontext
import gmpy2
from gmpy2 import mpfr
from mpmath import *


# TODO nie działa dla dużych liczb - trzeba poprawić
def cycle(n):
    getcontext().prec = 150
    check_str = ''
    i = 4
    print(getcontext())
    res = Decimal(1 / n)
    print(res)

    res_str = str(res)
    print(res_str)
    rest = math.modf(res)[0]
    print('REST:', rest)

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
print(cycle(197))
print('------------------')


def cycle_1(n):
    i = 4
    mp.dps = 200
    result = mpf(1) / mpf(n)
    result_str = str(result)

    while i < len(result_str):
        check_str = result_str[2:i]
        check_str_len = len(check_str)
        if check_str == result_str[i:i + check_str_len]:
            return check_str_len
        i += 1
    return -1


print(cycle_1(197))
print('-------------------')


def cycle_2(n):
    i = 4
    gmpy2.get_context().precision = 1024
    result = (mpfr(1) / mpfr(n))
    result_str = str(result)

    while i < len(result_str):
        check_str = result_str[2:i]
        check_str_len = len(check_str)
        if check_str == result_str[i:i + check_str_len]:
            return check_str_len
        i += 1
    return -1


print(cycle_2(197))
print('--------------')


def cycle_3(n):
    check_str = ''
    store_dictionary = {}
    result = 1 % n

    while ((result != 0) and (result not in store_dictionary)):
        store_dictionary[result] = len(check_str)
        result = result * 10

        check_str_part = result // n
        check_str += str(check_str_part)
        result = result % n

    if result == 0:
        return -1
    else:
        return len(check_str[store_dictionary[result]:])


print(cycle_3(197))
print('--------------')
