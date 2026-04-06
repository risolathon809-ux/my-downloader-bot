import os
import yt_dlp
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

async def download_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text
    if "http" not in url: return
    status_msg = await update.message.reply_text("⏳ Yuklanmoqda...")
    file_name = f"vid_{update.effective_chat.id}.mp4"
    ydl_opts = {'format': 'best[ext=mp4]/best', 'outtmpl': file_name, 'quiet': True}
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            await asyncio.to_thread(ydl.download, [url])
        await update.message.reply_video(video=open(file_name, 'rb'), caption="✅ Tayyor!")
        os.remove(file_name)
    except:
        await update.message.reply_text("❌ Xatolik yuz berdi.")
    await status_msg.delete()

if __name__ == '__main__':
    app = ApplicationBuilder().token("8780583094:AAFBxylTo_kzK0qUPF-U9XXyr28ifz85r5w").build()
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), download_video))
    app.run_polling()
