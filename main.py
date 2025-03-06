from stats import get_num_words, count_characters_ocurrences, sort_characters_by_count


with open ("books/frankenstein.txt") as f:
    book_text = f.read()

word_count = get_num_words(book_text)
character_counts = count_characters_ocurrences(book_text)
sorted_character_counts = sort_characters_by_count(character_counts)

print(f'''
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {word_count} total words 
--------- Character Count -------''')

for character, count in sorted_character_counts.items():
    if character.isalpha():
        print(f"{character}: {count}")

print("============= END ===============")