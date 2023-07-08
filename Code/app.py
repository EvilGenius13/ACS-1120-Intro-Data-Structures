from flask import Flask, render_template
from base_generator import MarkovGenerator

app = Flask(__name__)

generator_twilight = MarkovGenerator(order=3)
text_twilight = generator_twilight.read_file("data/twilight_fixed.txt")

generator_warcraft = MarkovGenerator(order=3)
text_warcraft = generator_warcraft.read_file("data/warcraft.txt")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/warcraft")
def warcraft():
    print("Inside the warcraft() route")
    try:
        generated_sentence = generator_warcraft.generate_markov(text_warcraft, 3)
        match_percentage = generator_warcraft.check_sentence_match(generated_sentence, "data/warcraft.txt")
        print("Generated sentence:", generated_sentence)
        print("Match percentage:", match_percentage)
        return render_template("warcraft.html", sentence=generated_sentence, match_percentage=match_percentage)
    except Exception as e:
        error_message = "Failed to generate a sentence: " + str(e)
        print(error_message)
        return render_template("error.html", error=error_message)
    
@app.route("/twilight")
def twilight():
    print("Inside the twilight() route")
    try:
        generated_sentence = generator_twilight.generate_markov(text_twilight, 3)
        match_percentage = generator_twilight.check_sentence_match(generated_sentence, "data/twilight.txt")
        print("Generated sentence:", generated_sentence)
        print("Match percentage:", match_percentage)
        return render_template("twilight.html", sentence=generated_sentence, match_percentage=match_percentage)
    except Exception as e:
        error_message = "Failed to generate a sentence: " + str(e)
        print(error_message)
        return render_template("error.html", error=error_message)


if __name__ == "__main__":
    app.run(debug=True)