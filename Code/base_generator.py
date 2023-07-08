from dictogram_attempt import Dictogram
from typing import List, Tuple
import re
import random

class MarkovGenerator:
    def __init__(self, order: int = 1) -> None:
        self.words_histogram = {}
        self.order = order

    def read_file(self, file_name: str) -> List[str]:
        """
        Reads given source file and returns list of words
        """
        with open(file_name) as f:
            text = f.read()
            text = text.replace("’", "'")
            text_without_numbers = re.sub(r"\d+", "", text)  # Remove all numbers from the text
            words = [match.group() for match in re.finditer(r"[a-zA-Z0-9_'.:,-;!?]+", text_without_numbers)]
        return words

    def prepare_histogram(self, file_name: str) -> None:
        """
        Reads given source file, creates a Dictogram and stores it in self.words_histogram
        """
        words = self.read_file(file_name)
        self.words_histogram["filled"] = Dictogram(words, self.order)
    
    def generate_markov(self, source_text: List[str], number: int = 1) -> str:
        """
        Generates a random sentence from the given text and word count number,
        regenerating the sentence if its length is less than 50 or more than 250 characters.
        """
        
        self.words_histogram.setdefault("filled", Dictogram(source_text, self.order))

        histogram = self.words_histogram["filled"]

        attempts = 0
        while attempts < 10:
            tuple_list = [histogram.sample_start()]
            sentence = " ".join(word_tuple[-1] for word_tuple in tuple_list)  # Start the sentence

            for _ in range(number):
                next_word = histogram.sample_next(tuple_list[-1])
                # Ensure that the sentence doesn't get too long
                if len(sentence) + len(next_word[-1]) + 1 > 250:
                    break
                tuple_list.append(next_word)
                while tuple_list[-1][-1][-1] not in [".", "!", "?"] and len(sentence) + len(next_word[-1]) + 1 <= 250:
                    next_word = histogram.sample_next(tuple_list[-1])
                    tuple_list.append(next_word)

            sentence = " ".join(word_tuple[-1] for word_tuple in tuple_list)

            if 50 <= len(sentence) <= 250:
                return sentence
            attempts += 1

        raise Exception("Failed to generate a sentence within the specified length range after 10 attempts.")
    
    def check_sentence_match(self, generated_sentence: str, file_name: str) -> None:
        """
        Checks if the generated sentence matches a sentence in the specified text file.
        Prints the percentage of the generated sentence that matches the source text.
        """
        with open(file_name) as f:
            text = f.read().replace('\n', ' ').lower() # Replace line breaks with spaces and convert to lowercase
            sentences = re.findall(r"[^.!?]+", text)

        longest_match_len = 0
        generated_sentence = generated_sentence.lower()

        for sentence in sentences:
            sentence = sentence.strip()
            if sentence in generated_sentence:
                longest_match_len = max(longest_match_len, len(sentence))

        matching_percentage = 100.0 * longest_match_len / len(generated_sentence)
        print(f'Matching percentage: {matching_percentage}%')
        return matching_percentage

if __name__ == "__main__":
    generator = MarkovGenerator(order=3)
    text = generator.read_file("data/twilight_fixed.txt")
    try:
        generated_sentence = generator.generate_markov(text, 3)
        print(generated_sentence)
        generator.check_sentence_match(generated_sentence, "data/twilight_fixed.txt")
    except Exception as e:
        print(e)