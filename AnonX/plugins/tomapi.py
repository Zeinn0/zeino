import asyncio
import os
from pyrogram.types import CallbackQuery
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app
import requests
import pyrogram
from pyrogram import Client, emoji 
from config import *
from pyrogram import filters
from strings.filters import command
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.errors import MessageNotModified



@app.on_message(
    filters.command("sezar")
    
)
async def cr_source(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/8ce74a37ac194b0cb943f.jpg",
        caption=f"""**⩹━★⊷━⌞ ᥉ًٰٖ᥆ُᥙٰٓᖇٰᥴٍᥱٍُٰ ᥉ُِٰᥱُْٰᤁُᥲُِᖇٖ ⌝━⊶★━⩺**\nمرحبا بك عزيزي {message.from_user.mention}\nانا بوت الذكاء الاصطناعي الخاص بسورس cr \nلمعرفة الاوامر اضغط على الأزرار بالأسفل👇\n**⩹━★⊷━⌞ ᥉ًٰٖ᥆ُᥙٰٓᖇٰᥴٍᥱٍُٰ ᥉ُِٰᥱُْٰᤁُᥲُِᖇٖ ⌝━⊶★━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "طريقة الإستخدام", callback_data="usage"), 
                 ],[
                    InlineKeyboardButton(
                        "⧛ 𝖕𝖔𝖐𝖊𝖒𝖔𝖓 ׀ 𝗝َ َ𝗢َ ٍ𝗞َ〡مّـمٌَــ ـؤِلًُ ⧚ ❲𝙫𝙞𝙥❳", url=f"https://t.me/devpokemon"),
                    InlineKeyboardButton(
                        "⧛ َ𝗝َ َ𝗢َ ٍ𝗞َ ׀ مــ ـٰٖمـوِٰلٰ ׀ جـِوڪَ ׀ ⧚", url=f"https://t.me/G_O_OZ"),
                ],[
                
                    InlineKeyboardButton(
                        "★⌞ ᥉ًٰٖ᥆ُᥙٰٓᖇٰᥴٍᥱٍُٰ ᥉ُِٰᥱُْٰᤁُᥲُِᖇٖ ⌝⚡", url=f"https://t.me/UIU_II"),
                ],

            ]

        ),

    )

    
@app.on_callback_query(filters.regex("usage"))
async def cr_usage(_, callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text(
        text="""**⩹━★⊷⌯⌞ ᥉ًٰٖ᥆ُᥙٰٓᖇٰᥴٍᥱٍُٰ ᥉ُِٰᥱُْٰᤁُᥲُِᖇٖ ⌝⌯⊶★━⩺**
★¦ اهلا بك عزيزي في قسم الأوامر
★¦ لتتمكن من تشغيل الذكاء الاصطناعي فقط اكتب
★¦ /gpt - لـلـسـؤال آي سـؤال بالـذكـاء الاسـطـناعي

**⩹━★⊷⌯⌞ ᥉ًٰٖ᥆ُᥙٰٓᖇٰᥴٍᥱٍُٰ ᥉ُِٰᥱُْٰᤁُᥲُِᖇٖ ⌝⌯⊶★━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "العودة", callback_data="back"), 
                ]
            ]
        )
    )

    
@app.on_callback_query(filters.regex("back"))
async def cr_back(_, callback_query: CallbackQuery):
    message = callback_query.message
  
    await message.edit_reply_markup(reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("طريقة الإستخدام", callback_data="tommm")],
            [InlineKeyboardButton("⧛ 𝖕𝖔𝖐𝖊𝖒𝖔𝖓 ׀ 𝗝َ َ𝗢َ ٍ𝗞َ〡مّـمٌَــ ـؤِلًُ ⧚ ❲𝙫𝙞𝙥❳", url=f"https://t.me/devpokemon"),
             InlineKeyboardButton("⧛ َ𝗝َ َ𝗢َ ٍ𝗞َ ׀ مــ ـٰٖمـوِٰلٰ ׀ جـِوڪَ ׀ ⧚", url=f"https://t.me/G_O_OZ")],
            [InlineKeyboardButton("★⌞ ᥉ًٰٖ᥆ُᥙٰٓᖇٰᥴٍᥱٍُٰ ᥉ُِٰᥱُْٰᤁُᥲُِᖇٖ ⌝⚡", url=f"https://t.me/UIU_II")],
        ]
    ))

