# Написать себе напоминание. Вы отправляете боту команду /writeme 2025-07-08 21:42 он должен вам в это время сказать "Ты просил тебя разбудить в ..."
#1. Использовать чтение текста сообщения message.text и захватить из него дату и время
#2. Вычислить, сколько необходимо подождать
#3. Запустить асинхронное выжидание
#4. По истечении времени выжидания отправить сообщение о побудке

import asyncio       # библиотека для работы с асинхронными (параллельными) функциями
from aiogram import Bot, Dispatcher  # библиотека для бота: класс бота и класс диспетчера (управляющий класс)
from aiogram.filters import Command

# Django settings
import os
os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'Best.settings')
import django
django.setup()

from arenda.models import Arenda

from asgiref.sync import sync_to_async
@sync_to_async
def get_data():
    return list(Arenda.objects.all())

from secret import TOKEN  # Секретный файл, полученный вами в переписке с бот-прародителем
dp = Dispatcher()         # Создание управляющего объекта.
bot = Bot(token=TOKEN)    # Создается объект бота с нашим паролем. Один бот - один экземпляр на токен.
# Команду в бот необходимо вводить так: /start
@dp.message(Command("start")) 
async def command_start_handler(message):
    print('Ура! Мне написал', message.chat.id)
    print('Его фраза', message.text)
    data = await get_data()
    print(data)
    await message.answer(
        "Ты написал:" + message.text)
asyncio.run(           # Запуск асинхронной функции
    dp.start_polling(  # диспетчер начинает обмен сообщениями, 
        bot))          # используя бот

# "работа" его - ничего не делать, только ожидать сообщения
