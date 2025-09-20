from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes
import os

# ⚠️ Replace with your new token from BotFather
BOT_TOKEN = os.getenv("BOT_TOKEN", "YOUR_NEW_BOT_TOKEN")

# Hosted URL of your HTML game (GitHub Pages or other host)
GAME_URL = "https://your-username.github.io/telegram-truth-dare/game.html"

# /start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Create a button that opens the game inside Telegram
    keyboard = [
        [KeyboardButton("🎮 Play Truth or Dare", web_app=WebAppInfo(url=GAME_URL))]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "Welcome! Tap below to start the Truth or Dare game 🎲",
        reply_markup=reply_markup
    )

if __name__ == "__main__":
    # Create the bot application
    app = Application.builder().token(BOT_TOKEN).build()
    
    # Add command handler
    app.add_handler(CommandHandler("start", start))
    
    print("✅ Bot is running...")
    app.run_polling()
