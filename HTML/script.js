fetch('/baby/Lucas')
    .then(function (response) {
        return response.json()
    })
    .then(function (foods) {
        console.log(foods)
        const ul = document.getElementById('food')
        for (let index = 0; index < foods.length; index++) {
            const food = foods[index];
            const li = document.createElement('li')
            li.textContent = food
            ul.appendChild(li)
        }
    })