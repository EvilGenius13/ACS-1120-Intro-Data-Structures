from histogram import create_word_histogram
import random
import sys

# RUNNING :  python3 stochastic.py <file_name> (optional). Do not end with .txt
# Check for file path
if len(sys.argv) > 1:
    file_name = sys.argv[1]
    file_path = f'data/{file_name}.txt'
else:
    file_path = 'data/paragraph.txt'

histogram = create_word_histogram(file_path)
word_probability = {}

# Calculate probability (checked with fish.txt and is working)
total_words = sum(histogram.values())
for word, count in histogram.items():
    word_probability[word] = count / total_words

random_word = random.choice(list(histogram.keys()))
print(f'Random word: {random_word}')
print(f'Probability: {word_probability[random_word]}')

top_words = sorted(word_probability.items(), key=lambda x: x[1], reverse=True)[:10]
print('Top 10 words:')
for word, probability in top_words:
    print(f'Word: {word}, Probability: {probability}')