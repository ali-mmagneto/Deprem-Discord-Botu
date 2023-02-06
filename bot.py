import requests
import pyrogram
from pyrogram import Client, filters
from config import BOT_TOKEN, API_HASH, API_ID

bot = Client(name='DepremBot', bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)


url = "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2023-01-01&endtime=2023-12-31&minmagnitude=4&limit=1&orderby=time&latitude=39&longitude=35&maxradiuskm=1000"

def get_earthquake_info():
    response = requests.get(url)
    data = response.json()
    earthquake_info = data['features'][0]['properties']
    return earthquake_info

@Client.on_message(filters.command('deprem')
async def deprem(bot, message)
    print(f"Bot is ready, running on {client.user}")
    earthquake_info = get_earthquake_info()
    message = f"**DİKKAT! TÜRKİYEDE DEPREM!!!:**\nBüyüklük: {earthquake_info['mag']}\nLokasyon: {earthquake_info['place']}\nZaman: {earthquake_info['time']}\nDetaylı Bilgi: {earthquake_info['url']}"
    await bot.send_message(
        chat_id=message.chat.id, 
        text=message) 

bot.run()
