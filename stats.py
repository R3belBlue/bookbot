def word_count(book_text):
    words = book_text.split()
    w_count = len(words)
    return w_count
def char_count(book_text):
    lower_case = book_text.lower()
    char_counts = {}
    for char in lower_case:
        char_counts[char] = char_counts.get(char, 0) +1
    return char_counts
def sort_on(item):
    return item["num"]
def report_sort(char_counts):
    alpha_sort = []
    for char, count in char_counts.items():
        if not char.isalpha():
            continue
        alpha_sort.append({"char": char, "num": count})
    alpha_sort.sort(reverse=True, key=sort_on)
    return alpha_sort