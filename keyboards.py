from telebot import types

menu_btn = types.ReplyKeyboardMarkup()
btn_1 = types.KeyboardButton(text='/math')
btn_2 = types.KeyboardButton(text='/game')
menu_btn.add(btn_1, btn_2)


