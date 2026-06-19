import sys
from stats import get_num_words, get_num_chars, chars_dict_to_sorted_list

def main():
    if len(sys.argv) > 1:
        path = sys.argv[1]
        s = get_book_text(path)
        c = get_num_words(s)
        n = get_num_chars(s)
        l = chars_dict_to_sorted_list(n)
        print_report(path, c, l)
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

def get_book_text(path_to_file: str) -> str:
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents
    
def print_report(book_path: str, word_count: list, sorted_list_char_count: list) -> None:
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {len(word_count)} total words")
    print("--------- Character Count -------")
    for item in sorted_list_char_count:
        if item[0].isalpha():
           a = item[0]
           b = item[1]
           print(f"{a}: {b}")
    print("============= END ===============")

main()