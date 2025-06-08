from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # ==== Главная страница ====
    path('', views.home, name='home'),

    # ==== Аутентификация ====
    # Страница логина: используем стандартный LoginView, шаблон 'user/login.html'
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    # Страница выхода: LogoutView сразу сделает logout и редирект на LOGOUT_REDIRECT_URL ('/')
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Страница регистрации: наша функция-обработчик register()
    path('register/', views.register, name='register'),

    # ==== Профиль пользователя ====
    # Переход на профиль после логина/регистрации
    path('profile/', views.profile, name='profile'),
    # ==== Домашняя работа ====
    path('myfetch/', views.myfetch, name='myfetch'),
    
]
