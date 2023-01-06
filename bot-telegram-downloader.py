from api_bot import geturlfacebook,urlinsta,urltube,urltiktok
import telebot

BOT_TOKEN="5611816657:AAHtAFDZ8TXkWIGHUhdqnwcRayRqe2_1SHU"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(func=lambda msg:True)
def send_replay(message):
    if "facebook.com" in message.text or "fb.watch" in message.text:
        bot.reply_to(message,geturlfacebook(message.text))
    elif "youtube.com" in message.text or  "youtu.be" in message.text:
        bot.reply_to(message,urltube(url=message.text))

    elif "instagram.com" in  message.text:
        bot.reply_to(message,urlinsta(url=message.text))
    elif "tiktok.com" in  message.text:
        bot.reply_to(message,urltiktok(url=message.text))


           
    elif "start" in message.text:
        bot.reply_to(message,"اهلا مرحبا بك في بوت التحميل الخاص بي هوك حط ليك الفيديو الي عايز تحمله  وهيرجعلك لينك التحميل")


bot.infinity_polling()
