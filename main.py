# by @Mr_AliMorradi, @Sigaris
# https://t.me/PiniGerTeam
from telethon.sync import TelegramClient, events
import os
api_id, api_hash = input('Enter your api_id: '), input('Enter your api_hash: ')
bot = TelegramClient('SecretBot', api_id, api_hash).start()

@bot.on(events.NewMessage(pattern=r'(بصبر دان بشه|بصبر دان شه|بصب دان شه|بصب دان بشه)', func=lambda e: e.is_reply))
async def show_image(event):
    userid = await bot.get_me()
    if event.sender_id == userid.id:
        try:
            message = await event.get_reply_message()
            download = await bot.download_media(message)
            await bot.send_message('me', f'عکس نابود شونده از مرحوم 😂😂', file=download)
            os.remove(download)
        except Exception as e:
            await bot.send_message('me', f"خطایی دریافت شد:\n\n{e}")

bot.run_until_disconnected()