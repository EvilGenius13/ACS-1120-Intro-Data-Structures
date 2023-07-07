from typing import List, Tuple
import random



class Dictogram(dict):
    """
    Dictogram is a histogram implemented as a subclass of the dict type.
    """

    def __init__(self, word_list: List[str] = None, order: int = 1) -> None:
        """
        Initialize this histogram as a new dict and count given words.
        """
        super().__init__()
        self.order = order
        self.types = 0  # Count of distinct word types in this histogram
        self.tokens = 0  # Total count of all word tokens in this histogram
        if word_list is not None:
            for index in range(len(word_list)):
                self.increment_word_count(tuple(word_list[index: index + order]))
                if index + order <= len(word_list) - order:
                    self.increment_next_word_count(
                        tuple(word_list[index: index + order]),
                        tuple(word_list[index + 1: index + order + 1]),
                    )

    def increment_word_count(self, word_tuple: Tuple[str], count: int = 1) -> None:
        """Increase frequency count of given word by given count amount."""
        if word_tuple in self:
            self[word_tuple]["count"] += count
        else:
            self[word_tuple] = {"count": count, "next": {}}
            self.types += 1
        self.tokens += count

    def increment_next_word_count(
        self, word_tuple: Tuple[str], next_tuple: Tuple[str]
    ) -> None:
        if next_tuple in self[word_tuple]["next"]:
            self[word_tuple]["next"][next_tuple] += 1
        else:
            self[word_tuple]["next"][next_tuple] = 1

    def frequency(self, word_tuple: Tuple[str]) -> int:
        """Return frequency count of given word, or 0 if word is not found."""
        return self.get(word_tuple, {"count": 0})["count"]

    def sample_start(self) -> Tuple[str]:
        """Return a word from this histogram, randomly sampled by weighting
        each word's probability of being chosen by its observed frequency."""
        start_histogram = {}
        start_tokens = 0
        for word_tuple in self:
            if word_tuple[-1][-1] in [".", "!", "?"]:
                next_tuples = self[word_tuple]["next"]
                for next_tuple in next_tuples:
                    if next_tuple in start_histogram:
                        start_histogram[next_tuple] += next_tuples[next_tuple]
                    else:
                        start_histogram[next_tuple] = next_tuples[next_tuple]
                    start_tokens += next_tuples[next_tuple]

        return random.choices(list(start_histogram.keys()), weights=list(start_histogram.values()), k=1)[0]

    def sample_next(self, word_tuple: Tuple[str]) -> Tuple[str]:
        next_tuples = self[word_tuple]["next"]

        # Get top 3 most frequent next words
        top_next_words = sorted(next_tuples.items(), key=lambda x: x[1], reverse=True)[:3]
        words, weights = zip(*top_next_words)

        # Sample next word from the top 3
        return random.choices(words, weights=weights, k=1)[0]