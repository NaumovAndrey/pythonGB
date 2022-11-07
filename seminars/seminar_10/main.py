from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime
from commands import *

updater = Updater('5720864290:AAHcaXDjPpHZpNsZB6aESb0exqjkVjtZ3Ac')
updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('time', bot_time))
updater.dispatcher.add_handler(CommandHandler('help', bot_help))
updater.dispatcher.add_handler(CommandHandler('summ', bot_summ))

updater.start_polling()
updater.idle()
