import string
""" Function for Creating, Transforming and Adding Prefix to Strings."""

def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.
    
    param word: str - takes the given word
    retutn: str - of root word prepended  with 'un'.
    
    """
    return 'un' + word

print(add_prefix_un("happy"))
print(add_prefix_un("manageable"))


def make_word_groups(vocab_words):
    """ Transform a list containg a prefix and words into a strings with the prefix followed by the word with prefix prepended
    
    param vocab_words: list - a vocabulary word with prefix in the first index
    return: str - of prefix followed by word with prefix applied.
    
    This function takes in 'vocab_words' list and return a string
    with the prefix and the word with the prefix applied and seperated by '::' . 
    
    For example list('en', 'close', 'joy', 'lighten), will return the following strings:
    'en :: enclose :: enjoy :: enlighten' .
    
    """
    
    new_vocab = [vocab_words[0]] + [vocab_words[0] + word for word in vocab_words if word != vocab_words[0]]
    return ' :: '.join(new_vocab)
        

print(make_word_groups(['en', 'close', 'joy', 'lighten']))
print(make_word_groups(['pre', 'serve', 'dispose', 'position']))
print(make_word_groups(['auto', 'didactic', 'graph', 'mate']))
print(make_word_groups(['inter', 'twine', 'connected', 'dependent']))

def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.
 
    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.
 
    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """
    if word[-5] == 'i':
        return word[:-5] + 'y'
    return word[:-4]

print(remove_suffix_ness("heaviness"))
print(remove_suffix_ness("sadness"))

        
def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set.", 2) becomes "darken".
    """
    word = sentence.split()[index].strip('.')
    return word  + 'en'
    
#One can use the string module for the above and instead of just mention one punctuation,
#One canthen use the whole collection of punctuation using the "string.punctuation" attribute

print(adjective_to_verb('I need to make that bright.', -1 ))
print(adjective_to_verb('It got dark as the sun set.', 2))