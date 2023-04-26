def anagrams(word, word_list):

    sorted_word = sorted(word.lower())
    anagrams = []
    for string in word_list:

        sorted_string = sorted(string.lower())

        if sorted_word == sorted_string:

            anagrams.append(string)
    return anagrams

word = "listen"
word_list = ["enlists", "google", "inlets", "banana"]
anagrams_list = anagrams(word, word_list)
print(anagrams_list)