"use strict";

function read(baby_name) {
    return fetch('/baby/' + baby_name)
        .then(function (response) {
            return response.json()
        })
        .then(function (foods) {
            const total_count = turn_json_object_to_html(baby_name, foods)
            return total_count
        })
}

function read_baby_name_file(event) {
    event.preventDefault();
    const baby_name = event.target.elements.baby_name.value
    read(baby_name).then(function (total_count) {
        register_adding_new_food(baby_name)
        const headerCollection = document.getElementsByClassName('baby_name')
        for (let i = 0; i < headerCollection.length; i++) {
            const header = headerCollection[i]
            header.classList.remove('hidden')
            header.querySelector('h1').textContent = baby_name
        }
        document.getElementById('form_baby_name').classList.add('hidden')
        const total = document.getElementById('total')
        total.classList.remove('hidden')
        total.textContent = baby_name + " has tried " + total_count + " foods !"
    })
}


document.getElementById('form_baby_name')
    .addEventListener('submit', read_baby_name_file)

function register_adding_new_food(baby_name) {
    document.getElementById('form_new_food').classList.remove('hidden')

    function add_new_food(event) {
        event.preventDefault();
        const new_food = event.target.elements.new_food.value
        const category = event.target.elements.category.value
        const body = {
            category: category,
            food: new_food
        }
        // fetch(URL, options)
        fetch('/baby/' + baby_name, {
            method: 'POST',
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(body)
        })
            .then(function (response) {
                return response.text()
            })
            .then(function (p) {
                console.log(p)
                read(baby_name)
            })
    }

    document.getElementById('form_new_food')
        .addEventListener('submit', add_new_food)
}



function turn_json_object_to_html(baby_name, categories) {
    const category_names = Object.keys(categories)
    const root = document.getElementById("list")
    root.innerHTML = ''
    let total_food = 0
    for (let i = 0; i < category_names.length; i++) {
        const category = category_names[i]
        const foods = categories[category]
        const number_food = foods.length
        total_food = total_food + number_food
        const button_element = create_button_element(category, number_food)
        const div_element = create_div_element()
        const ul = div_element.querySelector("ul")
        root.appendChild(button_element)
        root.appendChild(div_element)
        for (let j = 0; j < foods.length; j++) {
            const food = foods[j]
            const f = create_food_element(food)
            const d = create_delete_button(baby_name, food, category)
            ul.appendChild(f)
            f.appendChild(d)
        }
    }
    toggle_class_collapsed()
    return total_food
}

function create_food_element(food_name) {
    const food = document.createElement("li")
    food.textContent = food_name
    return food
}

function create_button_element(category_name, number_food) {
    const button = document.createElement("button")
    button.setAttribute("type", "button")
    button.classList.add("collapsible")
    button.textContent = category_name
    const number_types = document.createElement("span")
    number_types.classList.add("number_food")
    number_types.textContent = number_food + "types"
    button.appendChild(number_types)
    return button
}

function create_div_element() {
    const div = document.createElement("div")
    div.classList.add("foods")
    const ul = document.createElement("ul")
    div.appendChild(ul)
    return div
}

function toggle_class_collapsed() {
    const coll = document.getElementsByClassName("collapsible");

    for (let i = 0; i < coll.length; i++) {
        coll[i].addEventListener("click", function () {
            const button = this
            const foods = button.nextElementSibling;
            if (button.classList.contains("collapsed")) {
                button.classList.remove("collapsed")
                foods.classList.remove("collapsed")

            } else {
                button.classList.add("collapsed")
                foods.classList.add("collapsed")
            }
        })
    }
}

function create_delete_button(baby_name, selected_food, category) {
    const delete_button = document.createElement("button")
    delete_button.setAttribute("type", "button")
    delete_button.classList.add("delete_button")
    delete_button.textContent = "x"
    const body = {
        category: category,
        food: selected_food
    }
    delete_button.addEventListener("click", function () {
        fetch('/baby/' + baby_name, {
            method: 'DELETE',
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(body)
        })
            .then(function (response) {
                return response.text()
            })
            .then(function () {
                read(baby_name)
            })
    })
    return delete_button
}
