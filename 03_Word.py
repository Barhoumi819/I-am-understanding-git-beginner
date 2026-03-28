# def word_setence(s1et):
#     s1et += " "
#     lst = []
#     word = ""
#     for letter in s1et :
#         if letter == " ":
#             lst.append(word.strip())
#             word = ""
#         word += letter
#     print(lst,word)
# word_setence("Hello My name is Barhoumi") 

def camel_case(sent) :
    new_sent = ""
    for letter in sent :
        if letter == " ":
            # new_sent += letter.upper()
            pass
            
        else :
            new_sent += letter
    
    print(new_sent)
    return new_sent


camel_case("Hello my name is barhoumi")