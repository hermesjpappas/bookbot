def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    num_words = get_num_words(text)
    letters_dict = get_characters_count(text)

    chars_dict_list = []
    for char in letters_dict:
        if char.isalpha():
            chars_dict_list.append({"name": char, "num": letters_dict[char]})

    chars_dict_list.sort(reverse=True, key=sort_on)

    print ("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print()
    for dict in chars_dict_list:
        print(f"The '{dict['name']}' character was found {dict['num']} times")

    print()
    print("--- End report ---")

def sort_on(dict):
    return dict["num"]


def get_characters_count(text):
    words = text.split()
    letters_dict = {}
    for word in words:
        lowercase_word = word.lower()
        for character in lowercase_word:
            if character in letters_dict:
                letters_dict[character] += 1
            else:
                letters_dict[character] = 1

    return letters_dict


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_num_words(text):
    words = text.split()
    return len(words)


main()
