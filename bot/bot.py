import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

# from сonfig.py file 
from config import settings  

# from keyboards.py
from keyboards import main_menu, back_menu  

# Setup
logging.basicConfig(level=logging.INFO)

bot = Bot(token=settings.BOT_TOKEN)

dp = Dispatcher()

# /start command
@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "👋 Welcome to Stocki DeFi AI Bot — we’re still developing!\n\nChoose an option below:",
        reply_markup=main_menu()
    )

# About callback
@dp.callback_query(F.data == "about")
async def about(callback: CallbackQuery):
    about_text = (
        "🤖 *Stocki DeFi AI* is currently in development — but you can already purchase early access by contacting our admin\\.\n\n"
        "Stocki is built to help you succeed in DeFi\\. Our AI Agent finds real opportunities, "
        "enhances your trading decisions, and connects you with like\\-minded people — all in one place\\.\n\n"
        "It’s more than a tool — it’s your personal AI assistant that listens to what you need and gets things done for you\\. "
        "Whether you're exploring DeFi for the first time or looking to gain an edge, Stocki is here to help you grow\\."
    )

    await callback.message.edit_text(
        text=about_text,
        reply_markup=back_menu(),  # Make sure this function call
        parse_mode="MarkdownV2"
    )
    await callback.answer()

# Channel callback
@dp.callback_query(F.data == "channel")
async def channel(callback: CallbackQuery):
    await callback.message.edit_text(
        f"🪐 Check out Stocki DeFi channel for updates: {settings.REVIEWS_CHANNEL_LINK}",
        reply_markup=back_menu()
    )
    await callback.answer()

# Access callback
@dp.callback_query(F.data == "access")
async def access(callback: CallbackQuery):
    await callback.message.edit_text(
        f"🏄‍♂️ Want to get early access to your private chat with Stocki? \n\nContact our admin for more info: {settings.ADMIN_USERNAME}",
        reply_markup=back_menu()
    )
    await callback.answer()

# Back to main menu
@dp.callback_query(F.data == "back_menu")
async def back(callback: CallbackQuery):
    await callback.message.edit_text(
        "👋 Back to menu. Choose an option:",
        reply_markup=main_menu()
    )
    await callback.answer()

# Run the bot
async def main():
    logging.info("Starting Stocki DeFi bot...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
