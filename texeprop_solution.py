# create function for create sentence
def sentence_maker(phrase):
    interrogatives = ("how", "what", "why")  # Interrogative word how, when why,what
    capitalized = phrase.capitalize()
    if phrase.startswith(interrogatives):   #To concatinate . or ? at the end of phrase
       return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized) 


result = []
while True:
    username = input("Say something: ")
    if username == '\end': # if user enter (\end) input loop will break
        break

    else:
        result.append(sentence_maker(username))
print(" ".join(result)) # join all sentences together 
