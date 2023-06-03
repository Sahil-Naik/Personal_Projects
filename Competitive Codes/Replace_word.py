def replace_word(list_of_words, base_word, replace_with):
    print("Before replacing: {}".format(list_of_words))
    get_index = list_of_words.index(base_word)
    list_of_words[get_index] = replace_with
    print("After replacing: {}".format(list_of_words))
    
test_arr = ['cats', 'dugs', 'mouse', 'mice', 'rats', 'bat']
word_to_replace = 'dugs'
replaced_word = 'dogs'
replace_word(test_arr, word_to_replace, replaced_word)
