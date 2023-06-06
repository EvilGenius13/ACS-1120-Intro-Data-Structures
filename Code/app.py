"""Main script, uses other modules to generate sentences."""
from flask import Flask, render_template, request
from histogram import create_word_histogram
import random

app = Flask(__name__)

# TODO: Initialize your histogram, hash table, or markov chain here.
# Any code placed here will run only once, when the server starts.
file_path = 'data/paragraph.txt'
histogram = create_word_histogram(file_path)

@app.route("/")
def home():
    word_probability = {}

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
    return render_template("index.html", random_word=random_word, probability=word_probability[random_word], top_words=top_words)


if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
