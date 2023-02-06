import requests
import pyrogram
from pyrogram import Client, filters
from config import BOT_TOKEN, API_HASH, API_ID
import json

bot = Client("DepremBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)


url = "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2023-01-01&endtime=2023-12-31&minmagnitude=4&limit=1&orderby=time&latitude=39&longitude=35&maxradiuskm=1000"

@Client.on_message(filters.command('deprem'))
async def deprembilgi(bot, message):
    try:
        response = requests.get(url)
        data = json.load(open(response))
        earthquake_info = data['features'][0]['properties']
        message = f"**DİKKAT! TÜRKİYEDE DEPREM!!!:**\nBüyüklük: {earthquake_info['mag']}\nLokasyon: {earthquake_info['place']}\nZaman: {earthquake_info['time']}\nDetaylı Bilgi: {earthquake_info['url']}"
        await bot.send_message(
            chat_id=message.chat.id, 
            text=message) 
    except Exception as e:
        print(e)
        await bot.send_message(
            chat_id=message.chat.id,
            text=f"`{e}`")

bot.run()
