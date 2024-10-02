#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href='tg://user?id={OWNER_ID}'>ᏰᎧᎧᏦᏇᎧᏒᎷ</a>\n○ ʙᴏᴛ ᴠᴇʀꜱɪᴏɴ : <a href='https://t.me/infohub_updates'>ᴠ.2.8.1</a>\n○ ᴅᴀᴛᴀʙᴀꜱᴇ : <a href='https://www.mongodb.com/'>ᴍᴏɴɢᴏ-ᴅʙ</a>\n○ ᴏᴜʀ ᴄᴏᴍᴍᴜɴɪᴛʏ : <a href='https://t.me/InfoHub_Hall'>ɪɴꜰᴏʜᴜʙ ᴄᴏᴍᴍᴜɴɪᴛʏ ʜᴀʟʟ</a>\n○ ᴄᴀꜱᴜᴀʟ ᴄʜᴀᴛ : <a href='https://t.me/chat_vc_gossip_fun_friendship'>𝕯𝖊𝖛𝖎𝖑'𝖘 𝕯𝖊𝖓</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton('✇ ᴜᴘᴅᴀᴛᴇꜱ 〄', url='https://t.me/infohub_updates'),
                    InlineKeyboardButton('〄 Qᴜᴏᴛᴇꜱ ✇', url='https://t.me/Motivation_Inspiration_Quote')
                    ],[
                        InlineKeyboardButton('✇ ᴀᴅᴍɪɴꜱ 〄', url='https://t.me/infohubsupport_robot'),
                        InlineKeyboardButton('✪ ꜱᴜᴘᴘᴏʀᴛ ⌬', url='https://t.me/Infohub_Tech')
                    ],[
                        InlineKeyboardButton("✪ ᴄʟᴏsᴇ ⌬", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
