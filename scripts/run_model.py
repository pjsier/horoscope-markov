import sys

import markovify


if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        corpus = f.read()

    text_model = markovify.Text(corpus)
    for i in range(5):
        print(text_model.make_sentence())
