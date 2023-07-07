import string
import random
from collections import defaultdict

class SentenceGenerator:
    def __init__(self, corpus_path, n=2):
        self.corpus_path = corpus_path
        self.corpus = ''
        self.ngrams = defaultdict(list)
        self.special_chars = set(string.punctuation) - set('.,?!')
        self.n = n
        self.max_sentence_length = 250
        self.min_sentence_length = 50

    def preprocess_corpus(self):
        with open(self.corpus_path, 'r', encoding='utf-8') as file:
            self.corpus = file.read()
        self.corpus = self.corpus.strip()
        self.corpus = ''.join(char for char in self.corpus if char not in self.special_chars)

    def generate_ngrams(self):
        tokens = self.corpus.split()
        for i in range(len(tokens) - self.n):
            ngram = tuple(tokens[i:i+self.n])
            next_token = tokens[i+self.n]
            self.ngrams[ngram].append(next_token)

    def find_starting_ngram(self):
        sentence_starting_candidates = []
        for ngram in self.ngrams:
            if ngram[0][0].isupper():
                sentence_starting_candidates.append(ngram)
        if not sentence_starting_candidates:
            return random.choice(list(self.ngrams.keys()))
        return random.choice(sentence_starting_candidates)

    def generate_sentence(self, starting_ngram):
        sentence = list(starting_ngram)
        while len(sentence) < self.max_sentence_length:
            current_ngram = tuple(sentence[-self.n:])
            next_token = random.choice(self.ngrams[current_ngram])
            sentence.append(next_token)
            if next_token.endswith(('.', '!', '?')):
                break
        generated_sentence = ' '.join(sentence)
        return generated_sentence

    def generate_random_sentence(self):
        self.preprocess_corpus()
        self.generate_ngrams()
        generated_sentence = ""
        while len(generated_sentence) < self.min_sentence_length or len(generated_sentence) > self.max_sentence_length:
            starting_ngram = self.find_starting_ngram()
            generated_sentence = self.generate_sentence(starting_ngram)
        return generated_sentence
