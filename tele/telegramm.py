
import telebot


token = ''
my_id = 4432324

token = ''
my_id = 

bot = telebot.TeleBot(token)

def send_message(text):
    bot.send_message(my_id, text, parse_mode="Markdown")
