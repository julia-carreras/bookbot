# FROM FILE TO STRING
def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()
    return file_contents
    
text = get_book_text("books/frankenstein.txt")

# COUNT WORDS
def get_num_words(text):
    words = text.split()
    return len(words)

word_count = get_num_words(text)
print(f"{word_count} words found in the document")

# COUNT CHARACTERS DICTIONARY
def count_characters_ocurrences(text):
    text = text.lower()
    character_counts = {}
    
    for character in text:
        if character in character_counts:
            character_counts[character] += 1
        else:
            character_counts[character] = 1
    return character_counts

character_counts = count_characters_ocurrences(text)
print(character_counts)

# SORT CHARACTERS BY COUNT 
def sort_characters_by_count(dictionary):
    sorted_items = sorted(dictionary.items(), key=lambda item: item[1], reverse=True)
    return dict(sorted_items)

sorted_character_counts = sort_characters_by_count(character_counts)
print(sorted_character_counts)
