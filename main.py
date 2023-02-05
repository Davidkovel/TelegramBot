# фунция отправки сообщение на 2 телеграм бот
import telebot
from telebot import types
import requests

bot = telebot.TeleBot('6061256501:AAFN6PglDd4-D4mtbYdY8pjeVxQq3M3mI-g')
bot2 = telebot.TeleBot("5940284114:AAEFndG_ea1a_hL5luxKavY0NFQl_lPGcoI")

# команда /start
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('📁Каталог')
    item2 = types.KeyboardButton('📦Заказы')
    markup.add(item1, item2)
    bot.send_message(message.chat.id, 'Привет', reply_markup=markup)

# кнопкы
@bot.message_handler(content_types=['text'])
def cars_choice(message):
    if message.chat.type == 'private':
        if message.text == '📁Каталог':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            clothes1 = types.KeyboardButton('👟Кроссовкы')
            item4 = types.KeyboardButton('🔙Назад')
            markup.add(clothes1, item4)

            bot.send_message(message.chat.id, 'Выберайте', reply_markup=markup)

        if message.text == '👕Рубашка':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            clothes1 = types.KeyboardButton('👟Кроссовкы')
            item4 = types.KeyboardButton('🔙Назад')
            markup.add(clothes1, item4)
    # после кнопкы купить
    if message.text == '👟Кроссовкы':
        # Открытие картинки
        img = open("C:\\Users\\davidik07\\Pictures\\Dropshiping\\28458157.jpg", 'rb')

        # Создание маркапа с кнопкой купить
        markup = types.InlineKeyboardMarkup()
        buy_button = types.InlineKeyboardButton("Купить", callback_data='buy')
        markup.add(buy_button)

        # Отправка фотографии и текста
        bot.send_photo(message.chat.id, img)
        bot.send_message(message.chat.id, 'Хорошие кроссовкы, хорошо качество', reply_markup=markup)

    if message.text == 'Купить':
        bot.send_message(message.chat.id, "Номер телефона")
        bot.register_next_step_handler(message, get_phone_number)
        # bot.send_message(message.chat.id, 'Номер телефона')
        # phone_number = message.text
        # bot.send_message(message.chat.id, f'Ваш номер телефона - {phone_number}')
        # bot2.send_message(chat_id='5034541225', text=f'Пользватель заказали посылку, номер телефона {phone_number}')

def get_phone_number(message):
    phone_number = message.text
    bot.send_message(message.chat.id, "Адресс")
    bot.register_next_step_handler(message, get_address, phone_number=phone_number)

def get_address(message, phone_number):
    adress = message.text
    bot.send_message(message.chat.id, f"Ваш номер телефона: {phone_number}, Ваш адресс {adress}")
    bot2.send_message(chat_id='5034541225', text=f"Пользователь заказал посылку, номер телефона: {phone_number},Адресс: {adress}")


@bot.callback_query_handler(func=lambda call: call.data == 'buy')
def buy_handler(call):
    bot.send_message(call.message.chat.id, "Номер телефона")
    bot.register_next_step_handler(call.message, get_phone_number)

bot.polling(none_stop=True)

