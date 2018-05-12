from flask import Flask, jsonify
from flask import render_template, redirect, request


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("resume.html")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
	print request.form.get('name')
	return redirect('/')

@app.route('/data')
def names():
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
