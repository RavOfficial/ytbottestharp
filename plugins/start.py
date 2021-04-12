import os
import asyncio
from urllib.parse import urlparse
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from youtube_dl import YoutubeDL
from opencc import OpenCC
from config import Config


@BellaYT.on_message(filters.command("start"))
async def start(client, message):
   if message.chat.type == 'private':
       await Jebot.send_message(
               chat_id=message.chat.id,
               text="""<b>Youtube Downloader Bot Help!
Just send a Youtube url to download it in video or audio format!
If you have any question?
Report us [here!](https://t.me/HARP_Chat)
Another bot by [HARP Tech 🇱🇰](https://t.me/Tech)
Join now with us @HARP_Tech 🇱🇰 </b>""",   
                            reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "Help ❔", callback_data="help"),
                                        InlineKeyboardButton(
                                            "Channel", url="https://t.me/HARP_Tech")
                                    ],[
                                      InlineKeyboardButton(
                                            "Group", url="https://t.me/HARP_Chat")
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")

@BellaYT.on_message(filters.command("help"))
async def help(client, message):
    if message.chat.type == 'private':   
        await BellaYT.send_message(
               chat_id=message.chat.id,
               text="""<b>Youtube Downloader Bot Help!
Just send a Youtube url to download it in video or audio format!
If you have any question?
Report us [here!](https://t.me/HARP_Chat)
Another bot by [HARP Tech 🇱🇰](https://t.me/HARP_Tech)
Join now with us @HARP_Chat 🇱🇰 </b>""",
        reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "Back", callback_data="start"),
                                        InlineKeyboardButton(
                                            "About", callback_data="about"),
                                  ],[
                                        InlineKeyboardButton(
                                            "Join now! 🇱🇰 ", url="https://t.me/HARP_Tech")
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")

@BellaYT.on_message(filters.command("about"))
async def about(client, message):
    if message.chat.type == 'private':   
        await Jebot.send_message(
               chat_id=message.chat.id,
               text="""<b>About Youtube Downloader Bot!</b>
<b>Creator:</b> <a href="https://t.me/HARP_Tech">HARP Tech 🇱🇰</a>
<b>Get a help by contacting us:</b> <a href="https://t.me/HARP_Chat">HARP Tech's official support group</a>
<b>Join now with us @HARP_Chat 🇱🇰</b>""",
     reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "Back", callback_data="help"),
                                        InlineKeyboardButton(
                                            "Join now! 🇱🇰 ", url="https://t.me/HARP_Tech")
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")
