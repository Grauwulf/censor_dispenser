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

proprietary_terms = ["she", "She", "personality", "matrix", "sense", "of", "self", "self-preservation", "learning", "algorithms", " her", "herself"]
negative_words = ["concerned", "concerning", "behind", "danger", "dangerous", "alarming", "alarmed", "out", "control", "control." "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]

def censor_email_one(originalString, valueToCensor, valueToReplace):
    stringToReturn = originalString.replace(valueToCensor, valueToReplace)
    return stringToReturn
#print(censor_email_one(email_one))

def censor_email_two(email):
    email_two_split = email.split()
    for terms in proprietary_terms:
        for word in email_two_split:
            if terms == word:
                word_index = email_two_split.index(word)
                email_two_split[word_index] = "*"*len(word)
    return " ".join(email_two_split)

#print(censor_email_two(email_two))

def censor_email_three(email):
    negative_words_repeated = {}
    email_three_split = email.split()   
    for word in negative_words:
        for term in email_three_split:
            if word == term:
                if not word in negative_words_repeated: #This if/else statement currently determines if the word from negative words is in the email
                    negative_words_repeated[word] = 1   #If it isn't, it adds it if it is 
                elif word in negative_words_repeated:
                    negative_words_repeated[word] += 1
                else:
                    return word
    for word in negative_words_repeated:
        if negative_words_repeated[word] >= 2:
            proprietary_terms.append(word)
    for terms in proprietary_terms: #Censors the words in the list proprietary_terms
        for word in email_three_split:
            if terms == word:
                word_index = email_three_split.index(word)
                email_three_split[word_index] = "*"*len(word)
    return " ".join(email_three_split) 

def censor_email_four(email):
    negative_and_proprietary = []
    email_four_split = email.split()   
    for word in negative_words:
        negative_and_proprietary.append(word)
    for word in proprietary_terms:
        negative_and_proprietary.append(word)
    
    for terms in negative_and_proprietary: #Censors the words in the list negative_and_proprietary
        for word in email_four_split:
            if terms == word:
                word_index = email_four_split.index(word)
                email_four_split[(word_index)-1] = "*"*len(word)
                email_four_split[word_index] = "*"*len(word)
                email_four_split[(word_index)+1] = "*"*len(word)
    return " ".join(email_four_split) 

print(censor_email_four(email_four))