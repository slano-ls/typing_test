import requests
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///typing_test.db'
db = SQLAlchemy(app)

class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    wpm = db.Column(db.Integer, nullable=False)
    errors = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        quote = request.form['quote']
        user_input = request.form['text']
        wpm, errors = calculate_wpm_and_errors(user_input, quote)
        result = Result(name=request.form['name'], wpm=wpm, errors=errors)
        db.session.add(result)
        db.session.commit()
        return render_template('results.html', wpm=wpm, errors=errors)
    else:
        quote = fetch_random_quote()
        return render_template('index.html', quote=quote)

@app.route('/results', methods=['GET', 'POST'])
def results():
    if request.method == 'POST':
        # Handle the form submission
        return "Results submitted successfully"  # Placeholder response
    else:
        return render_template('results.html')

def fetch_random_quote():
    response = requests.get('https://api.quotable.io/random')
    if response.status_code == 200:
        quote = response.json().get('content')
        return quote
    return None

def calculate_wpm_and_errors(user_input, quote):
    words_typed = len(user_input.split())
    characters_typed = len(user_input)
    time_minutes = 1.0  # Assuming it took 1 minute
    wpm = int(words_typed / time_minutes)
    errors = count_errors(user_input, quote)
    return wpm, errors


def count_errors(user_input, quote):
    errors = 0
    for i in range(min(len(user_input), len(quote))):
        if user_input[i] != quote[i]:
            errors += 1
    errors += abs(len(user_input) - len(quote))
    return errors

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
