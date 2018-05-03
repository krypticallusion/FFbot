from FFbot.modules.sql.translation import switch_to_locale, prev_locale
from FFbot.modules.translations.strings import tld
from telegram.ext import CommandHandler
from FFbot import dispatcher
from FFbot.modules.translations.list_locale import list_locales
from FFbot.modules.helper_funcs.chat_status import user_admin

@user_admin
def change_locale(bot, update, args):
    chat = update.effective_chat
    if len(args) > 0:
        locale = args[0].lower()
        if locale in list_locales:
            if locale in  ('en', 'de', 'nl', 'id', 'fi', 'pt-br'):
                switch_to_locale(chat.id, locale)
                update.message.reply_text(tld(chat.id, 'Switched to {} successfully!').format(list_locales[locale]))
            else:
                update.message.reply_text("{} not supported yet!".format(list_locales[locale]))
        else:
            update.message.reply_text("Is that even a valid language code? Use an internationally accepted ISO code!")
    else:
        update.message.reply_text("You haven't give me a locale to begin with!")

def curn_locale(bot, update):
    chat_id = update.effective_chat.id
    LANGUAGE = prev_locale(chat_id)
    if LANGUAGE:
        locale = LANGUAGE.locale_name
        native_lang = list_locales[locale]
        update.message.reply_text("Current locale for this chat is : {}".format(native_lang))
    else:
        update.message.reply_text("Current locale for this chat is : English")

CURN_LOCALE_HANDLER = CommandHandler("localenow", curn_locale)
LOCALE_HANDLER = CommandHandler(["set_locale", "locale"], change_locale, pass_args=True)
dispatcher.add_handler(LOCALE_HANDLER)
dispatcher.add_handler(CURN_LOCALE_HANDLER)
