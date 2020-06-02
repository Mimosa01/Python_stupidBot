# -*- coding: utf-8 -*-

import telebot

bot = telebot.TeleBot("1298531617:AAE3SCepRRJSuEOHIclidw3MYZC0N54WNt8")

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
     bot.infinity_polling()
