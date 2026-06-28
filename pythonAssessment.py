import re
from collections import Counter

def count_specific_word(text, word):
    words = re.findall(r'\b' + re.escape(word.lower()) + r'\b', text.lower())
    return len(words)

def identify_most_common_word(text):
    if not text.strip():
        return None
    words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
    if not words:
        return None
    return Counter(words).most_common(1)[0][0]

def calculate_average_word_length(text):
    if not text.strip():
        return 0
    words = re.findall(r'\b[a-zA-Z]+\b', text)
    if not words:
        return 0
    return sum(len(word) for word in words) / len(words)

def count_paragraphs(text):
    paragraphs = [p for p in text.split('\n\n') if p.strip()]
    return len(paragraphs) if paragraphs else 1

def count_sentences(text):
    sentences = re.findall(r'[^.!?]*[.!?]', text)
    return len(sentences)

article = input("Paste your news article text here:\n")
search_word = input("Enter a word to search for: ")

word_count = count_specific_word(article, search_word)
most_common = identify_most_common_word(article)
avg_length = calculate_average_word_length(article)
paragraphs = count_paragraphs(article)
sentences = count_sentences(article)

print(f"\nWord '{search_word}' count: {word_count}")
print(f"Most common word: {most_common}")
print(f"Average word length: {avg_length:.2f}")
print(f"Number of paragraphs: {paragraphs}")
print(f"Number of sentences: {sentences}")

i = 0
while i < 1:
    if word_count > 0:
        print(f"\nThe word '{search_word}' was found in the article.")
    else:
        print(f"\nThe word '{search_word}' was not found in the article.")
    i += 1