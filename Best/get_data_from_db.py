# Написать себе напоминание. Вы отправляете боту команду /writeme 2025-07-08 21:42 он должен вам в это время сказать "Ты просил тебя разбудить в ..."
#1. Использовать чтение текста сообщения message.text и захватить из него дату и время
#2. Вычислить, сколько необходимо подождать
#3. Запустить асинхронное выжидание
#4. По истечении времени выжидания отправить сообщение о побудке

import asyncio       # библиотека для работы с асинхронными (параллельными) функциями
from aiogram import Dispatcher  # библиотека для бота: класс бота и класс диспетчера (управляющий класс)
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
    result = ''
    for b in Arenda.objects.all():
        result += f" \n --------------- ПОЛЬЗОВАТЕЛЬ  \n *{b.user}* \n --------------- ДАТА ПУБЛИКАЦИИ  \n *{b.dt}* \n --------------- ПОСТ  \n _{b.title}_ \n \n --------------- СЛЕДУЮЩИЙ ПОСТ  \n \n "
    return result


from Best.settings import BOT  # объект бота 
dp = Dispatcher()         # Создание управляющего объекта.


# Команду в бот необходимо вводить так: /arenda
@dp.message(Command("arenda"))
async def command_start_handler(message):
    print('Ура! Мне написал', message.chat.id)
    print('Его фраза', message.text)
    arenda = await get_data()
    await message.answer(
        "Твои записи:\n" + arenda, parse_mode='Markdown')
    
asyncio.run(           # Запуск асинхронной функции
    dp.start_polling(  # диспетчер начинает обмен сообщениями, 
        BOT))          # используя бот
