from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import SUPPORT_CHAT


keyboard = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton(text="- بـدء استخـراج الجلسـة .", callback_data="getsession")],
        [
            InlineKeyboardButton(text="- قنـاة الشـروحـات .", url=SUPPORT_CHAT),
            InlineKeyboardButton(
                text="- قنـاة السـورس .", url="https://t.me/A0R01"
            ),
        ],
    ]
)

string_key = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="بايـروجـرام", callback_data="pyrogram1"),
            InlineKeyboardButton(text="بايـروجرام v2", callback_data="pyrogram"),
        ],
        [InlineKeyboardButton(text="تليثـون", callback_data="telethon")],
    ]
)

retry_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="إعـادة المحاولـة .", callback_data="getsession")]]
)
