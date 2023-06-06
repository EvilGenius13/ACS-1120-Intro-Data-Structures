from histogram import create_word_histogram
import random
import sys

# RUNNING: python3 stochastic.py <file_name> <smoothing_constant>
# Check for file path
if len(sys.argv) > 1:
    file_name = sys.argv[1]
    file_path = f'data/{file_name}.txt'
else:
    file_path = 'data/paragraph.txt'

histogram = create_word_histogram(file_path)

# Check for smoothing constant
smoothing_constant = 0.0  # Default value
if len(sys.argv) > 2:
    try:
        smoothing_constant = float(sys.argv[2])
    except ValueError:
        print("Invalid smoothing constant. Defaulting to 0.0.")

word_probability = {}

# Calculate probability with Laplace smoothing
total_words = sum(histogram.values())
vocabulary_size = len(histogram.keys())
for word, count in histogram.items():
    word_probability[word] = (count + smoothing_constant) / (total_words + (smoothing_constant * vocabulary_size))

random_word = random.choice(list(histogram.keys()))
print(f'Random word: {random_word}')
print(f'Probability: {word_probability[random_word]}')