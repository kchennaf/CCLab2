import nltk
#   nltk.download('punkt')

# nltk.download('stopwords')
import re

from collections import Counter
counter = 0
from nltk.corpus import stopwords

def get_tokens():
   with open('C:\\Users\Chennaf\Downloads\FirstContactWithTensorFlow.txt', 'r') as tf:
    text = tf.read()
    lowers = text.lower()
    no_punctuation = re.sub(r'[^\w\s]', '', lowers)
    tokens = nltk.word_tokenize(no_punctuation)
    print('Total number of words in the book including punctuation & stopwords  is ' + str(len(text)) + '.')
    print('Total number of words in the book excluding punctuation  is ' + str(len(tokens)) + '.')
    return tokens

tokens = get_tokens()
# the lambda expression below this comment
# stores stopwords in a variable for eficiency:
# it avoids retrieving them from ntlk for each iteration
sw = stopwords.words('english')
filtered = [w for w in tokens if not w in sw]
count = Counter(filtered)
print('Total number of words in the book excluding punctuation & stopwords is ' + str(len(filtered)) + '.')
print('The ten most common words excluding punctuation & stopwords are:')
print (count.most_common(10))