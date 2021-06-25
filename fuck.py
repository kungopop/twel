from telegram import *
from telegram.ext import *
bot = Bot("1886958966:AAGdTzp7iULCnEpZgf4wuV92ldkLVeXP5CY")
#print(bot.getMe())
updater = Updater("1886958966:AAGdTzp7iULCnEpZgf4wuV92ldkLVeXP5CY",use_context=True)

dispatcher = updater.dispatcher
def test_function(update:Update,context:CallbackContext):
    bot.sendMessage(

        chat_id=update.effective_chat.id,
        text="اؤمرني يا نجم",

    )

def test_function2(update:Update,context:CallbackContext):
    bot.sendMessage(

        chat_id=update.effective_chat.id,
        text="يولا يا زعيم ",

    )

def lol(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'انت يا جدع  {update.effective_user.first_name}')

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'نورتنا يا زعيم  {update.effective_user.first_name}')

start_value1=CommandHandler('HELLO',test_function)
start_value2=CommandHandler('HELLO_pro',test_function2)

updater.dispatcher.add_handler(CommandHandler('lol', lol))
updater.dispatcher.add_handler(CommandHandler('start', start))

dispatcher.add_handler(start_value1)
dispatcher.add_handler(start_value2)

print(bot.getMe())

updater.start_polling()
