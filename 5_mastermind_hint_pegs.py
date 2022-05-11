def get_hints(answer, guess):
    result = {
        'black': 0,
        'white': 0,
    }
    answer_copy = []
    guess_copy = []
    for number in answer:
        answer_copy.append(number)
    for number in guess:
        guess_copy.append(number)

    for idx, number in enumerate(answer):
        if answer[idx] == guess[idx]:
            result['black'] += 1
            answer_copy[idx] = -1
            guess_copy[idx] = -1

    for number in answer_copy:
        if number > -1 and number in guess_copy:
            result['white'] += 1
            i = guess_copy.index(number)
            guess_copy[i] = -1

    return result


# print(get_hints([1, 2, 3, 4], [1, 2, 4, 3]))
print(get_hints([0, 0, 1, 1, 2, 3], [0, 0, 0, 1, 3, 2]))

# [0, 0, 1, 1, 2, 3]
# [0, 0, 0, 1, 3, 2]

# [-1, -1, 1, -1, 2, 3]
# [-1, -1, 0, -1, 3, 2]

# code = [1, 2, 3]
# guess = [2, 1, 3]
# result = {black: 1, white: 2}

# ta sama pozycja czarne
# różne pozycje, ale trafione białe
