# Ben Siri 10-10-22
# Learn flask

from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
    from flask import render_template
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)