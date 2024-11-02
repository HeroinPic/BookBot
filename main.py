def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    count = words_count(text)
    print(f"The Frankenstein book counts '{count}' words")

def get_book_text(path):
    with open(path) as f:
        return f.read()


def words_count(book):
    count = 0
    for word in book.split():
        count += 1
    return count


main()