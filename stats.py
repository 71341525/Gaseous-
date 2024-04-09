from pyrogram import filters
from pyrogram.types import Message

from config import OWNER_ID
from ArStringTep import Anony
from ArStringTep.utils import get_served_users


@Anony.on_message(filters.command(["stats", "users"]) & filters.user(OWNER_ID))
async def get_stats(_, message: Message):
    users = len(await get_served_users())
    await message.reply_text(f"» الإحصائيات الحالية ل {Anony.name} :\n\n {users} المستخدميـن")
