candidate_words = {}

def UniqueFirstCharacter(value):
    for word in value:
        if candidate_words.get(word, 0):
            candidate_words.pop(word)
        else:
            candidate_words[word] = True
        
        if candidate_words != {}:
            return list(candidate_words.keys())[0] 
        else:
            return "Nothing"
Unique = UniqueFirstCharacter("9239")

print(Unique) # Debug