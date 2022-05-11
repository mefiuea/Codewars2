def find_children(dancing_brigade):
    upper_list = []
    lower_list = []
    temp_list = []
    string = ''

    letters_list = list(dancing_brigade)
    for letter in letters_list:
        if letter.isupper():
            upper_list.append(letter)
        else:
            lower_list.append(letter)

    upper_list.sort()
    lower_list.sort()

    print(upper_list)
    print(lower_list)

    for up_letter in upper_list:
        string += up_letter
        for low_letter in lower_list:
            if up_letter.lower() == low_letter:
                temp_list.append(low_letter)
        string += ''.join(temp_list)
        temp_list = []

    return string


print(find_children("CbcBcbaA"))
