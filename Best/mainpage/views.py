from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from .forms import UserRegistrationForm

def home(request):
    """
    Главная страница: простой текст и ссылки на вход/регистрацию (если не залогинен),
    либо ссылка на профиль (если уже авторизован).
    """
    return render(request, 'mainpage/home.html')


def register(request):
    """
    Регистрация нового пользователя. 
    — если POST и форма валидна, создаём User, делаем set_password(), логиним и редиректим на /profile/.
    — иначе просто рендерим форму.
    """
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # создаём объект пользователя, но пока не сохраняем в БД
            new_user = form.save(commit=False)
            # хешируем пароль
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            # сразу логиним его
            auth.login(request, new_user)
            # после регистрации сразу находимся на странице профиля
            return redirect('profile')
    else:
        form = UserRegistrationForm()
    return render(request, 'user/register.html', {'form': form})


@login_required
def profile(request):
    """
    Страница «мой профиль» — доступна только залогиненным ( с @login_required). 
    Просто страница с приветствием и ссылками «Главная» и «Выйти».
    """
    return render(request, 'mainpage/profile.html')
