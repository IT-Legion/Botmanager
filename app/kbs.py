from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton ,InlineKeyboardMarkup , InlineKeyboardButton

kb_footer = ReplyKeyboardMarkup(resize_keyboard=True)
rb1 = ('/info')
rb2 = ('/help')
kb_footer.add(rb2)





# создаем новую клавиатуру
ikb = InlineKeyboardMarkup(row_width=2 )
ib1 = InlineKeyboardButton(text="Кнапка 1" , callback_data='1')
ib2 = InlineKeyboardButton(text="Кнапка 2" , callback_data='2')
ikb.add(ib1,ib2)


