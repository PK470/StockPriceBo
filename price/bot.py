import telebot
import os
from dotenv import load_dotenv
from stock_price import StockPrice  


load_dotenv()


TOKEN = os.getenv('BOT_TOKEN')


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Send me a stock symbol followed by /price, and I'll fetch the price for you.")


@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = (
        "Here are the commands you can use:\n"
        "/start - Start the bot and receive a welcome message.\n"
        "/help - Get a list of available commands.\n"
        "/price <stock_symbol> - Get the current price of a stock. Example: /price NHPC"
    )
    bot.reply_to(message, help_text)

@bot.message_handler(commands=['price'])
def get_stock_price(message):
    
    stock_symbol = message.text.split(' ', 1)[1] if len(message.text.split(' ', 1)) > 1 else ''
    sp = StockPrice()
    try:
        price = sp.get_price(stock_symbol)
        bot.reply_to(message, f"The current price of {stock_symbol} is ₹{price}.")
    except Exception as e:
        bot.reply_to(message, f"Sorry, I couldn't find that {stock_symbol}. Please check the spelling or try another symbol.")

@bot.message_handler(func=lambda message: True)  
def handle_unknown_command(message):
    bot.reply_to(message, f"Unknown command: {message.text}")
    send_help(message)

bot.polling()
