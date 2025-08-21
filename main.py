from stats import word_count, character_count, sort_dict
import sys


def main():
    text = get_book_text(sys.argv[1])
    num_word = word_count(text)
    char_count = character_count(text)
    sorted_char_count = sort_dict(char_count)

    print(f"============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------\nFound {num_word} total words\n--------- Character Count -------")
    for char in sorted_char_count:
        if char['char'].isalpha():
            print(f"{char['char']}: {char['num']}")
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    

if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
else:
    main()

