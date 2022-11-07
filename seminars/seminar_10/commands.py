from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime
from spy import *

def hello(update: Update, context: CallbackContext) -> None:
    log(update, context)
    update.message.reply_text(f'Hello {update.effective_user.first_name}')


def bot_help(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'/hello\n/help\n/time\n/summ ')


def bot_time(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'{datetime.datetime.now().time()}')


def bot_summ(update: Update, context: CallbackContext):
    try:
        log(update, context)
        num = update.message.text
        print(num)
        num = num.split()
        sum = int(num[1]) + int(num[2])
        update.message.reply_text(f'{num[1]} + {num[2]} = {sum}')

    except:
        update.message.reply_text("Ошибка ввода")
