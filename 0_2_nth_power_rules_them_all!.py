def modified_sum(a, n):
    return sum([number**n for number in a]) - sum([number for number in a])
