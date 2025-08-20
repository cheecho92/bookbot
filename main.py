from stats import word_count, character_count, sort_dict, sort_on


def main():
    text = get_book_text("books/frankenstein.txt")
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
    

main()

