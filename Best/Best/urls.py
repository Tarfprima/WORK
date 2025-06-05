
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('mypage/', views.show,)
    path('', include('mainpage.urls')),    # новые маршруты логина/регистрации

]
