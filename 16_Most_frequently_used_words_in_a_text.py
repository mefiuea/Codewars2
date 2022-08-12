import collections
import re

characters_to_replace = r"#\/.,_;?!-:"
white_space = ["'", "'''"]


def top_3_words(text):
    new_text = ''
    word_dictionary = {}
    for word in text.split():
        for character in characters_to_replace:
            word = word.lower().replace(character, ' ')
        new_text += word + " "

    print(new_text)

    for word in new_text.split():
        if word not in word_dictionary.keys():
            word_dictionary[word] = 1
        else:
            word_dictionary[word] += 1

    # print('Oryginalny słownik: ', word_dictionary)
    # print('*' * 30)
    # print('Zmieniony słownik: ', dict(sorted(word_dictionary.items(), key=lambda item: item[1])))
    sorted_list = sorted(word_dictionary, key=word_dictionary.get, reverse=True)[:3]
    # sl = [word for word in sorted_list if word not in white_space]

    return sorted_list


text1 = """In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income."""

text2 = """e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"""

text3 = """  //wont won't won't"""

text4 = """, e   .. """

text5 = """'''  """

text6 = """sEQCV_UCGGDw/,UCGGDw,sEQCV    /sEQCV,,;sEQCV,sEQCV sEQCV//-sEQCV:?sEQCV./?sEQCV:UCGGDw!_/?;sEQCV_?:sEQCV;??UCGGDw:UCGGDw::-/ sEQCV!;?  UCGGDw,; -/sEQCV- ,:,sEQCV!sEQCV !sEQCV ,/UCGGDw-:,-?"""

print(top_3_words(text1))
print('*' * 30)
print(top_3_words(text2))
print('*' * 30)
print(top_3_words(text3))
print('*' * 30)
print(top_3_words(text4))
print('*' * 30)
print(top_3_words(text5))
print('*' * 30)
print(top_3_words(text6))
print('*' * 30)
print(collections.Counter(['a', 'b', 'c', 'a', 'b', 'b']).most_common(3))
print(collections.Counter({'a': 2, 'b': 3, 'c': 1}))
print(collections.Counter(a=2, b=3, c=1))


def top_3_words_v2(text):
    words = re.findall(r"[a-z']+", text.lower())
    print(words)
    top = collections.Counter(words).most_common(3)

    return [tpl[0] for tpl in top]


print('#' * 30)
print(top_3_words_v2(text6))
print('#' * 30)
