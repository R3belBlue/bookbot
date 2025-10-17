from stats import word_count, char_count, report_sort
import sys
if len(sys.argv) != 2:
    print("please tpye path to book you wish to use")
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
path = sys.argv[1]

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents
def main():
    
    book_text = get_book_text(path)
    wc = word_count(book_text)
    cc = char_count(book_text)
    rs = report_sort(cc)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {wc} total words")
    print("--------- Character Count -------")
    for item in rs:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
if __name__ == "__main__":
    main()

