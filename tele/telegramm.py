
import telebot

<<<<<<< HEAD
token = '5234349306:AAEhMvHbT56dSFRJlBjVL_WQvvdjasnOhA8'
my_id = 443232407
=======
token = ''
my_id = 
>>>>>>> 1b4f1a5237ffab42bd3753dbfbbdcb9639dad022
bot = telebot.TeleBot(token)

def send_message(text):
    bot.send_message(my_id, text, parse_mode="Markdown")
