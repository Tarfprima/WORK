from django.shortcuts import render, redirect
from . import models # Нужно обратится к базе данных чтобы вывести в feed.html записи добавленные через админку. Чтобы обратиться к базе данных используем "модели" что-бы обратиться к моделям из них надо испортировать наш код. 
from datetime import datetime, timedelta # для работы с фильтрами и не только
from . import forms # импортируем forms.py
from django.contrib.auth.decorators import login_required # будем требовать логин для публикации
from django.http import JsonResponse

def posts(request, **kwargs): # Функция для рендера шаблона т.е размещения информации на странице.
    my_posts = models.Arenda.objects.filter( 
        # Все это свойство объекта. Логические методы
        # Вместо "all" используем фильтр если хотим использовать фильтрацию.
        # это функция для фильтрации постов добавленных через админку.
        # __gt - это "greater than" как знак ">" т.е больше.
        # __lt - это "less than" как знак "<" т.е меньше.
        # __gte - это "greater than or equal" как знак ">=" т.е больше или равно. 
        # __lte - это "less than or equal to" как знак "<=" т.е меньше или равно. 
        # Можно сравнивать дни или года и т.д отдельно, например:
        
        # dt__day__gt=19 - т.е больше 19 числа дня.
        
        # user=1 # записи только пользователя под номером 1

        # dt__gt=datetime(2025,6,11) # "dt" - это название переменной для datetime из "models.py". "__gt" - это знак больше. После идет знак равенства и datetime с указанием времени. На сайте отобразятся посты добавленные после 11 июня. 
    
        user=kwargs['uid'] # request.GET.get('uid') # Если перейти по этой ссылке: "http://127.0.0.1:8000/arenda/1/?uid=2" появится пост добавленный созданным мной юзером "Arthur" а посты добавленные Админом видны не будут.
    
    ) 
    
    context = {
            'author': 'Я', # {{author}} из шаблона "<h1>Все записи {{author}}</h1> "
            'uid': str(kwargs['uid']), # request.GET.get('uid'),
            'all_posts': my_posts
#           'all_posts': models.Arenda.objects.all() # {{all_posts}} из шаблона. "models" - это models.py | "Arenda" - это название класса из models.py | "objects" - это свойство django чтобы получить объекты | "all" - это выбрать все объекты arenda из базы данных. 
        }
    # Context обязателен. Туда прередаются ключи которые были добавлены в шаблоне "feed.html"
    return render( 
        request,
        'arenda/feed.html',
        context
    )

def tmain(request): # Для рендера страницы main.html и всех его шаблонов
    return render(
        request,
        'arenda/main.html',
    )

@login_required(login_url='/arenda/login/') # Это декоратор. Тут указан путь куда перенаправить пользователя если он не залогинен
def publish(request): # Для рендера страницы new.html и всех его шаблонов
    form = forms.BlogPostForm(request.POST) # форма создается из пост запроса, пустая или не пустая
    context = {
        'new_blog_post_form': form # контекст ее запоминает, больше не надо проверять есть у нас пост запрос или нет.
    }
    if request.method == 'POST':
        if form.is_valid():
            print(form.cleaned_data)
            new_arenda = form.save(commit=False)
            new_arenda.user = request.user
            new_arenda.save()
            return redirect('blogpost', uid=request.user.id)
    return render(
        request,
        'arenda/new.html', context) 
    


def register(request):
    user_form = forms.UserRegistrationForm(request.POST)
    if request.method == 'POST':
        if user_form.is_valid():
            new_user = user_form.save(commit=False)   # Создать, но в базу не записывать!
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()  
            auth.login(request, new_user)
            return redirect('/')
    return render(
        request,
        'arenda/register.html', {
            'form': user_form        
        }
    )


# КАЛЕНДАРЬ 
def calendar(request):
    dt = datetime.now()
    if 'dt' in request.GET:
        dt = datetime.strptime(
            request.GET['dt'],
            '%Y%m%d'
        )
    print(dt)
    return render(
        request,
        'arenda/timetable.html',
        timeslots(dt)
    )

def timeslots(dt, period = 7, daystart = 8, dayend = 18):
    result = []
    dt = datetime(
        dt.year, dt.month, dt.day
    )
    for i in range(period):
        # Прибавить к дате количество дней, равное i
        day = {
            'weekday': dt.strftime('%a'),
            'slots': []
        }
        for h in range(daystart, dayend + 1):
            dt_h = dt + timedelta(seconds = 3600 * h)
            day['slots'].append({
                'time': dt_h.strftime('%H:%M'),
                'dt':   dt_h.strftime('%Y%m%d%H%M'),
                'client': ''
            })
        result.append(day)
        # Создать словарь, хранящий день недели и 
        # Массив слотов, где каждый слот содержит
        #     время для отображения
        #     дату и время для записи
        #     клиента при наличии 
        dt += timedelta(1)  # timedelta(days=i)
    return {
        'days': result
    } 
    {
        'days': [
            {  # Описание одного дня в нашей неделе
                'weekday': 'ПН',
                'slots': [
                    {
                        'time': '8:00',
                         'client': ''
                    },
                    {
                        'time': '9:00',
                        'client': 'Wera'
                    },
                    {
                        'time': '10:00',
                        'client': ''
                    },
                    {
                        'time': '11:00',
                        'client': ''
                    }
                ]
            },
            {
                'weekday': 'ВТ',
                'slots': [
                    {
                        'time': '8:00',
                         'client': ''
                    },
                    {
                        'time': '9:00',
                        'client': ''
                    },
                    {
                        'time': '10:00',
                        'client': ''
                    },
                    {
                        'time': '11:00',
                        'client': ''
                    }
                ]
            },
            {
                'weekday': 'СР',
                'slots': [
                    {
                        'time': '8:00',
                         'client': ''
                    },
                    {
                        'time': '9:00',
                        'client': ''
                    },
                    {
                        'time': '10:00',
                        'client': ''
                    },
                    {
                        'time': '11:00',
                        'client': ''
                    }
                ]
            }
            ]
    }
    
def data_function(request):
    return JsonResponse({
        'param': 25
    })
    
def data_page_rendering(request):
    return render(
        request,
        'arenda/datapage.html'
    )
    
def book_appointment(request):
    if request.method == 'GET':
        dt = request.GET.get('dt')
        if dt and request.user.is_authenticated:
            try:
                return JsonResponse({'success': True, 'message': 'Запись создана'})
            except Exception as e:
                return JsonResponse({'success': False, 'error': str(e)})
        else:
            return JsonResponse({'success': False, 'error': 'Неверные параметры или пользователь не авторизован'})
    return JsonResponse({'success': False, 'error': 'Метод не поддерживается'})

