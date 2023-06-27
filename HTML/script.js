function read(baby_name) {
    return fetch('/baby/' + baby_name)
        .then(function (response) {
            return response.json()
        })
        .then(function (foods) {
            const ul = document.getElementById('food')
            ul.innerHTML = ''
            for (let index = 0; index < foods.length; index++) {
                const food = foods[index];
                const li = document.createElement('li')
                li.textContent = food
                ul.appendChild(li)
            }
        })
}

function read_baby_name_file(event) {
    event.preventDefault();
    const baby_name = event.target.elements.baby_name.value
    read(baby_name).then(function () {
        register_adding_new_food(baby_name)
        const header = document.getElementById('baby_name')
        header.classList.remove('hidden')
        header.querySelector('h1').textContent = baby_name
        document.getElementById('form_baby_name').classList.add('hidden')
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

const categories = {
    "Dairy": [
        "yogurt"
    ],
    "Fruits": [
        "apple",
        "banana",
        "Mandarine"
    ],
    "Grains/Roots": [
        "rice"
    ],
    "Legumes": [],
    "Meat/Fish/Eggs": [],
    "Natural Seasonings": [],
    "Seeds/Nuts": [],
    "Vegetables": []
}

function turn_json_object_to_html(categories) {
    const category_names = Object.keys(categories)
    const root = document.getElementById("list")
    for (let i = 0; i < category_names.length; i++) {
        const category = category_names[i]
        const foods = categories[category]
        const button_element = create_button_element(category)
        const div_element = create_div_element()
        const ul = div_element.querySelector("ul")
        root.appendChild(button_element)
        root.appendChild(div_element)
        for (let j = 0; j < foods.length; j++) {
            const food = foods[j]
            const f = create_food_element(food)
            ul.appendChild(f)
        }
    }
}

function create_food_element(food_name) {
    const food = document.createElement("li")
    food.textContent = food_name
    return food
}

function create_button_element(category_name) {
    const button = document.createElement("button")
    button.setAttribute("type", "button")
    button.classList.add("collapsible")
    button.textContent = category_name
    return button
}

function create_div_element() {
    const div = document.createElement("div")
    div.classList.add("foods")
    const ul = document.createElement("ul")
    div.appendChild(ul)
    return div
}

turn_json_object_to_html(categories)