import sys
from stats import count_words, count_char, sorted_list

def get_book_text(path: str):
    file_content = None
    with open(path) as f:
        file_content = f.read()
    return file_content


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    path = sys.argv[1]
    book_text = get_book_text(path)
    book_text_count = count_words(book_text)
    book_char_count_dict = count_char(book_text)
    book_char_count_list = sorted_list(book_char_count_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {book_text_count} total words")
    print("--------- Character Count -------")
    for count_map in book_char_count_list:
        char = count_map["char"]
        count = count_map["num"]
        if char.isalpha():
            print(f"{char}: {count}")
    
    

main()