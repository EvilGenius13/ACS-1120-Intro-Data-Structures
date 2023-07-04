"""Main script, uses other modules to generate sentences."""
from flask import Flask, render_template, request
from generator_class import SentenceGenerator

app = Flask(__name__)
sg = SentenceGenerator('data/paragraph3.txt')

# TODO: Initialize your histogram, hash table, or markov chain here.
# Any code placed here will run only once, when the server starts.
@app.route("/")
def home():
    generated_sentence = sg.generate_random_sentence()

    return render_template("index.html", sentence=generated_sentence)


if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
