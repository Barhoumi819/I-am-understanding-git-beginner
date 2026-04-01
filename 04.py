def count_words(sentence):
    word = ""
    ster = []
    for letter in sentence:
        word += letter 
        if letter == " ":
            ster.append(word.strip())
            word = ""