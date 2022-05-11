def sep_str(str_object):
    i = 0
    try:
        counter = len(max(str_object.split(), key=len))
    except ValueError:
        counter = 0
    lists = [[] for i in range(0, counter)]

    word_list = str_object.split()

    for list_element in lists:
        for idx, word in enumerate(word_list):
            try:
                list_element.append(word[i])
            except IndexError:
                list_element.append('')
        i += 1

    return lists


print(sep_str("The Mitochondria is the powerhouse of the cell"))
