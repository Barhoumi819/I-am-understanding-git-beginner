def count_words(sentence):
    sentence += " "
    word = ""
    ster = []
    count = 0
    for letter in sentence:
        if letter == " ":
            ster.append(word.strip())
            word = ""
        word += letter 
    for number in ster :
        count +=1
    return count



print(count_words("Hello my name is barhoumi"))

# finally finshed let us seewhat is going to happen with this git thing