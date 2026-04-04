def to_jaden_case(string):
    gr = 0
    string += " "
    word = ""
    lst = []
    real_lst = ""
    for letter in string :
        gr += 1 
        if gr == 1 :
            letter = letter.upper()
        word += letter 
        if letter == " ":
            lst.append(word)
            word = ""
            gr = 0
    for wrd in lst :
        real_lst += wrd 
    return real_lst.strip()
    

print(to_jaden_case("How can mirrors be real if our eyes aren't real"))