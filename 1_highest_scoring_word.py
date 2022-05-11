import string


def high(x):
    letter_dict = dict(zip(string.ascii_lowercase, range(1, 27)))
    score = 0
    score_list = []

    words_list = x.split()

    for word in words_list:
        list_of_letters = list(word)
        for letter in list_of_letters:
            score += letter_dict[letter]
        score_list.append(score)
        score = 0

    max_value = max(score_list)
    index_of_max_value = score_list.index(max_value)

    return words_list[index_of_max_value]


print(high('aa bb def'))
