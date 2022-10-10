# Ben Siri 10-10-22
# Learn flask

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello world!"


if __name__ == "__main__":
    app.run(debug=True)