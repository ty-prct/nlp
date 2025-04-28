import spacy
from sklearn.metrics import classification_report
nlp = spacy.load("en_core_web_sm")

text = """
Apple Inc. was founded by Steve Jobs and Steve Wozniak in Cupertino, California on April 1, 1976. 
They introduced the iPhone in 2007, which became a massive success, generating billions of dollars.
"""

doc = nlp(text)

print("Named Entities:\n")
for ent in doc.ents:
    print(f"{ent.text} --> {ent.label_}")

true_entities = [
    ("Apple Inc.", "ORG"),
    ("Steve Jobs", "PERSON"),
    ("Steve Wozniak", "PERSON"),
    ("Cupertino", "GPE"),
    ("California", "GPE"),
    ("April 1, 1976", "DATE"),
    ("2007", "DATE"),
]

predicted_entities = [(ent.text, ent.label_) for ent in doc.ents]

y_true = []
y_pred = []

for true_text, true_label in true_entities:
    y_true.append(true_label)
    
    matched_label = "NO_ENTITY"
    for pred_text, pred_label in predicted_entities:
        if true_text.lower() == pred_text.lower():
            matched_label = pred_label
            break
    y_pred.append(matched_label)

print("\nEvaluation Report:")
print(classification_report(y_true, y_pred, zero_division=0))