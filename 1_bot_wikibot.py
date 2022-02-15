import logging
import wikipedia
import wikipedia
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5246828331:AAG999JIXHdd2CYEyso4ImDpUvLr9ClgJCQ'

wikipedia.set_lang('uz')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Assalomu allaykum!\nWikipediya botman Xo'sh keldingiz!\nSizga kerakli ma'lumotni kiritishingiz mumkin.")



@dp.message_handler()
async def sendWiki(message: types.Message):
    try:
        respons = wikipedia.summary(message.text)
        await message.answer(respons)

    except:
        await message.answer("Bu mavzuga oid maqola topilmadi.")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
