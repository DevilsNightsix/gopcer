from telegram.ext import Updater, CommandHandler
from gtts import gTTS
import re
import uuid
import os
TOKEN = os.environ['TELEGRAM_TOKEN']
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="I'm bot please talk to me!")

def say(bot, update):
    text = re.sub(r'\/say\s+', '', update.message.text)
    tts = gTTS(text=text, lang='ru')
    message_name ="/tmp/" + uuid.uuid4().hex + "-voice.mp3"
    tts.save(message_name)
    bot.sendVoice(chat_id=update.message.chat_id, voice=open(message_name, 'rb'))
    os.remove(message_name)

start_handler = CommandHandler('start', start)
say_handler = CommandHandler('say', say)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(say_handler)

import os

PORT = int(os.environ.get('PORT', '5000'))
# add handlers
updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN)
updater.bot.setWebhook("https://gopcer-bot.herokuapp.com/" + TOKEN)
updater.idle()
