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
            words = [match.group() for match in re.finditer(r"[a-zA-Z_.',:-;!?]+", text)]
        return words

    def generate_beam(self, source_text: List[str], k: int = 5) -> str:
        """
        Generates a random sentence from the given text using BEAM search,
        regenerating the sentence if its length is less than 50 or more than 250 characters.
        """
        self.words_histogram.setdefault("filled", Dictogram(source_text, self.order))

        histogram = self.words_histogram["filled"]

        attempts = 0
        while attempts < 10:
            sentence_beams = [([histogram.sample_start()], 0)]  # Start the BEAMs

            while True:  # Generate until we reach a terminal punctuation or exceed the maximum character limit
                new_beams = []
                for sentence, score in sentence_beams:
                    next_words = list(histogram[sentence[-1]]["next"].keys())
                    next_words_freq = list(histogram[sentence[-1]]["next"].values())

                    next_word = random.choices(next_words, weights=next_words_freq, k=1)[0]

                    new_sentence = sentence + [next_word]
                    new_score = score + histogram.frequency(next_word)  # The frequency can be a basic score

                    # Check if the sentence has reached a terminal punctuation
                    sentence_str = " ".join(word_tuple[-1] for word_tuple in new_sentence)
                    if new_sentence[-1][-1][-1] in ".!?" or len(sentence_str) > 250:
                        if new_sentence[-1][-1][-1] in ".!?":
                            new_beams.append((new_sentence, new_score))
                        continue
                    else:
                        new_beams.append((new_sentence, new_score))

                # If we have not generated any new beams, then all sentences have reached a terminal punctuation or exceeded the maximum character limit
                if not new_beams:
                    break

                sentence_beams = sorted(new_beams, key=lambda x: x[1], reverse=True)[:k]

            sentence, _ = max(sentence_beams, key=lambda x: x[1])
            sentence = " ".join(word_tuple[-1] for word_tuple in sentence)

            if 50 <= len(sentence) <= 250:
                return sentence
            attempts += 1

        raise Exception("Failed to generate a sentence within the specified length range after 10 attempts.")





if __name__ == "__main__":
    generator = MarkovGenerator(order=2)
    text = generator.read_file("data/twilight.txt")
    try:
        print(generator.generate_beam(text, 3))
    except Exception as e:
        print(e)