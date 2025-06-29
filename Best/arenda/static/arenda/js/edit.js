// Функции для редактирования записей
function showEditForm(id) {
    // Получаем кнопку и извлекаем данные из data-атрибутов
    const button = event.target; // Получаем элемент, на который был клик (кнопка)
    const title = button.getAttribute('data-title'); // Извлекаем значение атрибута data-title из кнопки
    const text = button.getAttribute('data-text'); // Извлекаем значение атрибута data-text из кнопки
    
    // Показываем форму
    document.getElementById('editForm' + id).style.display = 'block'; // Делаем форму редактирования видимой, изменяя CSS свойство display
    
    // Заполняем поля формы
    document.getElementById('title' + id).value = title; // Устанавливаем значение поля заголовка извлеченным title
    document.getElementById('text' + id).value = text; // Устанавливаем значение поля текста извлеченным text
}

function hideEditForm(id) {
    document.getElementById('editForm' + id).style.display = 'none'; // Скрываем форму редактирования, изменяя CSS свойство display на none
} 