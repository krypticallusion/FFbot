from FFbot.modules.notes import get
from telegram.ext import CommandHandler
from FFbot import dispatcher

def remote_notes_get(bot, update, args):
    if len(args) >= 2 and update.effective_chat.type == 'private':
        try:
            chat_id = int(args[0])
        except ValueError:
            update.effective_message.reply_text("Invalid Chat ID")
        notename = args[1]
        get(bot, update, notename, remote=chat_id)
#        else:
#            update.effective_message.reply_text("Invalid chat ID specified!")
    else:
        update.effective_message.reply_text("Usage limited to PMs only!")

REMOTE_NOTES_GET_HANDLER = CommandHandler("rng", remote_notes_get, allow_edited=True, pass_args=True)
dispatcher.add_handler(REMOTE_NOTES_GET_HANDLER)
