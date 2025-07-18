import telebot
from telebot import types, TeleBot

bot: TeleBot = telebot.TeleBot('6550986023:AAGq7mmtJl_pmBW3MsyXgx22uYz4en1Jco4')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("500₽")
    btn2 = types.KeyboardButton("1000₽")
    btn3 = types.KeyboardButton("1500₽")
    btn4 = types.KeyboardButton("3000₽")
    btn5 = types.KeyboardButton("любой")
    markup.add(btn1, btn2, btn3, btn4, btn5)
    bot.send_message(message.chat.id, 'Привет, выбери один из диапозонов цен и я скину под него подходящую композицию:',
                     reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == "500₽":
        audio = open("74172714276124.mp3", "rb")
        bot.send_audio(message.chat.id, audio)
        audio = open("8158172451827456.mp3", "rb")
        bot.send_audio(message.chat.id, audio)
    elif message.text == "1000₽":
        audio = open("444444445425.mp3", "rb")
        bot.send_audio(message.chat.id, audio)
    elif message.text == "1500₽":
        audio = open("е4е4е4е4е4.mp3", "rb")
        bot.send_audio(message.chat.id, audio)
    elif message.text == "3000₽":
        audio = open("1234444.mp3", "rb")
        bot.send_audio(message.chat.id, audio)
        audio = open("14768876141874.mp3", "rb")
        bot.send_audio(message.chat.id, audio)
    elif message.text == "любой":
        audio = open("74172714276124.mp3", "rb")
        bot.send_audio(message.chat.id, audio)
        audio = open("8158172451827456.mp3", "rb")
        bot.send_audio(message.chat.id, audio)
        audio = open("444444445425.mp3", "rb")
        bot.send_audio(message.chat.id, audio)
        audio = open("е4е4е4е4е4.mp3", "rb")
        bot.send_audio(message.chat.id, audio)
        audio = open("1234444.mp3", "rb")
        bot.send_audio(message.chat.id, audio)
        audio = open("14768876141874.mp3", "rb")
        bot.send_audio(message.chat.id, audio)
    else:
        bot.send_message(message.chat.id, text="Извини, такого диапозона цен у меня нет(")


bot.polling(none_stop=True)
