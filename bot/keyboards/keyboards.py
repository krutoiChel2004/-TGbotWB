from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, 
                           InlineKeyboardMarkup, InlineKeyboardButton)

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Получить информацию по товару:")],
    [KeyboardButton(text="Остановить уведомления"),
     KeyboardButton(text="получить информацию из БД")]
], 
                        resize_keyboard=True,
                        input_field_placeholder="выберете пункт меню")           