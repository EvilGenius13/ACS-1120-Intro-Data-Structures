import re
from collections import defaultdict
import random


class MarkovGenerator:
    def __init__(self, order=1):
        self.order = order
        self.start_words = []
        self.word_chain = defaultdict(list)

    def read_file(self, file_name):
        with open(file_name) as f:
            text = f.read()
            words = re.findall(r"[a-zA-Z_.',:-;!?]+", text)
        return words

    def generate_chain(self, source_text):
        for i in range(len(source_text) - self.order):
            word_tuple = tuple(source_text[i : i + self.order])
            next_word = source_text[i + self.order]
            if i == 0:
                self.start_words.append(word_tuple)
            self.word_chain[word_tuple].append(next_word)

    def generate_sentence(self, number=1):
        sentences = []
        for _ in range(number):
            current_word = random.choice(self.start_words)
            sentence = list(current_word)
            while current_word in self.word_chain:
                next_word = random.choice(self.word_chain[current_word])
                sentence.append(next_word)
                current_word = tuple(sentence[-self.order:])
                if sentence[-1][-1] in [".", "!", "?"]:
                    break
            sentence = " ".join(sentence)
            sentences.append(sentence)
        return sentences


if __name__ == "__main__":
    # Create an instance of MarkovGenerator
    generator = MarkovGenerator(order=2, smoothing=0.1)

    # Read the source text from the file
    file_name = "./data/twilight.txt"
    source_text = generator.read_file(file_name)

    # Train the generator with the source text
    generator.train(source_text)

    # Generate a random sentence
    sentence = generator.generate_markov(sentence_number=1, min_length=50, max_length=250)
    print(sentence)