from __future__ import division, print_function
import random
from dictogram import Dictogram


class MarkovChain:
    def __init__(self, order=2):
        self.order = order  # Order of the Markov chain (default: 1)
        self.transitions = {}  # Store the transition probabilities

    def train(self, data):
        # Convert input data into n-grams
        ngrams = self._generate_ngrams(data)

        # Build transition matrix
        for ngram in ngrams:
            prefix = tuple(ngram[:-1])
            suffix = ngram[-1]
            if prefix not in self.transitions:
                self.transitions[prefix] = Dictogram()
            self.transitions[prefix].add_count(suffix)

    def generate_sentence(self):
        # Start with a random initial prefix
        current_prefix = random.choice(list(self.transitions.keys()))
        sentence = list(current_prefix)

        # Generate the rest of the sentence based on transition probabilities
        while not self._is_sentence_complete(sentence):
            suffix_dist = self.transitions.get(current_prefix, None)
            if suffix_dist is None:
                break
            next_state = suffix_dist.sample()
            sentence.append(next_state)
            current_prefix = tuple(sentence[-self.order:])

        return ' '.join(sentence)

    def predict_next_state(self, current_state):
        prefix = tuple(current_state[-self.order:])
        suffix_dist = self.transitions.get(prefix, None)
        if suffix_dist is None:
            return None
        return suffix_dist.sample()

    def _generate_ngrams(self, data):
        ngrams = []
        for i in range(len(data) - self.order):
            ngram = [data[i + j] for j in range(self.order + 1)]
            ngrams.append(ngram)
        return ngrams

    @staticmethod
    def read_data_from_file(file_path):
        with open(file_path, 'r') as file:
            data = file.read().replace('\n', ' ')
        return data.split()

    def _is_sentence_complete(self, sentence):
        last_word = sentence[-1]
        return last_word.endswith(('.', '?', '!'))


def main():
    # Example usage of the MarkovChain class
    chain = MarkovChain(order=2)  # Use order=2 for a second-order Markov chain
    # Read text data from a file
    file_path = 'data/paragraph3.txt'  # Path to your input file
    data = MarkovChain.read_data_from_file(file_path)
    # Train the Markov chain with the input data
    chain.train(data)

    # Generate a new sentence
    generated_sentence = chain.generate_sentence()

    # Print the generated sentence
    print('Generated sentence:', generated_sentence)


if __name__ == '__main__':
    main()
