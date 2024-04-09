from pyrogram import filters
from pyrogram.types import CallbackQuery

from ArStringTep import Anony
from ArStringTep.utils import string_key
from ArStringTep.modules.string import string_session


@Anony.on_callback_query(
    filters.regex(pattern=r"^(getsession|pyrogram|pyrogram1|telethon)$")
)
async def cb_choose(_, cq: CallbackQuery):
    await cq.answer()
    query = cq.matches[0].group(1)
    if query == "getsession":
        return await cq.message.reply_text(
            text="<b>» اختـر الجلسـة التـي تريـد استخـراجها :</b>",
            reply_markup=string_key,
        )
    elif query.startswith("pyrogram") or query.startswith("telethon"):
        try:
            if query == "pyrogram":
                await string_session(cq.message, cq.from_user.id)
            elif query == "pyrogram1":
                await string_session(cq.message, cq.from_user.id, old_pyro=True)
            elif query == "telethon":
                await string_session(cq.message, cq.from_user.id, telethon=True)
        except Exception as e:
            await cq.edit_message_text(e, disable_web_page_preview=True)
