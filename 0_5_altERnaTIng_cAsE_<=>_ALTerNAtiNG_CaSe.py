def to_alternating_case(string):
    char_list = list(string)
    new_char_list = []
    for char in char_list:
        if char.islower() and not char.isnumeric():
            new_char_list.append(char.upper())
        elif char.isupper() and not char.isnumeric():
            new_char_list.append(char.lower())
        else:
            new_char_list.append(char)

    return ''.join(new_char_list)
