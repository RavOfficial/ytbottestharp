from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt ="""<b>About Youtube Downloader Bot!</b>
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
    await message.reply_text(helptxt)
