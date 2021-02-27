import telebot
import keyboards
import random

TOKEN = '1448680065:AAEu5ccC2iFME27LahCWJGhFDwK5tlft3mU'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'Представляю вам клавитуру для использования бота', reply_markup=keyboards.menu_btn)



@bot.message_handler(commands=['game'])
def check(message):
    a = random.choice(['Грустный','Веселый'])
    bot.send_message(message.chat.id, 'Я загадал какой-то смайл! Отгадывай!')
    if message.text.lower == 'Грустный':
        bot.send_message(message.chat.id, 'Угадал, это веселый смайл!')
    elif message.text.lower == 'Веселый':
        bot.send_message(message.chat.id, 'Угадал, это грустный смайл!')
    else:
        bot.send_message(message.chat.id, 'К сожалению, ты не угадал, попробуй снова!')

@bot.message_handler(commands=['math'])
def smile(message):
    while True:
        a = random.randint(10, 99)
        b = random.randint(10, 99)
        global result
        result = str(a + b)
        break
    bot.send_message(message.chat.id, f'Создал числа, сложи их {a} и {b}')

@bot.message_handler(content_types=['text'])
def check(message):
    if message.text == result:
        bot.send_message(message.chat.id, f'Ты был прав, ответ {result}')
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAALhB2A2a40_pT6Una7BVnBS8TZLjxduAAL7JAACns4LAAFO_D4FuKoVuB4E')
    else:
        bot.send_message(message.chat.id, 'Ты не угадал, попробуй снова')

bot.polling()



