import random
import sys
import timeit

def random_words(num_words):
    filepath = "/usr/share/dict/words"

    with open(filepath) as file:
        words = file.read().splitlines()

        random_words = random.sample(words, num_words)
        sentence = " ".join(random_words)
        return sentence

if __name__ == "__main__":
    num_words = int(sys.argv[1])

    # Define the setup code
    setup_code = """
import random
from __main__ import random_words
"""

    # Define the code snippet
    code_snippet = f"""
num_words = {num_words}
sentence = random_words(num_words)
"""

    # Measure the execution time using timeit
    execution_time = timeit.timeit(code_snippet, setup=setup_code, number=1)

    # Generate and print the sentence
    sentence = random_words(num_words)
    print("Generated sentence:", sentence)
    print(f"Execution time: {execution_time} seconds")