import string
import random
from collections import defaultdict


corpus_path = 'data/paragraph3.txt'
# Read the corpus from the file
with open(corpus_path, 'r', encoding='utf-8') as file:
    corpus = file.read()
# Remove non-textual content
corpus = corpus.strip()
# Define the set of special characters and symbols to remove
special_chars = set(string.punctuation) - set('.,?!')  # Preserve punctuation marks: . , ? !
# Remove special characters and symbols
corpus = ''.join(char for char in corpus if char not in special_chars)
# Print the preprocessed corpus
# print(corpus)

# ----------------------------------------------
tokens = corpus.split()  # Tokenize the corpus

n = 2  # Define the value of n for n-grams

ngrams = defaultdict(list)  # Initialize the Markov chain

# Generate n-grams and build the Markov chain
for i in range(len(tokens) - n):
    ngram = tuple(tokens[i:i+n])
    next_token = tokens[i+n]
    ngrams[ngram].append(next_token)

# Function to find the starting n-gram for generating a sentence
def find_starting_ngram():
    sentence_starting_candidates = []

    for ngram in ngrams:
        if ngram[0][0].isupper():  # Check if the first word of the n-gram starts with a capital letter
            sentence_starting_candidates.append(ngram)

    if not sentence_starting_candidates:
        return random.choice(list(ngrams.keys()))

    return random.choice(sentence_starting_candidates)

# Function to generate a sentence using the Markov chain
def generate_sentence(starting_ngram, max_length=250):
    sentence = list(starting_ngram)

    while len(sentence) < max_length:
        current_ngram = tuple(sentence[-n:])
        next_token = random.choice(ngrams[current_ngram])
        sentence.append(next_token)

        # Check if the sentence ends with a sentence-ending punctuation mark
        if next_token.endswith(('.', '!', '?')):
            break

    generated_sentence = ' '.join(sentence)
    return generated_sentence

# Test the sentence generation
max_sentence_length = 250
min_sentence_length = 50

generated_sentence = ""
while len(generated_sentence) < min_sentence_length or len(generated_sentence) > max_sentence_length:
    starting_ngram = find_starting_ngram()
    generated_sentence = generate_sentence(starting_ngram, max_length=max_sentence_length)

print(generated_sentence)
