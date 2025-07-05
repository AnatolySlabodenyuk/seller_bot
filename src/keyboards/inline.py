from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def fabric_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Брезент (500 ₽/м²)", callback_data="fabric_Брезент"),
            InlineKeyboardButton(text="Оксфорд (450 ₽/м²)", callback_data="fabric_Оксфорд")
        ]
    ])


def zipper_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Без молнии", callback_data="zipper_0")],
        [InlineKeyboardButton(text="1 молния по центру", callback_data="zipper_1")],
        [InlineKeyboardButton(text="2 молнии по бокам", callback_data="zipper_2")]
    ])


def restart_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Рассчитать ещё одну штору", callback_data="restart")]
    ])
