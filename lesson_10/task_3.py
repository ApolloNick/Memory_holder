def longest_word(sequence_of_words):
    return max(sequence_of_words.split(), key=len)


print(longest_word("What makes a good man"))
