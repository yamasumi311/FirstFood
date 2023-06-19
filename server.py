import os

from flask import Flask, request

from functions import read_food_from_file, get_file_path

app = Flask(__name__)


@app.route("/<baby_name>", methods=['POST', 'GET'])
def get_name(baby_name):
    if request.method == 'POST':
        file_path = get_file_path(baby_name)
        with open(file_path, 'a') as file:
            file.write(request.get_data(as_text=True) + '\n')
        return 'OK'
    else:
        items = read_food_from_file(baby_name)
        return items


if __name__ == "__main__":
    app.run(debug=True)
