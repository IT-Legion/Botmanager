from config.TOKENS import Token
from app.kbs import kb_footer,ikb
import logging,time
from aiogram import Bot, Dispatcher, executor, types

# Configure logging
logging.basicConfig(level=logging.INFO)
# Initialize bot and dispatcher
bot = Bot(token=Token.botkey)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    name = message.from_user.first_name
    if message.text == "/start":
        await message.answer(f"Здраствуйте,{name}!\n Я могу расказать о продуктах Альфа-Банка",reply_markup= kb_footer)
        await message.delete()
        time.sleep(1.5)
        await bot.send_message(message.from_user.id,"Что вас интересует?",reply_markup=ikb)
    elif message.text == '/help':
        await message.reply("1")

@dp.callback_query_handler()
async def callback_query_keyboard(callback_query: types.CallbackQuery):
    if callback_query.data == '1':
        await bot.send_message(chat_id=callback_query.from_user.id,text= '1')
    elif callback_query.data == '2':
        await bot.send_message(chat_id=callback_query.from_user.id,text= '2')






@dp.message_handler()
async def text(message: types.Message):
    text = message
    print(text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
