
import telebot
from habr import pars, pars_serch
import random
from telebot import types
import os


TOKEN="2073512340:AAF2H5s3Y4II2-s2pAIn4R2W3QFJ1LQJfOI"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    #keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("all news")
    item2 = types.KeyboardButton("next")
    item3 = types.KeyboardButton("serch")
    item4 = types.KeyboardButton("reset")
    markup.add(item1, item2,item3, item4)
    bot.send_message(message.chat.id, "Это хабр бот, по вашему запросу могут быть выданы сaмые новые статьи с этого сайта.".format(message.from_user,
        bot.get_me()), parse_mode="html", reply_markup=markup)










nom = 2
@bot.message_handler(content_types=["text"])
def lalala(message):
    global nom

    messag=str(message.text)
    if message.chat.type=="private":
        a = str(messag[:1])
        if messag == "all news":

            for i in pars(1):   bot.send_message(message.chat.id, i[1])
            print("print 1 page")
        elif messag == "next":
            old_page = pars(nom - 1)
            print(f"Print {nom} page")
            for i in pars(nom):
                if i not in old_page:
                    bot.send_message(message.chat.id, i[1])
            nom+=1
        elif a == "!":
            word = messag[1:].strip()
            print("!")
            lists=pars_serch(word)
            for i in lists:
                tex = i[0]+'\n'+i[1]
                bot.send_message(message.chat.id,  tex)
        elif message.text == "serch":
            bot.send_message(message.chat.id, 'Для поиска по ключевому слову введите:   <b>!</b> "ключевое слово"'.format(message.from_user,
        bot.get_me()), parse_mode="html")
        elif message.text == "reset":
            nom = 2
            print(nom)
        else:   bot.send_message(message.chat.id,"ffffff")
#run
bot.polling(none_stop=True)