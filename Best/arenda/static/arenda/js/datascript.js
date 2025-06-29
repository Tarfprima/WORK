fetch('/arenda/data_addr/')
.then(
    (response) => response.json() // Заколовки
)
.then(
    (data) => console.log(data) // Данные
)