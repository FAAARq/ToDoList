document.addEventListener('click', function (e) {
    const picker = e.target.closest('.color-picker');
    if (!picker) return;

    e.preventDefault();

    const task = picker.closest('.task');
    const color = picker.dataset.color;
    const taskId = task.id.replace('task-', ''); // получаем ID задачи

    // Меняем цвет визуально
    task.classList.remove('task-blue', 'task-red', 'task-yellow', 'task-green', 'task-purple', 'task-orange');
    if (color !== 'task-default') {
        task.classList.add(color);
    }

    // Отправляем на сервер
    fetch(`/task/${taskId}/set-color/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken'), // CSRF токен
        },
        body: JSON.stringify({ color: color })
    });
});

// Функция получения CSRF токена из куки
function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}