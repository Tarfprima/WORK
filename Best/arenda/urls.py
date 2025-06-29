# Это urls.py для приложения, а есть urls.py глобальный, который находится в файле Best, необходимо чтобы путь из глобального urls.py ввель в путь urls.py из приложения.
from django.urls import path
from . import views # Импорт содержимого файла views.py т.е получения доступа к содержимому файла.
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Путь к страницам
    #     "Ссылка",  "views.py",  "функция", "имя ссылки для работы с url".
    
    path('<int:uid>/',  views.posts,    name='blogpost'), # "posts" это название функции в "views.py" а "views" это название файла где написана функция "posts". т.е идет обрашения к пути. (связано с feed.html). "uid" - это переменная.
    path('glav/',       views.tmain,    name='arenda'), # "tmain" это название функции в "views.py" а "views" это название файла где написана функция "tmain". т.е идет обрашения к пути. (связано с main.html). "name='arenda'" - связан с "<a href="{% url 'arenda' %}">Главная</a>" из menu.html. 
    path('new/',        views.publish,  name='save_arendas'),
    path(
        'login/', # путь в браузере 
        auth_views.LoginView.as_view( # django login
            template_name='arenda/login.html'), # шаблон
        name='arenda_login'), # {% url name %} - 
    
    path('logout/',     auth_views.LogoutView.as_view(next_page='/'), name='logout'), 
    path('register/',   views.register, name='new_register'),
    path('schedule/',   views.calendar, name='new_calendar'), # для изучения записи 
    path('data_addr/',  views.data_function), # для изучения feth
    path('data_page/', views.data_page_rendering), # для изучения feth
    path('book_appointment/', views.book_appointment, name='book_appointment'), # запись на прием
    
]