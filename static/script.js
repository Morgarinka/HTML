document.getElementById('load-users').addEventListener('click', fetchUsers);

function fetchUsers() {
    // Используем API для получения списка пользователей
    fetch('https://jsonplaceholder.typicode.com/users')
        .then(response => {
            if (!response.ok) {
                throw new Error('Сеть сломалась: ' + response.status);
            }
            return response.json(); // Преобразуем ответ в JSON
        })
        .then(users => {
            updateUserList(users); // Обновляем список пользователей
        })
        .catch(error => console.error('Ошибка:', error)); // Обработка ошибок
}

function updateUserList(users) {
    const userList = document.getElementById('user-list'); // Получаем элемент списка
    userList.innerHTML = ''; // Очищаем предыдущий список

    users.forEach(user => {
        const li = document.createElement('li'); // Создаем новый элемент списка
        li.textContent = `${user.name} (${user.email})`; // Устанавливаем текст с именем и email пользователя
        userList.appendChild(li); // Добавляем элемент списка в ul
    });
}


var myImage = document.querySelector("img");

myImage.onclick = function () {
    var mySrc = myImage.getAttribute("src");
    if (mySrc === "images/firefox-icon.png") {
        myImage.setAttribute("src", "images/firefox2.png");
    } else {
        myImage.setAttribute("src", "images/firefox-icon.png");
    }
};


// document.querySelector("html").onclick = function () {
//     alert ("Ouch! Stop poking me!");
// };
