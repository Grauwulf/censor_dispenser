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
    return " ".join(email_two_split) #joins back e list into str

print(censor_email_two(email_two))


#print(censor_email_two(email_two))
#print(censor_algorithms(email_two, proprietary_terms, "gibberish"))