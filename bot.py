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
import time
import re
from PIL import Image
from pyrogram.types import Message
from pyrogram import Client, filters
import KekikSpatula
from KekikSpatula import NobetciEczane, Doviz, SonDepremler, HavaDurumu
Bot = Client("DepremBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
telegraph = Telegraph()
telegraph.create_account(short_name='deprembot')
import asyncio

url = "https://hasanadiguzel.com.tr/api/sondepremler"

from pyrogram import Client, filters
from KekikSpatula import HavaDurumu
from unidecode import unidecode
import json
import re



async def video_to_gif(old_name, new_name, bot, message):
    try:
        output = new_name 
        out_location = f"downloads/{output}"
        command = [
                'ffmpeg','-hide_banner',
                '-i',old_name,
                '-c:v','copy',
                '-y',out_location
                ]

        process = await asyncio.create_subprocess_exec(
                *command,
                # stdout must a pipe to be accessible as process.stdout
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
                )
        await bot.send_video(
            chat_id=message.chat.id, 
            video=out_location)
    except Exception as e:
        await bot.send_message(message.chat.id, f"{e}")

async def depremdongusu(bot, message, caption1, say):
    try:
        sayi = 1
        print(sayi)
        response = requests.get(url)
        data = response.json()
        bilgi = data['data'][0]
        text = "**TÜRKİYE'DE YAŞANAN SON DEPREMLER!!!\n\n**"
        for i in bilgi:
            say += 1
            latitude1 = f"{i['enlem_n']}"
            longitude1 = f"{i['boylam_e']}"
            dadresurl = 'https://maps.google.com/maps?q=' + latitude1 + ',' + longitude1
            text += f"{say}-)\nBüyüklük: {i['ml']}\nDerinlik: {i['derinlik_km']}\nLokasyon: [{i['yer']}]({dadresurl})\nTarih: {i['tarih']} {i['saat']}\n\n"
            if int(say) == sayi:
                if text == caption1:
                    time.sleep(60) 
                    text = "**TÜRKİYE'DE YAŞANAN SON DEPREMLER!!!\n\n**"
                else:
                    await bot.send_message(
                        chat_id="sohbetgnl2", 
                        text=text)
                    caption1 = text
                    say = 0
                    text = "**TÜRKİYE'DE YAŞANAN SON DEPREMLER!!!\n\n**"
                    time.sleep(60)
                    depremdongusu(bot, message, caption1, say)
    except Exception as e:
        print(e)
        await bot.send_message(
            chat_id=message.chat.id,
            text=f"`{e}`")

@Bot.on_message(filters.command('hava'))
async def havaa(bot, message):
    try:
        ev = unidecode(message.text).split()
        if len(ev) < 3:
            await bot.send_message(message.chat.id, "Hatalı Kullanım :/ Doğru Kullanım Şu Şekilde:\n\n`/hava İstanbul Avcılar`") 
            return
        il = ev[1]
        ilce = ev[2]
        istek = HavaDurumu(il, ilce)
        text = ""
        for i in json.loads(istek.gorsel())["veri"]:
            fahrenayt1 = re.findall(r'\d+', f"{i['derece']}") # Api den çektiğimiz hava durumu bilgisinden Fahrenayt birimindeki sayıyı String formattan çekiyoruz.
            fahrenayt =  f"{fahrenayt1[0]}" # list olarak çektiğimiz verinin ilk objesi olan Derece bilgisini fahrenayta tanımlıyoruz. 
            derece = (int(fahrenayt) - 32) / float(1.8) # Fahrenaytı Celciusa çeviriyoruz bunu yapmak için 32 ile çıkartıp 1.8'e bölüyoruz.
            text += f"**{i['yer']}** İçin:\n**Hava Durumu**: `{i['derece']}` - {derece}°C\n**Vakit**: `{i['gun']}`"
        await bot.send_message(
           chat_id=message.chat.id,
           text=text)
    except Exception as e:
        await bot.send_message(
            chat_id=message.chat.id,
            text=f"`{e}`")

@Bot.on_message(filters.command("start"))
async def start(bot, message):
    await bot.send_photo(
        chat_id=message.chat.id,
        photo="https://telegra.ph/file/8069ff4c3544d796c977a.jpg",
        caption="Komut 1 - /deprem <istediğin deprem sayısı>\nKomut 2 - /hava girdiğin bölgenin güncel hava durumunu gösterir.\nKomut 3 - /kurtardiklarimiz azcikta olsa içimize umut serpicek görüntüler. Kaynak: @solcugazete, @bpthaber\n\nBeni Oluşturan: @mmagneto")
    
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
    elif message.reply_to_message.video:
        rand_id = random.randint(1, 900)
        mes = await bot.send_message(message.chat.id, "`Dönüştürülüyor...`")
        await bot.download_media(
            message = message.reply_to_message,
            file_name=f"downloads/{message.chat.id}-{rand_id}.mkv")
        old_name = f"downloads/{message.chat.id}-{rand_id}.mkv"
        new_name = f"{message.chat.id}-{rand_id}.mp4"
        await video_to_gif(old_name, new_name, bot, message)
        
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
        link = unidecode(message.text).split()
        if len(link) == 1:
            sayi = 1
        else:
            sayi =  link[1]
        print(sayi)
        say = 0
        response = requests.get(url)
        data = response.json()
        bilgi = data['data']
        text = "**TÜRKİYE'DE YAŞANAN SON DEPREMLER!!!\n\n**"
        for i in bilgi:
            say += 1
            latitude1 = f"{i['enlem_n']}"
            longitude1 = f"{i['boylam_e']}"
            dadresurl = 'https://maps.google.com/maps?q=' + latitude1 + ',' + longitude1
            text += f"{say}-)\nBüyüklük: {i['ml']}\nDerinlik: {i['derinlik_km']}\nLokasyon: [{i['yer']}]({dadresurl})\nTarih: {i['tarih']} {i['saat']}\n\n"
            if say == int(sayi):
                await bot.send_message(
                    chat_id=message.chat.id, 
                    text=text) 
                return
    except Exception as e:
        print(e)
        await bot.send_message(
            chat_id=message.chat.id,
            text=f"`{e}`")

@Bot.on_message(filters.command("depremdongu"))
async def deprembilgi(bot, message):
    try:
        link = unidecode(message.text).split()
        sayi = 1
        print(sayi)
        say = 0
        response = requests.get(url)
        data = response.json()
        bilgi = data['data'][0]
        text = "**TÜRKİYE'DE YAŞANAN SON DEPREMLER!!!\n\n**"
        for i in bilgi:
            say += 1
            latitude1 = f"{i['enlem_n']}"
            longitude1 = f"{i['boylam_e']}"
            dadresurl = 'https://maps.google.com/maps?q=' + latitude1 + ',' + longitude1
            text += f"{say}-)\nBüyüklük: {i['ml']}\nDerinlik: {i['derinlik_km']}\nLokasyon: [{i['yer']}]({dadresurl})\nTarih: {i['tarih']} {i['saat']}\n\n"
            if int(say) == sayi:
                await bot.send_message(
                    chat_id="sohbetgnl2", 
                    text=text) 
                caption1 = text
                say = 0
                text = "**TÜRKİYE'DE YAŞANAN SON DEPREMLER!!!\n\n**"
                time.sleep(60)
                depremdongusu(bot, message, caption1, say)
    except Exception as e:
        print(e)
        await bot.send_message(
            chat_id=message.chat.id,
            text=f"`{e}`")

@Bot.on_message(filters.command('kurtardiklarimiz'))
async def kurtardiklarimiz(bot, message):
    kurtardıklarımızknl = "dddhhsjdheuehehehrjr"
    message_id = random.randint(2, 125)
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
