def sort_by_guide(arr, guide):
    empty_list = []

    for number in guide:
        if number != -1:
            empty_list.append(0)
        else:
            empty_list.append(-1)
    print(empty_list)

    for i, number in enumerate(guide):
        if number != -1:
            empty_list.insert(number-1, arr[i])
            del empty_list[number]
    print(empty_list)

    sorted_list = []
    for number in empty_list:
        if number > 0:
            sorted_list.append(number)
    print(sorted_list)

    for i, number in enumerate(guide):
        if number == -1:
            sorted_list.insert(i, arr[i])

    return sorted_list


# print(sort_by_guide([56, 78, 3, 45, 4, 66, 2, 2, 4], [3, 1, -1, -1, 2, -1, 4, -1, 5]))
print(sort_by_guide([70, 10, 15, 800, 400, 4, 225, 438, 509, 1000], [6, 1, 4, -1, -1, 2, -1, -1, 5, 3]))
