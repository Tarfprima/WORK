import asyncio       # библиотека для работы с асинхронными (параллельными) функциями
from aiogram import Bot, Dispatcher  # библиотека для бота: класс бота и класс диспетчера (управляющий класс)
from aiogram.filters import Command
from secret import TOKEN  # Секретный файл, полученный вами в переписке с бот-прародителем
dp = Dispatcher()         # Создание управляющего объекта.
bot = Bot(token=TOKEN)    # Создается объект бота с нашим паролем. Один бот - один экземпляр на токен.
# Команду в бот необходимо вводить так: /start
@dp.message(Command("start"))
async def command_start_handler(message):
    print('Ура! Мне написал', message.chat.id)
    await message.answer(
        "Я веду канал космических событий! https://t.me/2317248832/1") 
#asyncio.run(           # Запуск асинхронной функции
#    dp.start_polling(  # диспетчер начинает обмен сообщениями, 
#        bot))          # используя бот

asyncio.run(
    bot.send_message(
        79023938, #chat_id,
        "Привет!"))

# "работа" его - ничего не делать, только ожидать сообщения
