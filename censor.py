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

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]

def censor_algorithms(originalString, valueToCensor, valueToReplace):
    stringToReturn = originalString.replace(valueToCensor, valueToReplace)
    return stringToReturn

def censor_more_algorithms(string):
    for terms in proprietary_terms:
        if terms == email_two:
            string.replace(terms, "censored")
    return string

print(censor_more_algorithms(email_two))
#print(censor_algorithms(email_two, proprietary_terms, "gibberish"))