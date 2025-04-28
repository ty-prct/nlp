import nltk
import re
import string
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk import ngrams, FreqDist
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt_tab')

text = """I love natural language processing. It is one of the most exciting fields in Artificial Intelligence. 
Natural Language Processing involves teaching machines how to understand and generate human language."""

text = text.lower()

text = re.sub(f'[{re.escape(string.punctuation)}]', '', text)

tokens = nltk.word_tokenize(text)

stop_words = set(stopwords.words('english'))
tokens = [word for word in tokens if word not in stop_words]

lemmatizer = WordNetLemmatizer()
tokens = [lemmatizer.lemmatize(word) for word in tokens]

print(f"Preprocessed Tokens:\n{tokens}")

def generate_ngrams(tokens, n):
    n_grams = list(ngrams(tokens, n))
    return n_grams

unigrams = generate_ngrams(tokens, 1)
bigrams = generate_ngrams(tokens, 2)
trigrams = generate_ngrams(tokens, 3)

def plot_ngram_freq(ngrams_list, title):
    freq_dist = FreqDist(ngrams_list)
    common_ngrams = freq_dist.most_common(10)
    
    ngrams_text = [' '.join(gram) for gram, freq in common_ngrams]
    freqs = [freq for gram, freq in common_ngrams]
    
    plt.figure(figsize=(10,5))
    plt.bar(ngrams_text, freqs, color='skyblue')
    plt.title(title)
    plt.xticks(rotation=45)
    plt.xlabel('N-Grams')
    plt.ylabel('Frequency')
    plt.show()

plot_ngram_freq(unigrams, "Top 10 Unigrams")
plot_ngram_freq(bigrams, "Top 10 Bigrams")
plot_ngram_freq(trigrams, "Top 10 Trigrams")