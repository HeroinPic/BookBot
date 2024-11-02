def main():
    print("Give me the file path of the book")
    book_path = input()
    print(f"Initializing report of {book_path}")
    text = get_book_text(book_path)
    count = words_count(text)
    print(f"The Frankenstein book counts '{count}' words")
    report = character_count(text)
    for re in report:
        print (f"The character '{re}' has been used -{report[re]} times")
    print ("-----End of report-----")


def get_book_text(path):
    with open(path) as f:
        return f.read()


def words_count(book):
    count = 0
    for word in book.split():
        count += 1
    return count


def character_count(book):
    character_dict = {}
    for char in book:
        lowered = char.lower()
        if lowered in character_dict:
            character_dict[lowered] += 1
        else:
            character_dict[lowered] = 1
    return character_dict


main()