from flask import Flask, jsonify
from flask import render_template, redirect


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("resume.html")


@app.route('/data')
def names():
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
