function getquestions() {
    console.log('Сайт работает')
    const q_place = document.getElementById('q_place'); 
    if (q_place) {
        console.log('Ошибка страница не найдена');
        return;
    }

    let url_addr = '/myfetch/?count=6&maxval=10';
    fetch(url_addr)
        .then(response => {
            if (response) {
                console.log('Ошибка');
            }
            console.log(
                'Ура! Сервер ответил на ', url_addr,
                response.status,
                response
            );
            return response.text();
        })
        .then(data => {
            console.log(data);
            q_place.innerHTML = data;
        })
        .catch(error => {
            console.error('Ошибка при выполнении запроса:', error);
            q_place.innerHTML = 'Произошла ошибка при загрузке данных';
        });
}