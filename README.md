# Word Count & Character Analysis Report

This script analyzes a given text file and generates a report on the number of words and the frequency of individual alphabetic characters found in the document. It is a simple tool for gaining insights into the structure of a text.

## Features

- **Word Count**: Counts the total number of words in the text file.
- **Character Frequency Analysis**: Displays the frequency of each alphabetic character (case insensitive).

## How It Works

The script reads the content of a text file, counts the words, and calculates the frequency of each alphabetic character. It then prints a report detailing the results.

### Functions Overview

1. **`read_file(filepath)`**: Reads the content of a given file.
2. **`count_words(file_content)`**: Counts the number of words in the file content.
3. **`count_chars(file_content)`**: Counts the occurrences of each character in the file content (ignoring case).
4. **`print_report(file_content)`**: Generates a report of the word count and character frequency.

## Usage Instructions

1. **Create a directory named `books` in the root directory** of your project.
2. **Add a text file** of any book or document you wish to analyze in the `books` directory.
3. **Update the file path** in the `print_report()` function call to match the path of your text file.
   
   For example:
   ```python
   print_report(read_file("books/frankenstein.txt"))
   ```
4. Run the script to get the word count and character frequency report.

## Example Output

The script generates a report similar to this:

```
--- Begin report of books/frankenstein.txt ---
43205 words found in the document

The 'e' character was found 25432 times
The 't' character was found 18254 times
The 'a' character was found 15342 times
...
```

The report begins with a summary of the total word count, followed by the frequency of each alphabetic character in descending order.

## Requirements

- Python 3

## Notes

- Ensure the text file you want to analyze is properly formatted to avoid errors during processing.
- The script ignores non-alphabetic characters when generating the character frequency report.

## Improvements

This script could be extended in the future to include:
- **More detailed analysis** like sentence count, average word length, etc.
- **Exclusion of common stop words** for a more meaningful word frequency analysis.
- **Additional file formats** support such as PDFs or DOCX.

## License

This project is open-source and free to use and modify.

