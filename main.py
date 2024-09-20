from flask import Flask, render_template, request, jsonify
from pythainlp import word_tokenize
import os

app = Flask(__name__)

def is_thai(char):
    return ord('\u0E00') <= ord(char) <= ord('\u0E7F')

def split_mixed_sentence(sentence):
    words = []
    current_word = ""
    is_current_thai = False

    for char in sentence:
        if char.isspace():
            if current_word:
                words.append(current_word)
                current_word = ""
            words.append(char)
            is_current_thai = False
        elif is_thai(char):
            if current_word and not is_current_thai:
                words.append(current_word)
                current_word = ""
            current_word += char
            is_current_thai = True
        else:
            if current_word and is_current_thai:
                words.extend(word_tokenize(current_word))
                current_word = ""
            current_word += char
            is_current_thai = False

    if current_word:
        if is_current_thai:
            words.extend(word_tokenize(current_word))
        else:
            words.append(current_word)

    return words

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/split", methods=["POST"])
def split_sentence():
    data = request.json
    sentence = data.get("sentence", "")
    words = split_mixed_sentence(sentence)
    return jsonify({"words": words})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
