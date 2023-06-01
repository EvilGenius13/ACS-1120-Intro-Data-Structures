import string
from collections import Counter
import timeit
import sys

def create_word_histogram(file_path):
    with open(file_path, 'r') as file:
        text = file.read()

        # Remove punctuation and numbers
        translator = str.maketrans('', '', string.punctuation + string.digits)
        text = text.translate(translator)

        # Convert text to lowercase and split into words
        words = text.lower().split()

        # Create a word histogram
        word_histogram = Counter(words)
        # Backup method
        # word_histogram = {}
        # for word in words:
        #     if word in word_histogram:
        #         word_histogram[word] += 1
        #     else:
        #         word_histogram[word] = 1
        return word_histogram

# Txt file option
if __name__ == "__main__":
    if len(sys.argv) > 1:
         file_name = sys.argv[1]
         file_path = f'data/{file_name}.txt'
    else:
        file_path = 'data/paragraph.txt'

    # Measure execution time using timeit
    execution_time = timeit.timeit(lambda: create_word_histogram(file_path), number=1)

    # Print the histogram
    histogram = create_word_histogram(file_path)
    for word, count in histogram.items():
        print(f'{word}: {count}')

    # Print the execution time
    print(f"Execution Time: {execution_time} seconds")
