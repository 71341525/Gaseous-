from pyrogram import filters
from pyrogram.types import Message

from ArStringTep import Anony
from ArStringTep.utils import add_served_user, keyboard


@Anony.on_message(filters.command("start") & filters.private & filters.incoming)
async def f_start(_, message: Message):
    await message.reply_text(
        text=f"<b>✦ مرحبًــا  👋</b> {message.from_user.first_name},\n<b>هذا هو</b>  {Anony.mention},\n<b>✦ يمكنـك استخـدامي لـ استخـراج كـود الجلسـة لـ تنصيـب  ردثـون اضغط بدء استخراج الجلسة وابدأ بالاستخراج ✨</b>\n<b>✦ ملاحظـات هامـة</b> : \n1. لا تشارك كود الجلسة لأحد \n2. عند وصولك الكود ضع بين كل رقم ورقم فراغ مثال : 1 2 3 4",
        reply_markup=keyboard,
        disable_web_page_preview=True,
    )
    await add_served_user(message.from_user.id)
