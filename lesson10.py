# 7046057284:AAHHBka-ErQrw9b5dDJCdAdsQSn1MTvlYaI
import random
import telebot
from telebot import types
import os
bot = telebot.TeleBot("7046057284:AAHHBka-ErQrw9b5dDJCdAdsQSn1MTvlYaI")

@bot.message_handler(commands=["start"])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🎲 Какую оценку сегодня получишь?")
    item2 = types.KeyboardButton("😊 Как дела?")

    markup.add(item1, item2)

    bot.send_message(message.chat.id, "🎲Hello!!!".format(message.from_user, bot.get_me()), parse_mode='html',
    reply_markup=markup)
@bot.message_handler(commands=['help'])
def help(message):
    sti = ("/sendnumber - send you random number(0-9)\n/secretcode - send you random code(30 symbols)\n"
                     "/atomicboom - send you gif file atomic boom\n/frog - send you gif file dancing rainbow frog\n"
                     "/photo - send you cockroach's photo\n/audio - send you audio file\n/cat - send you cat's photo")
    bot.send_message(message.chat.id, sti)
@bot.message_handler(commands=['sendnumber'])
def sendnumber(message):
    sti = random.randint(0, 9)
    bot.send_message(message.chat.id, sti)
@bot.message_handler(commands=['secretcode'])
def secretcode(message):
    list_of_cymbols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 's', 't',
                       'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '_', '#']
    secretcode = ""
    while len(secretcode) != 30:
        list_of_cymbols_index = random.randint(0, len(list_of_cymbols)-1)
        cymbol_for_secret_code = list_of_cymbols[list_of_cymbols_index]
        secretcode += cymbol_for_secret_code
    bot.send_message(message.chat.id, secretcode)
@bot.message_handler(commands=['atomicboom'])
def atomicboom(message):
    sti = open('7goP.gif', 'rb')
    bot.send_animation(message.chat.id, sti)
@bot.message_handler(commands=['frog'])
def frog(message):
    sti = open('frog.gif', 'rb')
    bot.send_animation(message.chat.id, sti)
@bot.message_handler(commands=['photo'])
def stickers(message):
    sti = open('1.gif', 'rb')
    bot.send_sticker(message.chat.id, sti)
@bot.message_handler(commands=['audio'])
def audio(message):
    sti = open('rington.mp3', 'rb')
    bot.send_audio(message.chat.id, sti)
@bot.message_handler(commands=['cat'])
def cat(message):
    sti = open('кошак.jpg', 'rb')
    bot.send_sticker(message.chat.id, sti)
@bot.message_handler(commands=['book'])
def book(message):
    sti = "your favorite books: Harry Potter"
    bot.send_message(message.chat.id, sti)
@bot.message_handler(commands=['film'])
def film(message):
    sti = "your favorite films: Avatar"
    bot.send_message(message.chat.id, sti)
@bot.message_handler(commands=['sport'])
def sport(message):
    sti = "your favorite kinds of sport: football, basketball"
@bot.message_handler(commands=['funnystory'])
def funnystory(message):
    sti = ("your funny story from your life: В детстве я был очень болтливым мальчиком. Мог говорить с утра до вечера, не"
           "переставая, конечно родители уставали от этого. И вот папа придумал, как угомонить мою речь. Папа мне"
           "сказал, что каждому человеку в месяц дается только 10 000 слов, а если слова закончатся, то придется ходить"
           "немым. Я конечно испугался. И вот, бывает, начну опять болтать, а папа мне говорит: «Сегодня только середина"
           "месяца, а ты уже 90 000 слов сказал, осталась у тебя еще тысяча». И тогда я сразу замолкал.")
    bot.send_message(message.chat.id, sti)
@bot.message_handler(commands=['friends'])
def friends(message):
    sti = "your friends: Даниил, Денис, Никита, Артём, Тимофей"
    bot.send_message(message.chat.id, sti)
@bot.message_handler(content_types=['text'])
def processing_text(message):
    if message.chat.type == 'private':
        if message.text == '🎲 Какую оценку сегодня получишь?':
            bot.send_message(message.chat.id, str(random.randint(0,12)))
        elif message.text == '😊 Как дела?':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Да", callback_data='good')
            item2 = types.InlineKeyboardButton("Нет", callback_data='bad')

            markup.add(item1, item2)

            bot.send_message(message.chat.id, 'Отлично, домашку сделал?', reply_markup=markup)
        elif message.text == 'хіба ревуть воли як ясла повні?':
            bot.send_message(message.chat.id, 'не ревуть')
        else:
            bot.send_message(message.chat.id, 'I don\'t know ')








    


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'Вот и отличненько 😊')
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                    text="ЭТО ШЕДЕВР!")
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Маме расскажу, ругать будет 😢')
                bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                    text="ТІКАЙ З СЕЛА!!!!")

            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="😊 Как дела?",
                reply_markup=None)

            # show alert
    except Exception as e:
        print(repr(e))
bot.polling(none_stop=True)