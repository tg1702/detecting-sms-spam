import string

from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer




def transform_text(text):
    nltk.download('punkt')
    nltk.download('punkt_tab')
    nltk.download('stopwords')

    ps = PorterStemmer()
    text = text.lower()
    text = nltk.word_tokenize(str(text))

    y = []
    for char in text:
        if char.isalnum():
            y.append(char)

    text = y[:]

    y.clear()

    for char in text:
        if char not in stopwords.words('english') and char not in string.punctuation:
            y.append(char)

    text = y[:]

    y.clear()

    for char in text:
        y.append(ps.stem(char))

    return " ".join(y)
