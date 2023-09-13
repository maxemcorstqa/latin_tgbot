import telebot # Импортируем telebot
import random
import os
from telebot import types

token = ('')
bot = telebot.TeleBot(token)

f = open('latin.txt', 'r', encoding='UTF-8')
latin = f.read().split('\n')
f.close()

# хендлер и функция для обработки команды /start
@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    action_button = types.KeyboardButton("Новая пословица")
    markup.add(action_button)
    bot.send_message(message.chat.id, text="Привет, {0.first_name} 👋\nВоспользуйся кнопками".format(message.from_user), reply_markup=markup)

# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])

# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    # Если юзер прислал Новая пословица, выдаем ему случайную строку
    if message.text.strip() == 'Новая пословица' :
            answer = random.choice(latin)
            photo = open('image/' + random.choice(os.listdir('image')), 'rb')
            bot.send_photo(message.chat.id, photo, caption=answer)
    else:
        bot.send_message(message.chat.id, text="Я могу отвечать только на нажатие кнопок")

# бесконечное выполнение кода
bot.polling(non_stop=True, interval=0) 