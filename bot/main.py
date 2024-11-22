from aiogram import Bot, Dispatcher, filters, types
import asyncio

bot = Bot(token='7638919419:AAG0EYZ0fcdTahTIcM-ZicpIKZQ1dfKYQug')
dp = Dispatcher(bot=bot)

@dp.message(filters.CommandStart())
async def start_bot(message: types.Message):
    await message.answer(text='Salom')

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())