from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Passing a List as an Argument to send any data types of argument to a function (string, number, list, dictionary etc.),
# and it will be treated as the same data type inside the function.

# main menu function 

def main_menu():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🌌 What is this bot about?", callback_data="about")],
            [InlineKeyboardButton(text="🏄‍♂️ Open Channel Link to Stocki DeFi", callback_data="channel")],
            [InlineKeyboardButton(text="👩‍🚀 Early access to private chat with Stocki Agent ", callback_data="access")]
        ]
    )
    return keyboard

# back menu for return to main menu function 

def back_menu():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🔙 Back to Menu", callback_data="back_menu")]
        ]
    )
    return keyboard
