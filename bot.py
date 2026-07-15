from telegram import Update
from telegram.ext import Application, MessageHandler, filters

BOT_TOKEN = "6587062245:AAFsbuycIGMWpYKF-eXUZHqXuJsqnCKdcKc"
FRIEND_CHAT_ID = "8781939113"

async def handle_message(update, context):
    chat_id = update.effective_chat.id
    if int(FRIEND_CHAT_ID) != chat_id:
        text = update.message.text
        sender = update.effective_user.first_name
        await context.bot.send_message(
            chat_id=FRIEND_CHAT_ID,
            text=f"📨 From {sender}: {text}"
        )

app = Application.builder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT, handle_message))
print("Bot running! Forwarding messages to @foreverpaidpal...")
app.run_polling()
