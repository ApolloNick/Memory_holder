def longest_word(sequence_of_words):
    length_of_words = []
    for word in sequence_of_words.split():
        length_of_words.append((len(word), word))
    length_of_words.sort()
    print(length_of_words[-1][1])


longest_word("What makes a good man")
