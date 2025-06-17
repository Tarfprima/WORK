from django.contrib import admin
from . import models # Импортируем все модели и файлы models

# models.НашКласс
@admin.register(models.Arenda) # Спомошью декоратора admin.register которому передается в качесве параметра наш класс 'Arenda' из файла models.py
class ArendaAdmin(admin.ModelAdmin): # Создается класс который будет отображать все что нужно в админке
    list_display = ['dt', 'title', 'user']