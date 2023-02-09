import requests
import pyrogram
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton 
from pyrogram import Client, filters
from config import BOT_TOKEN, API_HASH, API_ID
import json
from urllib.request import urlopen
from unidecode import unidecode
from urllib.request import urlopen
import random

kuratrdıklarımızknl = "dddhhsjdheuehehehrjr"

Bot = Client("DepremBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

url = "https://hasanadiguzel.com.tr/api/sondepremler"

@Bot.on_message(filters.command("start"))
async def start(bot, message):
    await bot.send_photo(
        chat_id=message.chat.id,
        photo="https://telegra.ph/file/8069ff4c3544d796c977a.jpg",
        caption="Komut 1 - /deprem Son Depremi Gösterir.\nKomut 2 - /deprem3 Son 3 Depremi Gösterir.\nKomut 3 - /hava girdiğin bölgenin güncel hava durumunu gösterir.\n\nBeni Oluşturan: @mmagneto")


@Bot.on_message(filters.command("deprem"))
async def deprembilgi(bot, message):
    try:
        response = requests.get(url)
        data = response.json()
        bilgi = data['data'][0]
        latitude1 = f"{bilgi['enlem_n']}"
        longitude1 = f"{bilgi['boylam_e']}"
        dadresurl = 'https://maps.google.com/maps?q=' + latitude1 + ',' + longitude1
        text = f"**TÜRKİYE'DE YAŞANAN SON DEPREM!!!:**\nBüyüklük: {bilgi['ml']}\nDerinlik: {bilgi['derinlik_km']}\nLokasyon: [{bilgi['yer']}]({dadresurl})\nTarih: {bilgi['tarih']}\nSaat: {bilgi['saat']}"
        await bot.send_message(
            chat_id=message.chat.id, 
            text=text) 
    except Exception as e:
        print(e)
        await bot.send_message(
            chat_id=message.chat.id,
            text=f"`{e}`")

@Bot.on_message(filters.command('nobetcieczane'))
async def eczanebilgi(bot, message):
    if len(message.text) < 3:
        await bot.send_message(
            chat_id=message.chat.id,
            text="`Hatalı Kullanım`")
    else:
        yer = unidecode(message.text).lower().split()
        il = yer[1]
        ilce = yer[2]
        eczane_url = f"https://www.nosyapi.com/apiv2/pharmacyLink?city={il}&county={ilce}&apikey=aYG3s2ErzrWUUl7Xt6RrTzve0zm3rb5gfgYHfoh9IBTO84ZhFp7dgi6wz7C6"
        istek = requests.get(eczane_url)
        veri = istek.json()
        ebilgi = veri['data'][0]
        elatitude = f"{ebilgi['latitude']}"
        elongitude = f"{ebilgi['longitude']}"
        adresurl = 'https://maps.google.com/maps?q=' + elatitude + ',' + elongitude
        text = f"Nöbetçi Eczane: ⚕ {ebilgi['EczaneAdi']}\n\nTelefon Numarası: ☎️ {ebilgi['Telefon']}\n\n@TrDepremBot" 
        await bot.send_location(
            chat_id=message.chat.id,
            latitude=float(elatitude), 
            longitude=float(elongitude),
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{ebilgi['EczaneAdi']} Git", url=adresurl),InlineKeyboardButton(f"Beni Oluşturan", url="https://t.me/mmagneto")]]))
        await bot.send_message(
            chat_id=message.chat.id,
            text=text)

@Bot.on_message(filters.command("deprem3"))
async def deprembilgi(bot, message):
    try:
        response = requests.get(url)
        data = response.json()
        bilgi = data['data'][0]
        bilgi1 = data['data'][1]
        bilgi2 = data['data'][2]
        latitude1 = f"{bilgi['enlem_n']}"
        longitude1 = f"{bilgi['boylam_e']}"
        dadresurl = 'https://maps.google.com/maps?q=' + latitude1 + ',' + longitude1
        latitude2 = f"{bilgi1['enlem_n']}"
        longitude2 = f"{bilgi1['boylam_e']}"
        dadresurl1 = 'https://maps.google.com/maps?q=' + latitude2 + ',' + longitude2
        latitude3 = f"{bilgi2['enlem_n']}"
        longitude3 = f"{bilgi2['boylam_e']}"
        dadresurl2 = 'https://maps.google.com/maps?q=' + latitude3 + ',' + longitude3
        text = f"**TÜRKİYE'DE YAŞANAN SON 3 DEPREM!!!:**\nBüyüklük: {bilgi['ml']}\nDerinlik: {bilgi['derinlik_km']}\nLokasyon: [{bilgi['yer']}]({dadresurl})\nTarih: {bilgi['tarih']}\nSaat: {bilgi['saat']}\n\nBüyüklük: {bilgi1['ml']}\nDerinlik: {bilgi1['derinlik_km']}\nLokasyon: [{bilgi1['yer']}]({dadresurl1})\nTarih: {bilgi1['tarih']}\nSaat: {bilgi1['saat']}\n\nBüyüklük: {bilgi2['ml']}\nDerinlik: {bilgi2['derinlik_km']}\nLokasyon: [{bilgi2['yer']}]({dadresurl2})\nTarih: {bilgi2['tarih']}\nSaat: {bilgi2['saat']}"
        await bot.send_message(
            chat_id=message.chat.id, 
            text=text) 
    except Exception as e:
        print(e)
        await bot.send_message(
            chat_id=message.chat.id,
            text=f"`{e}`")


@Bot.on_message(filters.command('hava'))
async def hava(bot, message):
    try:
        if len(message.text) < 2:
            bot.send_message(message.chat.id, "Hatalı Kullanım")
        else:
            ev = unidecode(message.text).lower().split()
            sehir = ev[1]
            sehir1 = sehir.upper()
            hava_api = f"https://api.openweathermap.org/data/2.5/weather?appid=51018b60257b50207fc63de7c53af5e1&q={sehir}"
            deger2 = urlopen(hava_api).read().decode("utf-8")
            havajson = json.loads(deger2)
            coord = havajson["coord"]
            weather = havajson["weather"][0]
            genel = havajson["main"]
            wind = havajson["wind"]
            derece = float(genel['temp']) - 273
            derece2 = float(genel['feels_like']) - 273
            icon="🌨️"
            if weather["icon"]=="11d":
                icon="⛈"
            elif weather["icon"]=="09d":
                icon="☔"
            elif weather["icon"]=="10d":
                icon="🌦"
            elif weather["icon"]=="13d":
                icon="❆"
            elif weather["icon"]=="50d":
                icon="🌫"
            elif weather["icon"]=="01d":
                icon="🌞"
            elif weather["icon"]=="01n":
                icon="🌜"
            elif weather["icon"]=="03d" or weather["icon"]=="03n" :
                icon="☁"
            elif weather["icon"]=="04d" or weather["icon"]=="04n" :
                icon="⛅"
            elif weather["icon"]=="13n" :
                icon="🌨️" 
            text = f"{sehir1} için:\n**Hava Durumu**: `{weather['description']}` {icon}\n**Sıcaklık**: `{derece}`\n**Hissedilen Sıcaklık**: `{derece2}`"
            await bot.send_message(
               chat_id=message.chat.id,
               text=text)
    except Exception as e:
        await bot.send_message(
            chat_id=message.chat.id,
            text=f"`{e}`")

@Client.on_message(filters.command('kurtardiklarimiz'))
async def kurtardiklarimiz(bot, message):
    m.id = random.randint(2, 92)
    await bot.copy_message(
        chat_id=chat_id,
        from_chat_id=kuratrdıklarımızknl,
        message_id=m.id)
        
Bot.run() 
