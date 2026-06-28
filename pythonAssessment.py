import re
import string

def count_specific_word(text, search_word):
    if text == "" or search_word == "":
        return 0
        
    text_lower = text.lower()
    word_lower = search_word.lower()
    
    count = text_lower.count(word_lower)
    
    if count > 0:
        return count
    else:
        return 0

def identify_most_common_word(text):
    if text == "":
        return None
        
    words = re.findall(r'\b\w+\b', text.lower())
    
    if not words:
        return None
        
    word_counts = {}
    
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
            
    most_common = max(word_counts, key=word_counts.get)
    return most_common

def calculate_average_word_length(text):
    if text == "":
        return 0.0
        
    words = re.findall(r'\b[a-zA-Z]+\b', text)
    
    if not words:
        return 0.0
        
    total_length = 0
    index = 0
    
    while index < len(words):
        total_length += len(words[index])
        index += 1
        
    average_length = total_length / len(words)
    return float(average_length)

def count_paragraphs(text):
    if text == "":
        return 1
        
    paragraphs = text.split('\n\n')
    
    valid_paragraphs = 0
    for p in paragraphs:
        if p.strip() != "":
            valid_paragraphs += 1
        else:
            continue
            
    return valid_paragraphs if valid_paragraphs > 0 else 1

def count_sentences(text):
    if text == "":
        return 1
        
    periods = text.count('.')
    exclamations = text.count('!')
    questions = text.count('?')
    
    total_sentences = periods + exclamations + questions
    
    if total_sentences == 0 and text.strip() != "":
        return 1
    return total_sentences if total_sentences > 0 else 1

if __name__ == "__main__":
    sample_article = """
    The tech industry is booming with new advancements in NLP. NLP is changing the way we interact with data! 
    Are you ready for the future?

    Startups are leading this wave. Our NLP models analyze text efficiently.
    """

    empty_article = ""

    print("--- NLP Text Analysis Initialization ---")
    
    print("\n[TESTING: Standard News Article]")
    search_target = "NLP"
    print(f"1. Target Word Count ('{search_target}'):", count_specific_word(sample_article, search_target))
    print("2. Most Common Word:", identify_most_common_word(sample_article))
    print("3. Average Word Length:", round(calculate_average_word_length(sample_article), 2))
    print("4. Total Paragraphs:", count_paragraphs(sample_article))
    print("5. Total Sentences:", count_sentences(sample_article))

    print("\n[TESTING: Edge Cases (Empty String)]")
    print("1. Target Word Count ('NLP'):", count_specific_word(empty_article, "NLP"))
    print("2. Most Common Word:", identify_most_common_word(empty_article))
    print("3. Average Word Length:", calculate_average_word_length(empty_article))
    print("4. Total Paragraphs:", count_paragraphs(empty_article))
    print("5. Total Sentences:", count_sentences(empty_article))
    
    print("\n[FILE ANALYSIS]")
    try:
        with open('news_article.txt', 'r') as file:
            file_content = file.read()
            print("File loaded successfully. Running analysis...")
            user_word = input("Enter a specific word to count in the article: ")
            
            print(f"\n--- Results for 'news_article.txt' ---")
            print(f"Count of '{user_word}': {count_specific_word(file_content, user_word)}")
            print(f"Most Common Word: {identify_most_common_word(file_content)}")
            print(f"Average Word Length: {calculate_average_word_length(file_content):.2f}")
            print(f"Total Paragraphs: {count_paragraphs(file_content)}")
            print(f"Total Sentences: {count_sentences(file_content)}")
            
    except FileNotFoundError:
        print("Note: 'news_article.txt' was not found in the directory. Please ensure the file is present to run the live file analysis.")