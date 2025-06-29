function make_appointment(event) {
    let li = event.currentTarget.parentElement;
    let dt = li.querySelector('[type=hidden]').value;
    
    fetch(`/arenda/book_appointment/?dt=${dt}`)
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('Запись успешно создана!');
            } else {
                alert('Ошибка при записи: ' + data.error);
            }
        })
        .catch(error => {
            console.error('Ошибка:', error);
            alert('Ошибка при записи на прием');
        });
}
