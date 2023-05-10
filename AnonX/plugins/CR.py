import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app
from random import  choice, randint

                
@app.on_message(
    command(["مطورين سي ار","المطورين","مطورين","مطورين sezar"])
    & ~filters.edited
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/8ce74a37ac194b0cb943f.jpg",
        caption=f"""**⩹━★⊷━⌞ ᥉᥆ᥙᖇᥴᥱ ᥉ᥱᤁᥲᖇ ⌝━⊶★━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم مطورين sezar ميوزك\nللتحدث مع مطورين اضغط علي الازرار بالاسفل👇\n**⩹━★⊷━⌞ ᥉᥆ᥙᖇᥴᥱ ᥉ᥱᤁᥲᖇ ⌝━⊶★━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒⧛ 𝖕𝖔𝖐𝖊𝖒𝖔𝖓 ׀ 𝗝َ َ𝗢َ ٍ𝗞َ〡مّـمٌَــ ـؤِلًُ ⧚ ❲𝙫𝙞𝙥❳ ", url=f"https://t.me/devpokemon"), 
                 ],[
                    InlineKeyboardButton(
                        "ρ᥆kᥱꪔ᥆ꪀ", url=f"https://t.me/devpokemon"),
                ],[
                    InlineKeyboardButton(
                        "𝐶𝑅𝐼𝑆𝑇𝐼𝑁", url=f"https://t.me/dr_sezariss"),
                    InlineKeyboardButton(
                        "ꪔᥲ️ꪀ᥆᥆", url=f"https://t.me/C1_I_I"),
                ],[
                
                    InlineKeyboardButton(
                        "★⌞ ᥉᥆ᥙᖇᥴᥱ ᥉ᥱᤁᥲᖇ ⌝⚡", url=f"https://t.me/UIU_II"),
                ],

            ]

        ),

    )








@app.on_message(
    command(["جوك المطور","الجوك","جوك","مبرمج","jok","el jok"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("devpokemon")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞ ᥉᥆ᥙᖇᥴᥱ ᥉ᥱᤁᥲᖇ ⌝━⊶★━⩺\n\n‍ ¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\n**⩹━★⊷━⌞ ᥉᥆ᥙᖇᥴᥱ ᥉ᥱᤁᥲᖇ ⌝━⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )


@app.on_message(
    command(["زين المطور","زين","زين","بوكمان","pokmon","pokman"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("devpokemon")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞ ᥉᥆ᥙᖇᥴᥱ ᥉ᥱᤁᥲᖇ ⌝━⊶★━⩺\n\n¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\n**⩹━★⊷━⌞ ᥉᥆ᥙᖇᥴᥱ ᥉ᥱᤁᥲᖇ ⌝━⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )


@app.on_message(
    command(["كريستين المطور","كريستين","كرستين","الدكتوره","sezaristin","كرستينه"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("dr_sezariss")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞ ᥉᥆ᥙᖇᥴᥱ ᥉ᥱᤁᥲᖇ ⌝━⊶★━⩺\n\n‍ ¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\n**⩹━★⊷━⌞ ᥉᥆ᥙᖇᥴᥱ ᥉ᥱᤁᥲᖇ ⌝━⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )
    

@app.on_message(
    command(["مانو المطور","مانو","الممول","mano","Mano"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("C1_I_I")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞ ᥉᥆ᥙᖇᥴᥱ ᥉ᥱᤁᥲᖇ ⌝━⊶★━⩺\n\n ¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\n**⩹━★⊷━⌞ ᥉᥆ᥙᖇᥴᥱ ᥉ᥱᤁᥲᖇ ⌝━⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )
    


@app.on_message(
    command(["/api"])
    & ~filters.edited
    
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/8ce74a37ac194b0cb943f.jpg",
        caption=f"""**⩹⊷━⌞ ᥉᥆ᥙᖇᥴᥱ ᥉ᥱᤁᥲᖇ ⌝━━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم الذكاء الاصتناعي الخاص بسورس sezar\nلتتمكن من استخدام اوامر الذكاء الاصتناعي اكتب \n /gpt + السؤال بالاسفل👇\n**⩹━━⌞ ᥉᥆ᥙᖇᥴᥱ ᥉ᥱᤁᥲᖇ ⌝━━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒⧛ 𝖕𝖔𝖐𝖊𝖒𝖔𝖓 ׀ 𝗝َ َ𝗢َ ٍ𝗞َ〡مّـمٌَــ ـؤِلًُ ⧚ ❲𝙫𝙞𝙥❳", url=f"https://t.me/devpokemon"), 
                 ],[
                
                    InlineKeyboardButton(
                        "★⌞ ᥉᥆ᥙᖇᥴᥱ ᥉ᥱᤁᥲᖇ ⌝⚡", url=f"https://t.me/UIU_II"),
                ],

            ]

        ),

    )



@app.on_message(
    command(["قرأن"])
    & ~filters.edited
    
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/8ce74a37ac194b0cb943f.jpg",
        caption=f"""**⩹⊷━⌞ ᥉᥆ᥙᖇᥴᥱ ᥉ᥱᤁᥲᖇ ⌝━━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم تشغيل القرأن الخاص بسورس sezar\nلتتمكن من استخدام اوامر القرأن اكتب \n سورة + اسم السورة بالاسفل👇\n**⩹━━⌞ ᥉᥆ᥙᖇᥴᥱ ᥉ᥱᤁᥲᖇ ⌝━━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒⧛ 𝖕𝖔𝖐𝖊𝖒𝖔𝖓 ׀ 𝗝َ َ𝗢َ ٍ𝗞َ〡مّـمٌَــ ـؤِلًُ ⧚ ❲𝙫𝙞𝙥❳", url=f"https://t.me/devpokemon"), 
                 ],[
                
                    InlineKeyboardButton(
                        "★⌞ ᥉᥆ᥙᖇᥴᥱ ᥉ᥱᤁᥲᖇ ⌝⚡", url=f"https://t.me/UIU_II"),
                ],

            ]

        ),

    )



    
