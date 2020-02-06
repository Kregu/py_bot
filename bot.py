from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import Updater
from telegram.ext import Filters
from telegram.ext import MessageHandler

import settings

def message_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text = 'Hello world!!!',
    )


def main():
    print('Start')

    updater = Updater(
        settings.token,
        use_context=True,
    )
    updater.dispatcher.add_handler(MessageHandler(filters=Filters.all, callback=message_handler))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
