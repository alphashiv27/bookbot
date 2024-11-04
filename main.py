from collections import Counter


def read_file(filepath):
    with open(filepath) as f:
        file_content =f.read()
        return file_content

def print_report(file_content):
    words_count = count_words(file_content)
    chars_map_elements = list(count_chars(file_content).items())

    chars_map_elements.sort(reverse=True, key=lambda x: x[1])

    print("--- Begin report of books/frankenstein.txt ---")
    print(words_count ,"words found in the document")
    print("")

    for char in chars_map_elements:
        if char[0].isalpha():
            print(f"The '{char[0]}' character was found {char[1]} times")


def count_chars(file_content):
   file_string = file_content.lower()
   return Counter(file_string)

def count_words(file_content):
    return len(file_content.split())


# 1. Create a directory `books` in the root directory
# 2. Add a text file on any book
# 3. Paste the path here to get your report
print_report(read_file("books/frankenstein.txt"))
