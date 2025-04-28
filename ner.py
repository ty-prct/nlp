import spacy

nlp = spacy.load("en_core_web_sm")

text = "Utkarsh Pingale was born on 8:30 am in Pune and go to AISSMSIOIT college"

doc = nlp(text)

for word in doc:
    if word.ent_type_:
        print(f"{word.text:<15} -> {word.ent_type_}")
    else:
        print(f"{word.text:<15} -> None")

print()
for word in doc.ents:
    print(f"{word.text:<15} : {word.label_}")