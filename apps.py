from telegram.ext import Updater, Dispatcher
from telegram.ext import CommandHandler, MessageHandler, Filters
import os
TOKEN = os.environ.get("TELEGRAM_ID")

def start(update, context):
    first_name = update.message.chat.first_name

    msg = "Hi"+first_name+"!welcome to Dolly."
    context.bot.send_message(update.message.chat.id, msg)
    
def Dolly(update, context):
    context.bot.send_message(update.message.chat.id, update.message.text)
    
def details(update, context):
    context.bot.send_message(update.message.chat.id, message.update)

def error(update, context):
    context.bot.send_message(update.message.chat.id, "Opps! error encroupted")

def main():
    updater = Updater(token=TOKEN, user_context=True)

    dp = updater.dispatcher

    dp.add_handler(commandHandler("start",start))
    dp.add_handler(commandHandler("details", details))

    dp.add_handler(MessageHandler(Filters.text, Dolly))

    dp.add_error.handler(error)

    updater.start_webhook(listen="0.0.0.0",port=os.environ.get("PORT",443), 
                          url_path=TOKEN, 
                          webhook_url = "https://alice-once.herokuapp.com/"+TOKEN)
    Updater.idle()
if  __name__ == '__main__':
    main()



