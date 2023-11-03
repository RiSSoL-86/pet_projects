import config
import telebot

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(content_types=['text'])
def eehhoo_bot(message):
    """Эхо бот."""
    bot.send_message(message.chat.id, message.text)
    
bot.polling(non_stop=True)
