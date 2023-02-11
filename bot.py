import requests
import telegraph
from telegraph import upload_file
from telegraph import Telegraph
import pyrogram
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton 
from pyrogram import Client, filters
from config import BOT_TOKEN, API_HASH, API_ID
import json
from urllib.request import urlopen
from unidecode import unidecode
from urllib.request import urlopen
import random
import os
from PIL import Image
from pyrogram.types import Message
from pyrogram import Client, filters
import KekikSpatula
from KekikSpatula import NobetciEczane, Doviz, SonDepremler
Bot = Client("DepremBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
telegraph = Telegraph()
telegraph.create_account(short_name='deprembot')

url = "https://hasanadiguzel.com.tr/api/sondepremler"
doviz_ = Doviz()

@Bot.on_message(filters.command("doviz"))
async def dovizzz(bot, message):
    text = "**Birim / Gişe Alış / Gişe Satış**\n\n"
    for key in json.loads(doviz_.gorsel())["veri"]:
        text += f"**{key['birim']}**: {key['Gişe Satış']} TL - {key['Gişe Satış']}\n"
    await message.reply_text(text) 

@Bot.on_message(filters.command('depre'))
async def eczanebilgi(bot, message):
    deprem = SonDepremler()
    text = "Depremler:\n"
    say = 0
    for i in json.loads(deprem.gorsel())["veri"]:
        text += f"{i['ml']}\n"
        say += 1
        if say > 6:
            await bot.send_message(
                chat_id=message.chat.id, 
                text=text)

@Bot.on_message(filters.command("start"))
async def start(bot, message):
    await bot.send_photo(
        chat_id=message.chat.id,
        photo="https://telegra.ph/file/8069ff4c3544d796c977a.jpg",
        caption="Komut 1 - /deprem Son Depremi Gösterir.\nKomut 2 - /deprem3 Son 3 Depremi Gösterir.\nKomut 3 - /hava girdiğin bölgenin güncel hava durumunu gösterir.\nKomut 4 - /kurtardiklarimiz azcikta olsa içimize umut serpicek görüntüler. Kaynak: @solcugazete, @bpthaber\n\nBeni Oluşturan: @mmagneto")
    print(python3 --version)
@Bot.on_message(filters.command('donustur'))
async def donusturucu(bot, message):
    user_id = message.from_user.id
    message_id = message.reply_to_message.id
    name_format = f"Mickey_{user_id}_{message_id}"
    if message.reply_to_message.photo:
        m = await message.reply_text("`Dönüştürülüyor...`")
        image = await bot.download_media(
                    message = message.reply_to_message,
                    file_name=f"{name_format}.jpg")
        await m.edit("`Gönderiyorum...`")
        im = Image.open(image).convert("RGB")
        im.save(f"{name_format}.webp", "webp")
        sticker = f"{name_format}.webp"
        await m.reply_sticker(sticker)
        await m.delete()
        os.remove(sticker)
        os.remove(image)
    elif message.reply_to_message.sticker.is_animated:
        rand_id = random.randint(1, 900)
        mes = await bot.send_message(message.chat.id, "`Dönüştürülüyor...`")
        await bot.download_media(
            message = message.reply_to_message,
            file_name=f"downloads/{message.chat.id}-{rand_id}.tgs")
        old_name = f"downloads/{message.chat.id}-{rand_id}.tgs"
        new_name = f"downloads/{message.chat.id}-{rand_id}.gif"
        os.rename(old_name, new_name)
        await message.reply_animation(f"{message.chat.id}-{rand_id}.gif")
        mes.delete()
        os.remove(f"downloads/{message.chat.id}-{rand_id}.gif")
        os.remove(f'downloads/{message.chat.id}-{rand_id}.tgs')
    else:
        m = await message.reply_text("`Dönüştürülüyor...`")
        sticker = await bot.download_media(
                      message = message.reply_to_message,
                      file_name=f"{name_format}.webp")
        await m.edit("`Gönderiyorum...`")
        im = Image.open(sticker).convert("RGB")
        im.save(f"{name_format}.jpg", "jpeg")
        image = f"{name_format}.jpg"
        await m.reply_photo(image)
        await m.delete()
        os.remove(image)
        os.remove(sticker) 

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

@Bot.on_message(filters.command('kurtardiklarimiz'))
async def kurtardiklarimiz(bot, message):
    kurtardıklarımızknl = "dddhhsjdheuehehehrjr"
    message_id = random.randint(2, 122)
    await bot.copy_message(
        chat_id=message.chat.id,
        from_chat_id=kurtardıklarımızknl,
        message_id=message_id)
        
@Bot.on_message(filters.command('telegraph'))
async def telegraph_yukleme(bot, message):
    try:
        text = await bot.send_message(
                   chat_id=message.chat.id,
                   text="`Yüklüyorum...`")
        try:
            if message.reply_to_message.video or message.reply_to_message.photo:
                dizin = f"downloads/"
                dosya = await message.reply_to_message.download(dizin)
                await text.edit("`Dosyan indiriliyor..`")
                yuklenen = upload_file(dosya) 
                await text.edit(f"https://telegra.ph{yuklenen[0]}")     
                os.remove(dosya) 
            elif message.reply_to_message.text:
                mes = message.reply_to_message.text.html
                link = telegraph.create_page(
                    'Hey',
                    html_content=f"{mes}")
                await text.edit(f"{link['url']}")
        except Exception as e:
            await text.edit(f"`{e}`")
            os.remove(dosya) 
            return         
    except Exception:
        pass

Bot.run() 
