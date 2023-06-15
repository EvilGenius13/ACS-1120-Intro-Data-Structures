"""Main script, uses other modules to generate sentences."""
from flask import Flask, render_template, request
from markov import MarkovChain
import random

app = Flask(__name__)

# TODO: Initialize your histogram, hash table, or markov chain here.
# Any code placed here will run only once, when the server starts.
@app.route("/")
def home():
    chain = MarkovChain(order=2)  # Use order=2 for a second-order Markov chain
    # Read text data from a file
    file_path = 'data/paragraph3.txt'
    data = MarkovChain.read_data_from_file(file_path)
    # Train the Markov chain with the input data
    chain.train(data)

    # Generate a new sentence
    generated_sentence = chain.generate_sentence()

    return render_template("index.html", sentence=generated_sentence)


if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
