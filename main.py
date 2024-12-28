def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    sorted_chars_dict = sort_dict(chars_dict)
    print(f"--- Begin report of {path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in sorted_chars_dict:
        if item[0].isalpha():
            print(f"The '{item[0]}' character was found {item[1]} times")

    print("--- End Report ---")


def sort_dict(dict):
    sorted_list = sorted(dict.items(), key=lambda item: item[1], reverse=True)
    filtered_list = [item for item in sorted_list if item[0] != ' ']
    return filtered_list


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1

    return chars


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
