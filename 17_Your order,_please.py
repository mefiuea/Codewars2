def order(sentence):
    my_list = [0 for s in sentence.split()]

    for s in sentence.split():
        for char in s:
            if char.isdigit():
                my_list[int(char) - 1] = s

    return ' '.join(my_list)


print(order("is2 Thi1s T4est 3a"))
print(order("4of Fo1r pe6ople g3ood th5e the2"))
