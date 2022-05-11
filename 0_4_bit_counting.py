def count_bits(n):
    return sum([int(number) for number in list(f'{n:b}')])
