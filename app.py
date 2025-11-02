from flask import Flask, render_template, jsonify
from generator_logic import *

app = Flask(__name__)

@app.route('/')
def home():
    board = structure_board(generate_board())
    return render_template("index.html", board=board)

@app.route('/api/shuffle')
def shuffle():
    board = structure_board(generate_board())
    return jsonify(board)

if __name__ == '__main__':
    app.run(debug=True)
