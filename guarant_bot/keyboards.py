from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def games_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Mobile Legends", callback_data="ml")],
        [InlineKeyboardButton(text="PUBG", callback_data="pubg")],
        [InlineKeyboardButton(text="Free Fire", callback_data="ff")],
        [InlineKeyboardButton(text="Steam", callback_data="steam")],
        [InlineKeyboardButton(text="Supercell", callback_data="sc")],
    ])

def confirm_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="✅ Создать сделку", callback_data="yes")],
        [InlineKeyboardButton(text="❌ Отмена", callback_data="no")],
    ])
