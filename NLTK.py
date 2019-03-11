import nltk
#   nltk.download('punkt')
import re

from collections import Counter
counter = 0

def get_tokens():
   with open('C:\\Users\Chennaf\Downloads\FirstContactWithTensorFlow.txt', 'r') as tf:
    text = tf.read()
    tokens = nltk.word_tokenize(text)
    print('Total number of words in the book is ' + str(len(text)) + '.')
    return tokens

tokens = get_tokens()
count = Counter(tokens)
print('The ten most common words are:')
print (count.most_common(10))



