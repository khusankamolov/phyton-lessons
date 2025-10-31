# -*- coding: utf-8 -*-
"""
Created on Tue Oct 21 19:09:41 2025

@author: Surface
"""

from transliterate import to_cyrillic,to_latin
import telebot
TOKEN='8295310818:AAHeqTygSDcOUG3wwhZejE8amkzt-OhxJ9g'
bot = telebot.TeleBot(TOKEN, parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN

@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob='Assalomu alaykum,xush kelibsiz!'
    javob+='\nMatn kiriting:'
    bot.reply_to(message, javob)
    
bot.infinity_polling()


#matn=input("Enter a text:")

#if matn.isascii():
 #   print(to_cyrillic(matn))
#else:
 #   print(to_latin(matn))