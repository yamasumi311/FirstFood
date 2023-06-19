from flask import Flask

from functions import read_food_from_file

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, Lucas!"

@app.route("/<baby_name>")
def get_name(baby_name):
    items = read_food_from_file(baby_name)
    return items

if __name__ == "__main__":
    app.run(debug=True)