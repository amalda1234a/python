word =input("enter a string")
if len(word)>1:
    new_word=word[-1]+word[1:-1]+word[0]
else:
    new_word = word
print ("string after exchanging first and last characters:",new_word)
