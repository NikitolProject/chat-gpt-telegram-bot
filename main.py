import logging

import aiohttp

from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

logging.basicConfig(level=logging.INFO)

bot = Bot(token="5843948724:AAFPlrFosqoEq77tr_0Pzh0I9twJpsM6JKk")

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message) -> None:
    """
    Process a command /start
    """
    await message.reply(
        "Привет! Я - ChatGPT, нейронная сеть, созданная с целью помогать людям. Если тебя что-то интересует - задавай свои вопросы."
    )


@dp.message_handler(lambda message: True)
async def process_all_messages(message: types.Message) -> None:
    """
    Process all messages
    """
    async with aiohttp.ClientSession() as session:
        async with session.post("https://chestnut-bustling-allspice.glitch.me/api/v1/question", json={'text': message.text}) as response:
            answer = (await response.json())['answer']
    await message.reply(answer)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
