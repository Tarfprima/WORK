from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainpage.urls')),    # новые маршруты логина/регистрации (путь)
    path('arenda/', include('arenda.urls')), # Путь для открытия feed.html теперь выглядит вот так: "http://127.0.0.1:8000/arenda/1/" в глобальном urls пишется: 'arenda/' а в urls приложения пишется: '1/'.
    
]
