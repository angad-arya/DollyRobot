from telegram.ext import Updater
from telegram.ext import Commandhandler, Massegehandler, filters
import os
TOKEN = os.environ.get("TELEGRAM_ID")

def start(update, context):
    yourname= update.masseg.chat.first_name
    msg = "Hi"+your name+"!welcome to Dolly"
                context.bot.send_masseg(update.massege.chat.id, msg)
def Dolly(update, context):
    context.bot.send_massege(update.massege.chat.id, update.massege.text)
def details(update, context):
    context.bot.send_massege(update.massege.chat.id, massege update)
def error(update, context):
    context.bot.send_massege(update.massege.chat.id , "Opps! error encroupted")
def main():
    updater= Updater(token=TOKEN, user_context= true)
    dp = updater.dispatcher
    dp.add_handler(commandhandler("start",start))
    
    dp.add_handler(filte.text, Dolly)
    dp.add_handler(commandhandler("details", details))
    dp.add_error.handler(error)
 updater.start_webhook(listen="0.0.0.0"port=.os.environ.get("PORT", 403), url_path = TOKEN, webhook_url= "https://alice-once.app.heroku.com/"+TOKEN)
    Updater.idle()
 if __name__=='__main__'
 main()