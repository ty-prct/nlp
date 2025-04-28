morphology_table = [
    {'Word': 'play', 'Form': 'playing', 'Tense': 'present continuous'},
    {'Word': 'run', 'Form': 'running', 'Tense': 'present continuous'},
    {'Word': 'drive', 'Form': 'driven', 'Tense': 'past participle'}
]

def display_table(table):
    print(f"{'Word':<10} {'Form':<15} {'Tense':<20}")
    print("-" * 45)
    for entry in table:
        print(f"{entry['Word']:<10} {entry['Form']:<15} {entry['Tense']:<20}")

def add_word(word, form, tense):
    morphology_table.append({'Word': word, 'Form': form, 'Tense': tense})
    print(f"\nAdded: {word}, {form}, {tense}")

def delete_word(word):
    global morphology_table
    morphology_table = [entry for entry in morphology_table if entry['Word'] != word]
    print(f"\nDeleted word: {word}")

print("Initial Morphology Table:")
display_table(morphology_table)

add_word('eat', 'eating', 'present continuous')

delete_word('run')

print("\nFinal Morphology Table:")
display_table(morphology_table)
