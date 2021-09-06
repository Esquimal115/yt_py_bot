import telebot
import requests
import youtube_dl
import os
from youtube_dl import YoutubeDL
from bs4 import BeautifulSoup
import urllib3

token = '1928309017:AAHbrM5jRBO1yzhHHH9AkXWKi9GhAx9IyN0'
url = f'https://api.telegram.org/bot{token}/getUpdates'

bot = telebot.TeleBot(token)
id_chat = 1928309017
# user_id = 450125694



@bot.message_handler(func=lambda message: True)
def echo_all(message):
    try:
        user_id = message.chat.id
        SAVE_PATH = '/'.join(os.getcwd().split('/')[:3]) + '/Downloads'
        options = {
            'format': 'bestaudio/best',
            'outtmpl': SAVE_PATH + '/%(title)s.%(ext)s',
        }

        with youtube_dl.YoutubeDL(options) as ydl:
            song_url = str(message.text).split('&')[0]
            ydl.download([song_url])
        os.chdir(SAVE_PATH)
        song = os.listdir()
        bot.send_audio(user_id, audio=open(song[0], 'rb'))
        os.remove(song[0])

    except:
        bot.send_message(user_id, "Error al procesar la URL")


bot.polling()
