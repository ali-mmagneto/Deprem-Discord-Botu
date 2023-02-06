import requests
import pyrogram
from pyrogram import Client, filters
from config import BOT_TOKEN, API_HASH, API_ID
import json

Bot = Client("DepremBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)


url = "https://hasanadiguzel.com.tr/api/sondepremler"

@Bot.on_message(filters.command("deprem"))
async def deprembilgi(bot, message):
    try:
        response = requests.get(url)
        data = response.json()
        bilgi = data['data'][0]
        text = f"**DİKKAT! TÜRKİYEDE DEPREM!!!:**\nBüyüklük: {bilgi['ml']}\nDerinlik: {bilgi['derinlik_km']}\nLokasyon: {bilgi['yer']}\nZaman: {bilgi['saat']}"
        await bot.send_message(
            chat_id=message.chat.id, 
            text=text) 
    except Exception as e:
        print(e)
        await bot.send_message(
            chat_id=message.chat.id,
            text=f"`{e}`")

Bot.run()
