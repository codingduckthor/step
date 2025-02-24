import asyncio
import logging
import random
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import Message

logging.basicConfig(level=logging.INFO)
bot = Bot(token='7202256517:AAG2Qljyt3nWP_7Av11IOSxqKCLVcdQ7jEk')
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_name(message: Message):
    await message.reply("День добрый, чтобы узнать доступные команды этого бота - используйте /help")

@dp.message(Command("help"))
async def cmd_name(message: Message):
    await message.reply("Доступные команды: \n/start \n/help \n/name \n/joke \n/stop")

@dp.message(Command("name"))
async def cmd_name(message: Message):
    args = message.text.split(maxsplit=1)
    if len(args) > 1:
        await message.answer(f"Здравствуй, <b>{args[1]}</b>", parse_mode="HTML")
    else:
        await message.answer("Чтобы бот знал ваше имя, напишите его после команды /name")

jokes = ["Что общего у любви и Wi-Fi? На расстоянии начинаются проблемы",
         "Мам, смотри, голубь! У тебя хлеб есть? Без хлеба ешь!",
         "Из студенческого общежития куда-то исчезли все кошки… Вот такие пироги!",
         "Аня вышла замуж за механика и родила шестерню",
         "Обожаю гулять по болотам! Очень затягивает"
]

@dp.message(Command("joke"))
async def send_joke(message: Message):
    joke = random.choice(jokes)
    await message.answer(joke)

@dp.message(Command("stop"))
async def cmd_name(message: Message):
    await message.reply("До свидания")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

