def match_word(words) :
    ctr = 0
    lst = []
    for word in words :
        if len(word) > 2 and word[0] == word[-1] :
            ctr = ctr + 1
            lst.append(word)
    print("list of words with first and last character same is" , lst)
    return ctr

x = match_word(["dad" , "aca" , "aga" , "xyz"])
print("The number of words having first and last character same", x)