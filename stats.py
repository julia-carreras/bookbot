def get_num_words(text):
    words = text.split()
    return len(words)


def count_characters_ocurrences(text):
    text = text.lower()
    character_counts = {}
    
    for character in text:
        if character in character_counts:
            character_counts[character] += 1
        else:
            character_counts[character] = 1
    return character_counts


def sort_characters_by_count(dictionary):
    sorted_items = sorted(dictionary.items(), key=lambda item: item[1], reverse=True)
    return dict(sorted_items)

# This part only runs if you run *stats.py* directly (python3 stats.py)
if __name__ == "__main__":  
    text = get_book_text("books/frankenstein.txt")

    word_count = get_num_words(text)
    print(f"{word_count} words found in the document")

    character_counts = count_characters_ocurrences(text)
    print(character_counts)

    sorted_character_counts = sort_characters_by_count(character_counts)
    print(sorted_character_counts)
