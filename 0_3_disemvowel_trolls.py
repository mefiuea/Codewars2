def disemvowel(string_):
    vowels_list_lower = ['a', 'e', 'i', 'o', 'u']
    vowels_list_upper = ['A', 'E', 'I', 'O', 'U']
    char_list = list(string_)
    consonants_list = []
    for char in char_list:
        if char.islower() and char not in vowels_list_lower:
            consonants_list.append(char)
        elif char.isupper() and char not in vowels_list_upper:
            consonants_list.append(char)
        elif char not in vowels_list_lower and char not in vowels_list_upper:
            consonants_list.append(char)

    return ''.join(consonants_list)
