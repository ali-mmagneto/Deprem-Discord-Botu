import requests
import pyrogram
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton 
from pyrogram import Client, filters
from config import BOT_TOKEN, API_HASH, API_ID
import json

Bot = Client("DepremBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

eczane = "https://www.nosyapi.com/apiv2/pharmacyLink?city=duzce&county=cumayeri&apikey=aYG3s2ErzrWUUl7Xt6RrTzve0zm3rb5gfgYHfoh9IBTO84ZhFp7dgi6wz7C6"

url = "https://hasanadiguzel.com.tr/api/sondepremler"


@Bot.on_message(filters.command("start"))
async def start(bot, message):
    await bot.send_photo(
        chat_id=message.chat.id,
        photo="https://telegra.ph/file/8069ff4c3544d796c977a.jpg",
        caption="Komut - /deprem\nBeni Oluşturan: @mmagneto")


@Bot.on_message(filters.command("deprem"))
async def deprembilgi(bot, message):
    try:
        response = requests.get(url)
        data = response.json()
        bilgi = data['data'][0]
        text = f"**TÜRKİYE'DE YAŞANAN SON DEPREM!!!:**\nBüyüklük: {bilgi['ml']}\nDerinlik: {bilgi['derinlik_km']}\nLokasyon: {bilgi['yer']}\nTarih: {bilgi['tarih']}\nSaat: {bilgi['saat']}"
        await bot.send_message(
            chat_id=message.chat.id, 
            text=text) 
    except Exception as e:
        print(e)
        await bot.send_message(
            chat_id=message.chat.id,
            text=f"`{e}`")

@Bot.on_message(filters.command('eczane'))
async def eczanebilgi(bot, message):
    istek = requests.get(eczane)
    veri = istek.json()
    ebilgi = veri['data'][0]
    elatitude = f"{ebilgi['latitude']}"
    elongitude = f"{ebilgi['longitude']}"
    adresurl = 'https://maps.google.com/maps?q=' + elatitude + ',' + elongitude
    text = f"Nöbetçi Eczane: {ebilgi['EczaneAdi']}\n\nTelefon Numarası: {ebilgi['Telefon']}\n\n@TrDepremBot" 
    await bot.send_location(
        chat_id=message.chat.id,
        latitude=float(elatitude), 
        longitude=float(elongitude),
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{ebilgi['EczaneAdi']} Git", url=adresurl),InlineKeyboardButton(f"Beni Oluşturan", url="https://t.me/mmagneto")]]))
    await bot.send_message(
        chat_id=message.chat.id,
        text=text)
Bot.run()
