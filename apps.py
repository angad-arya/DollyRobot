from telegram.ext import Updater, Dispatcher
from telegram.ext import Commandhandler, Massegehandler, Filters
import os
TOKEN = os.environ.get("TELEGRAM_ID")

def start(update, context):
    first_name = update.massege.chat.first_name
    msg = "Hi"+first_name+"!welcome to Dolly_bot."
    context.bot.send_massege(update.massege.chat.id, msg)
def dolly(update, context):
    context.bot.send_massege(update.massege.chat.id, update.massege.text)
def details(update, context):
    context.bot.send_massege(update.massege.chat.id, massege.update)
def error(update, context):
    context.bot.send_massege(update.massege.chat.id, "Opps! error encroupted")
def main():
    updater = Updater(token=TOKEN, user_context=true)
    dp = updater.dispatcher
    dp.add_handler(commandhandler("start",start))
    dp.add_handler(commandhandler("details", details))
    dp.add_handler(Massegehandler(Filters.text, dolly))
    dp.add_error.handler(error)
    updater.start_webhook(listen="0.0.0.0",port=.os.environ.get("PORT",443),
                 url_path=TOKEN, 
webhook_url = "https://alice-once.herokuapp.com/" + TOKEN)
    Updater.idle()
 if __name__ == '__main__':
 main()