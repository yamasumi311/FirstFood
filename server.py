import os

from flask import Flask, request

from functions import read_food_from_file, get_file_path, check_array_contains

app = Flask(__name__)


@app.route("/<baby_name>", methods=['POST', 'GET'])
def get_name(baby_name):
    items = read_food_from_file(baby_name)
    if request.method == 'POST':
        file_path = get_file_path(baby_name)
        new_food = request.get_data(as_text=True)
        with open(file_path, 'a') as file:
            if check_array_contains(new_food, items):
                file.write(new_food + '\n')
                return 'Hooray! New food added:)'
            else:
                return 'Already tried before'
    else:
        return items


if __name__ == "__main__":
    app.run(debug=True)
