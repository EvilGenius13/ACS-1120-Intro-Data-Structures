import random

quotes = ( "I'll tell you what I want, what I really, really want",
            "If you wanna be my lover, you gotta get with my friends",
            "Make it last forever, friendship never ends")


def random_python_quote():
    rand_index = random.randint(0, len(quotes) - 1)
    return quotes[rand_index]

if __name__ == '__main__':
    quote = random_python_quote()
    print(quote)

