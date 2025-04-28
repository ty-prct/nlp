import nltk
from nltk.corpus import wordnet as wn
nltk.download('wordnet')
nltk.download('omw-1.4') 

words = ['dog', 'cat', 'park']

def find_semantic_relations(word):
    synsets = wn.synsets(word)
    if not synsets:
        print(f"No synsets found for {word}")
        return
    
    print(f"\nWord: {word}")
    print(f"Definition: {synsets[0].definition()}")
    
    synonyms = set()
    for syn in synsets:
        for lemma in syn.lemmas():
            synonyms.add(lemma.name())
    print(f"Synonyms: {synonyms}")
    
    antonyms = set()
    for syn in synsets:
        for lemma in syn.lemmas():
            if lemma.antonyms():
                antonyms.add(lemma.antonyms()[0].name())
    print(f"Antonyms: {antonyms}")
    
    hypernyms = synsets[0].hypernyms()
    print(f"Hypernyms: {[h.name().split('.')[0] for h in hypernyms]}")
    
    hyponyms = synsets[0].hyponyms()
    print(f"Hyponyms: {[h.name().split('.')[0] for h in hyponyms]}")
    
    meronyms = synsets[0].part_meronyms()
    print(f"Meronyms (Parts): {[m.name().split('.')[0] for m in meronyms]}")
    
    holonyms = synsets[0].member_holonyms()
    print(f"Holonyms (Wholes): {[h.name().split('.')[0] for h in holonyms]}")

for word in words:
    find_semantic_relations(word)