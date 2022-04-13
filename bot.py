import os
import telebot
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()
TOKEN = os.environ.get('TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['commands', 'help'])
def greet(message):
    bot.reply_to(message, "Here's what I can do:\n\\commands, \\help, and echo\ntype any message to echo!")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.polling()
