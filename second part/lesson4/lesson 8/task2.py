synonym_dict = {
    'Beautiful': 'Gorgeous',
    'Ugly': 'Hideous',
    'Complex': 'Confusing',
    'Simple': 'Easy',
    'Happy': 'Joyful',
    'Sad': 'Unhappy',
    'Fast': 'Quick',
    'Love': 'Oksana',
    'Family': 'Hassan, Oksana and Rodion',
    'Slow': 'Leisurely',
    'Smart': 'Intelligent',
    'Dull': 'Boring',
}

def suggest_synonym(word):
    word = word.title()

    return synonym_dict.get(word, "No synonym found.Think again!" )

user_input = input("Enter a word to find its synonym: ")
synonym = suggest_synonym(user_input)
print(f"Synonym for '{user_input}': {synonym}")
