from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def fetch_random_quote():
    response = requests.get('https://api.quotable.io/random')
    if response.status_code == 200:
        quote = response.json().get('content')
        return quote
    else:
        print('Failed to obtain quote - HTTP Error:', response.status_code)
    return None

@app.route('/')
def index():
    quote = fetch_random_quote()
    if quote:
        return render_template('index.html', quote=quote)
    else:
        return 'Failed to fetch a quote. Please try again later.'

@app.route('/results', methods=['POST'])
def results():
    typed_text = request.form.get('text', '').strip()
    quote = fetch_random_quote()
    if typed_text and quote:
        # Perform typing speed and accuracy calculations
        # Send results to the server (optional)
        return render_template('index.html', quote=quote)
    else:
        return 'Failed to fetch a quote. Please try again later.'

if __name__ == '__main__':
    app.run(debug=True)

