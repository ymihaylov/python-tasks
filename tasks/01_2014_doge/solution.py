def wow_such_much(start, end):
    result = []

    for x in range(start, end):
        if x % 3 == 0 and x % 5 == 0:
            result.append('suchmuch')
        elif x % 3 == 0:
            result.append('such')
        elif x % 5 == 0:
            result.append('much')
        else:
            result.append(str(x))

    return result

PARASITIC_WORDS = [
    'wow',
    'lol',
    'so',
    'such',
    'much',
    'very',
]


def count_doge_words(sentence):
    sentence_words = sentence.split()
    words_count = 0

    for parasitic_word in PARASITIC_WORDS:
        words_count += sentence_words.count(parasitic_word)

    return words_count
