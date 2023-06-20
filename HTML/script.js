function read(baby_name) {
    fetch('/baby/' + baby_name)
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


document.getElementById('form')
    .addEventListener('submit', function (event) {
        event.preventDefault();
        const baby_name = event.target.elements.baby_name.value
        const new_food = event.target.elements.new_food.value
        fetch('/baby/' + baby_name, { method: 'POST', body: new_food })
            .then(function (response) {
                return response.text()
            })
            .then(function (p) {
                console.log(p)
                read(baby_name)
            })
    })