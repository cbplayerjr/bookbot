def get_num_words(book_text: str) -> list:
    return book_text.split()

def get_num_chars(book_text: str) -> dict:

    num_chars = {}
    text = book_text.lower()
    for i in range(len(text)):
        a = text[i]
        if a in num_chars:
            num_chars[a] += 1
        else:
            num_chars[a] = 1
    return num_chars

def sort_on(num_chars: tuple[str, int]) -> int:
    return num_chars[1]

def chars_dict_to_sorted_list(num_chars_dict: dict[str, int]) -> list[tuple[str, int]]:
    chars_list: list[tuple[str, int]] = []
    for char in num_chars_dict:
        count = num_chars_dict[char]
        chars_list.append((char, count))
    return sorted(chars_list, reverse=True, key=sort_on)