import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tg_rewinder.settings")
django.setup()
from aiogram import Bot, Dispatcher, executor, types
import threading
from queue import Queue
import time
from weather import weather_app
from news import news_app
from bot_web_app.models import Message, User, BotCommand

TELEGRAM_TOKEN = "6369706682:AAFMpIgHpL3V3GbI5hRp8AUcczhZ6mxT4Sc"
WEATHER_TOKEN = "2c87759a08f90fd10c30d2935827efcd"

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)


def update_data(output_data):
    while True:
        print("updating")
        description = [BotCommand.objects.get(pk=1),
                       BotCommand.objects.get(pk=2),
                       BotCommand.objects.get(pk=3),
                       BotCommand.objects.get(pk=4),
                       ]
        output_data.put([[str(BotCommand.objects.get(pk=1)),
                         str(BotCommand.objects.get(pk=2)),
                         str(BotCommand.objects.get(pk=3)),
                         str(BotCommand.objects.get(pk=4))],
                        [
                            description[0].description.replace("\\n", "\n"),
                            description[1].description.replace("\\n", "\n"),
                            description[2].description,
                            description[3].description,
                        ]]
                        )
        time.sleep(1)


def process_data(input_data):
    print(input_data.get())
    print(q.get())
    while True:
        @dp.message_handler(commands=[q.get()[0][0]])
        async def start(message: types.Message):
            your_id = message.from_id
            your_name = message.from_user.username
            Message.objects.add
            await message.answer(f"Привет, {your_name}!" + q.get()[1][0])

        @dp.message_handler(commands=[q.get()[0][1]])
        async def help_cmd(message: types.Message):
            await message.answer(q.get()[1][1])

        @dp.message_handler(commands=[q.get()[0][2]])
        @dp.edited_message_handler(lambda message: message.text and q.get()[2] in message.text.lower())
        async def weather(message: types.Message):
            if len(message.text.split()) == 1:
                await message.answer("Вы не ввели названия города")
            city = message.text.split()[1].capitalize()
            weather_data = weather_app(token=WEATHER_TOKEN, chosen_city=city)
            await message.answer(weather_data)

        @dp.message_handler(commands=[q.get()[0][3]])
        async def news(message: types.Message):
            news_data = news_app()
            await message.answer(news_data)

        data = input_data.get()
        print(data)
        time.sleep(1)  # Задержка


q = Queue()
thread_update = threading.Thread(target=update_data, args=(q,), daemon=True)
thread_process = threading.Thread(target=process_data, args=(q,), daemon=True)

thread_update.start()
thread_process.start()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
