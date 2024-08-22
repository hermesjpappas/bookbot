def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    num_words = get_num_words(text)
    letters_dict = get_characters_count(text)

    



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
