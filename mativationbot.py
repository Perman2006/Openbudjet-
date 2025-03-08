import telebot
import requests
import asyncio
from googletrans import Translator

bot = telebot.TeleBot("7843469918:AAEk-YXpK59PXdlo--9vMnZGsiT7HyYAInk")  # Tokeningizni kiriting

async def translate_text(advice):
    translator = Translator()
    result = await translator.translate(advice, dest="uz")  # `await` bilan chaqirish kerak
    return result.text

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    url = "https://api.adviceslip.com/advice"
    r = requests.get(url)
    advice = r.json()["slip"]["advice"]

    translation = asyncio.run(translate_text(advice))  # Asinxron tarjimani ishlatish

    bot.reply_to(message, f"English: {advice} \n\nTarjimasi:{translation}")

bot.infinity_polling()