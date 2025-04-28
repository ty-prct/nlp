import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')

sentence = "The quick brown fox jumps over the lazy dog."

tokens = nltk.word_tokenize(sentence)

pos_tags = nltk.pos_tag(tokens)
print(pos_tags)
print("--" * 20)
print("POS Tags using NLTK:")
for token, tag in pos_tags:
    print(f"{token} --> {tag}")