from django.db import models
from django.contrib.auth.models import User # Возможность дабавить пользователя 
from datetime import datetime

class Arenda(models.Model): # класс в таблице обязательно должен наследовать класс 'Model'
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE) # Добавление пользователя и условия для удаления всех данных.
    title = models.CharField(max_length=64) # Текстовое поле (для CharField обязательно указать максимальную длину)
    text = models.CharField(max_length=10000) # Текстовое поле (поле можно поменять)
    dt = models.DateTimeField(default=datetime.now(), blank=True) # Поле даты
    
    def __str__(self):
        return self.title
    
