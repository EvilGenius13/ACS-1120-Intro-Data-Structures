from flask import Flask, render_template
from base_generator import MarkovGenerator

app = Flask(__name__)

generator_twilight = MarkovGenerator(order=3)
generator_twilight.prepare_histogram("data/twilight_fixed.txt")

generator_warcraft = MarkovGenerator(order=3)
generator_warcraft.prepare_histogram("data/warcraft.txt")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/warcraft")
def warcraft():
    print("Inside the warcraft() route")
    try:
        generated_sentence = generator_warcraft.generate_markov(3)
        print("Generated sentence:", generated_sentence)
        return render_template("warcraft.html", sentence=generated_sentence)
    except Exception as e:
        error_message = "Failed to generate a sentence: " + str(e)
        print(error_message)
        return render_template("error.html", error=error_message)
    
@app.route("/twilight")
def twilight():
    print("Inside the twilight() route")
    try:
        generated_sentence = generator_twilight.generate_markov(3)
        print("Generated sentence:", generated_sentence)
        return render_template("twilight.html", sentence=generated_sentence)
    except Exception as e:
        error_message = "Failed to generate a sentence: " + str(e)
        print(error_message)
        return render_template("error.html", error=error_message)



if __name__ == "__main__":
    # If running locally, use this:
    app.run(debug=True)
    # If using docker container, use this instead:
    # app.run(host='0.0.0.0', port=5000, debug=True)