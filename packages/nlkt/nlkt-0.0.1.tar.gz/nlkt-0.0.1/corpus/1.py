import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer, PorterStemmer
from nltk.corpus import stopwords
import string

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

def preprocess_text(text):
    
    tokens = word_tokenize(text.lower())
    tokens = [token for token in tokens if token not in string.punctuation]
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]
    return tokens

def lemmatize(tokens):
    lemmatizer = WordNetLemmatizer()
    lemmas = [lemmatizer.lemmatize(token) for token in tokens]
    return lemmas

def stem(tokens):
    stemmer = PorterStemmer()
    stems = [stemmer.stem(token) for token in tokens]
    return stems

def main():
    text = "Tokenization is the process of breaking down text into words and phrases. Stemming and Lemmatization are techniques used to reduce words to their base form."
    tokens = preprocess_text(text)
    lemmas = lemmatize(tokens)
    print("Lemmatization:")
    print(lemmas)
    stems = stem(tokens)
    print("\nStemming:")
    print(stems)

if __name__ == "__main__":
    main()