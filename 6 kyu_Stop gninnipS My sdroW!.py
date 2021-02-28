"""
Write a function that takes in a string of one or more words, and returns the same string, but with all five or more
letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces.
Spaces will be included only when more than one word is present.

Examples: spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" spinWords( "This is a test") => returns
"This is a test" spinWords( "This is another test" )=> returns "This is rehtona test"
"""
def drehen(word):
    word=list(word)
    word.reverse()
    neu=''
    for i in word:
        neu += i 
    return neu

def spin_words(sentence):
    words=sentence.split()
    for i in range(len(words)):
        if len(words[i])>4:
            words[i] = drehen(words[i])
    
    new_sentence = ''
    for i in words:
        new_sentence += i+' '    
    
    return new_sentence[:-1]

print(spin_words("Welcome"))

#Alternative Lösungen:
#return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])

#words = [word for word in sentence.split(" ")]
#words = [word if len(word) < 5 else word[::-1] for word in words]
#return " ".join(words)