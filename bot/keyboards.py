from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
# Passing a List as an Argument to send any data types of argument to a function (string, number, list, dictionary etc.),
# and it will be treated as the same data type inside the function.

# language option for start section

def language_menu():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="🇺🇸 English", callback_data="lang_en"),
            InlineKeyboardButton(text="🇷🇺 Русский", callback_data="lang_ru"),
        ]
    ])
    return keyboard

# main menu function 
def main_menu(lang="en"):
    if lang == "ru":
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[                
                [InlineKeyboardButton(text="🌌 О чем этот бот?", callback_data="about")],
                [InlineKeyboardButton(text="🚨 Ранний доступ к Stocki", callback_data="access")],
                [InlineKeyboardButton(text="📢 Telegram Канал", url="https://t.me/StockiDeFi")],
                [
                    InlineKeyboardButton(text="📞 Связь с командой", callback_data="contact"),
                    InlineKeyboardButton(text="🔗 Официальные ссылки", callback_data="links")
                ]
            ]
       )
    else:
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="🌌 What is this bot about?", callback_data="about")],
                [InlineKeyboardButton(text="🚨 Early Access to Stocki", callback_data="access")], 
                [InlineKeyboardButton(text="📢 Telegram Channel", url="https://t.me/StockiDeFi")],
                [
                    InlineKeyboardButton(text="📞 Contact the team", callback_data="contact"),
                    InlineKeyboardButton(text="🔗 Official Links", callback_data="links"),
                ]
            ]
        )
    
    return keyboard

# links menu for urls with all channels
def channels_menu(lang="en"):
                if lang == "ru":
                      keyboard = InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="💭 Открытый Чат", url="https://t.me/stocki_defiChat")],
                                [InlineKeyboardButton(text="🔴▶️ YouTube", url="https://www.youtube.com/@StockiDeFi")],
                                [InlineKeyboardButton(text="📖 Teletype Блог", url="https://teletype.in/@mak_sjr")],
                                [InlineKeyboardButton(text="⬅️ Назад", callback_data="back")]
                            ]
                        )
                else:
                      keyboard = InlineKeyboardMarkup(
                            inline_keyboard=[
                                  [InlineKeyboardButton(text="💭 Public Chat", url="https://t.me/stocki_defiChat")],
                                  [InlineKeyboardButton(text="🔴▶️ Youtube", url="https://www.youtube.com/")],
                                  [InlineKeyboardButton(text="📖 Teletype Blog", url="https://teletype.in/@mak_sjr")], 
                                  [InlineKeyboardButton(text="⬅️ Back", callback_data="back")]
                            ]
                      )
                return keyboard  

# back menu for return to main menu function 
def back_menu(lang="en"):
    if lang == "en":
        text = "🔙 Back to menu"
    elif lang == "ru":
        text = "🔙 Назад в меню" 
    return InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text=text, callback_data="back_menu")]]
    )