from flask import Flask, request, render_template, send_from_directory

from categories import add_to_category, remove_from_category
from functions import read_categories_from_file, \
    write_categories_to_file

app = Flask(__name__, template_folder="HTML")


@app.route('/')
def home():
    return render_template('FirstFood.html')


@app.route('/script.js')
def script():
    return send_from_directory('HTML', 'script.js')


@app.route('/style.css')
def css():
    return send_from_directory('HTML', 'style.css')


@app.route("/baby/<baby_name>", methods=['POST', 'GET','DELETE'])
def get_name(baby_name):
    if not baby_name:
        return 'Baby name is required'
    c = read_categories_from_file(baby_name)
    if request.method == 'POST':
        body = request.get_json()
        new_food = body["food"]
        category = body["category"]
        add_to_category(category, new_food, c)
        write_categories_to_file(baby_name, c)
        return "added a food"
    elif request.method == 'DELETE':
        body = request.get_json()
        selected_food = body["food"]
        category = body["category"]
        remove_from_category(category, selected_food, c)
        write_categories_to_file(baby_name, c)
        return "deleted a food"
    else:
        return c


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
