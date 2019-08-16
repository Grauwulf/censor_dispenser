"""These are the emails you will be censoring. 
The open() function is opening the text file 
that the emails are contained in and the .read() method is 
allowing us to save their contexts to the following variables:"""

email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

#print(email_one)

#def censor_algorithms():
    #return email_one.replace("learning algorithms", "gibberish")

#print(censor_algorithms())

proprietary_terms = ["she", "She" "personality", "matrix", "sense", "of", "self", "self-preservation", "learning", "algorithms", " her", "herself"]
negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out", "control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]

def censor_email_one(originalString, valueToCensor, valueToReplace):
    stringToReturn = originalString.replace(valueToCensor, valueToReplace)
    return stringToReturn
#print(email_two)

def censor_email_two(email):
    email_two_split = email.split()
    for terms in proprietary_terms:
        for word in email_two_split:
            if terms == word:
                word_index = email_two_split.index(word)
                email_two_split[word_index] = "*"*len(word)
    return " ".join(email_two_split)

#print(censor_email_two(email_two))

negative_words_repeated = []

def censor_email_three(email):
    email_three_split = email.split()   
    for terms in proprietary_terms:
        for word in email_three_split:
            if terms == word:
                word_index = email_three_split.index(word)
                email_three_split[word_index] = "*"*len(word)
    for term in negative_words:
        for word in email_three_split:
            if term == word:
                negative_words_repeated += term
                for bad_word in negative_words_repeated:
                    if bad_word == term:
                        email_three_split[word_index] = "*"*len(word)
                    else:
                        return term
    return " ".join(email_three_split)          

print(censor_email_three(email_three))
        
#1. Check email for negative words
#    A. If email contains negative word check the list
#        a. If list doesn't contain word, add it
#        b. If list contains word, censor it
#2. Censor words from proprietary_words