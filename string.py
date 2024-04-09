import asyncio

from pyrogram import Client, filters
from oldpyro import Client as Client1
from oldpyro.errors import ApiIdInvalid as ApiIdInvalid1
from oldpyro.errors import PasswordHashInvalid as PasswordHashInvalid1
from oldpyro.errors import PhoneCodeExpired as PhoneCodeExpired1
from oldpyro.errors import PhoneCodeInvalid as PhoneCodeInvalid1
from oldpyro.errors import PhoneNumberInvalid as PhoneNumberInvalid1
from oldpyro.errors import SessionPasswordNeeded as SessionPasswordNeeded1
from pyrogram.errors import (
    ApiIdInvalid,
    FloodWait,
    PasswordHashInvalid,
    PhoneCodeExpired,
    PhoneCodeInvalid,
    PhoneNumberInvalid,
    SessionPasswordNeeded,
)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from telethon import TelegramClient
from telethon.errors import (
    ApiIdInvalidError,
    PasswordHashInvalidError,
    PhoneCodeExpiredError,
    PhoneCodeInvalidError,
    PhoneNumberInvalidError,
    SessionPasswordNeededError,
)
from telethon.sessions import StringSession
from telethon.tl.functions.channels import JoinChannelRequest
from pyromod.listen.listen import ListenerTimeout

from config import SUPPORT_CHAT
from ArStringTep import Anony
from ArStringTep.utils import retry_key


async def string_session(
    message, user_id: int, telethon: bool = False, old_pyro: bool = False
):
    if telethon:
        ty = f"✦ تليثـون"
    elif old_pyro:
        ty = f"✦ بايروجـرام"
    else:
        ty = f"✦ بايروجـرام v2"

    await message.reply_text(f"<b>✦ محاولة بدء {ty} استخراج الجلسة</b>..")

    try:
        api_id = await Anony.ask(
            identifier=(message.chat.id, user_id, None),
            text="<b>✦ يرجـى إرسـال الأيبـي أيدي الخـاص بـك .</b>",
            filters=filters.text,
            timeout=300,
        )
    except ListenerTimeout:
        return await Anony.send_message(
            user_id,
            "<b>✦ انقضــت مـدة استخراج الجلسـة ⌛.</b>\n\nمن فضلك ابدأ في إنشاء الجلسة مرة أخرى.",
            reply_markup=retry_key,
        )

    if await cancelled(api_id):
        return

    try:
        api_id = int(api_id.text)
    except ValueError:
        return await Anony.send_message(
            user_id,
            "<b>✦ الأيبي أيدي الذي أرسلتـه غير صالح</b>\n\nمن فضـلك ابدأ في إنشاء الجلسة مرة أخرى*.",
            reply_markup=retry_key,
        )

    try:
        api_hash = await Anony.ask(
            identifier=(message.chat.id, user_id, None),
            text="<b>✦ يرجـى إرسـال الأيبـي هـاش الخـاص بـك .</b>",
            filters=filters.text,
            timeout=300,
        )
    except ListenerTimeout:
        return await Anony.send_message(
            user_id,
            "<b>✦ انقضـت مدة استخـراج الجلسـة</b>.\n\nمن فضـلك ابدأ في إنشاء الجلسة مرة أخرى.",
            reply_markup=retry_key,
        )

    if await cancelled(api_hash):
        return

    api_hash = api_hash.text

    if len(api_hash) < 30:
        return await Anony.send_message(
            user_id,
            "<b>✦ الأيبي هـاش الذي أرسلته غير صالح</b>\n\nمن فضـلك ابدأ في إنشاء الجلسة مرة أخرى .",
            reply_markup=retry_key,
        )

    try:
        phone_number = await Anony.ask(
            identifier=(message.chat.id, user_id, None),
            text="<b>✦ 📞 الرجـاء إرسـال رقـم هاتفـك</b>\n<b>مثال : +97075532342</b>",
            filters=filters.text,
            timeout=300,
        )
    except ListenerTimeout:
        return await Anony.send_message(
            user_id,
            "» تم الوصول إلى الحد الزمني وهو 5 دقائق.\n\nمن فضـلك ابدأ في إنشاء الجلسة مرة أخرى.",
            reply_markup=retry_key,
        )

    if await cancelled(phone_number):
        return
    phone_number = phone_number.text

    await Anony.send_message(user_id, "<b>✦ جـاري إرسـال الكـود ✉.....</b>")
    if telethon:
        client = TelegramClient(StringSession(), api_id, api_hash)
    elif old_pyro:
        client = Client1(":memory:", api_id=api_id, api_hash=api_hash)
    else:
        client = Client(name="Anony", api_id=api_id, api_hash=api_hash, in_memory=True)
    await client.connect()

    try:
        if telethon:
            code = await client.send_code_request(phone_number)
        else:
            code = await client.send_code(phone_number)
        await asyncio.sleep(1)

    except FloodWait as f:
        return await Anony.send_message(
            user_id,
            f"<b>✦ فشل في إرسال الرمز أو تسجيل الدخول</b>\n\nمن فضلك انتظر {f.value or f.x} ثانية وحاول مرة أخرى.",
            reply_markup=retry_key,
        )
    except (ApiIdInvalid, ApiIdInvalidError, ApiIdInvalid1):
        return await Anony.send_message(
            user_id,
            "» الأيبي أيـدي أو الأيبي هـاش غير صالح.\n\nمن فضـلك ابدأ في إنشاء الجلسة مرة أخرى.",
            reply_markup=retry_key,
        )
    except (PhoneNumberInvalid, PhoneNumberInvalidError, PhoneNumberInvalid1):
        return await Anony.send_message(
            user_id,
            "✦ رقم الهاتـف غير صالح.\n\nمن فضـلك ابدأ في إنشاء الجلسة مرة أخرى.",
            reply_markup=retry_key,
        )

    try:
        otp = await Anony.ask(
            identifier=(message.chat.id, user_id, None),
            text=f"<b>✦ يرجـى إرسـال الكـود الذي وصـلك</b> {phone_number}.\n\nإذا كان الرمز هو <code>12345</code>, يرجى إرساله مثـل <code>1 2 3 4 5.</code>",
            filters=filters.text,
            timeout=600,
        )
        if await cancelled(otp):
            return
    except ListenerTimeout:
        return await Anony.send_message(
            user_id,
            "» وصل الحد الزمني إلى 10 دقائق.\n\nمن فضـلك ابدأ في إنشاء الجلسة مرة أخرى.",
            reply_markup=retry_key,
        )

    otp = otp.text.replace(" ", "")
    try:
        if telethon:
            await client.sign_in(phone_number, otp, password=None)
        else:
            await client.sign_in(phone_number, code.phone_code_hash, otp)
    except (PhoneCodeInvalid, PhoneCodeInvalidError, PhoneCodeInvalid1):
        return await Anony.send_message(
            user_id,
            "» الكود الذي أرسلته هو <b>خطأ.</b>\n\nمن فضـلك ابدأ في إنشاء الجلسة مرة أخرى.",
            reply_markup=retry_key,
        )
    except (PhoneCodeExpired, PhoneCodeExpiredError, PhoneCodeExpired1):
        return await Anony.send_message(
            user_id,
            "» الكود الذي أرسلته <b>منتهي.</b>\n\nمن فضـلك ابدأ في إنشاء الجلسة مرة أخرى.",
            reply_markup=retry_key,
        )
    except (SessionPasswordNeeded, SessionPasswordNeededError, SessionPasswordNeeded1):
        try:
            pwd = await Anony.ask(
                identifier=(message.chat.id, user_id, None),
                text="<b>✦ يرجـى إرسـال التحـقق بخطوتين الخـاص بـك .</b>",
                filters=filters.text,
                timeout=300,
            )
        except ListenerTimeout:
            return Anony.send_message(
                user_id,
                "<b>✦  ⌛ تم الوصول إلى الحد الزمني لمدة 5 دقائق</b>\n\nمن فضـلك ابدأ في إنشاء الجلسة مرة أخرى.",
                reply_markup=retry_key,
            )

        if await cancelled(pwd):
            return
        pwd = pwd.text

        try:
            if telethon:
                await client.sign_in(password=pwd)
            else:
                await client.check_password(password=pwd)
        except (PasswordHashInvalid, PasswordHashInvalidError, PasswordHashInvalid1):
            return await Anony.send_message(
                user_id,
                "<b>✦ كلمة المـرور التي أرسلتها خاطئة</b>\n\nمن فضـلك ابدأ في إنشاء الجلسة مرة أخرى.",
                reply_markup=retry_key,
            )

    except Exception as ex:
        return await Anony.send_message(user_id, f"خطـأ : <code>{str(ex)}</code>")

    try:
        txt = "الخاص بك هنا {0} ✦ كود الجلسـة\n\n<code>{1}</code>\n\nᴀ مستخرج من<a href={2}>@A0R01</a>\n! <b>ملاحظـة :</b> لا تشارك كود الجلسة لأحد لأنه يستطيع اختراق حسابـك."
        if telethon:
            string_session = client.session.save()
            await client.send_message(
                "me",
                txt.format(ty, string_session, SUPPORT_CHAT),
                link_preview=False,
                parse_mode="html",
            )
            await client(JoinChannelRequest("@A0R01"))
        else:
            string_session = await client.export_session_string()
            await client.send_message(
                "me",
                txt.format(ty, string_session, SUPPORT_CHAT),
                disable_web_page_preview=True,
            )
            await client.join_chat("A0R01")
    except KeyError:
        pass
    try:
        await client.disconnect()
        await Anony.send_message(
            chat_id=user_id,
            text=f"تم استخراج الخاص بـك {ty} كود الجلسـة.\n\nيرجى تفقد الرسائل المحفوظة.\n\nᴀ من <a href={SUPPORT_CHAT}>!</a>.",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text=" ✉ الرسائل المحفوظـة",
                            url=f"tg://openmessage?user_id={user_id}",
                        )
                    ]
                ]
            ),
            disable_web_page_preview=True,
        )
    except:
        pass


async def cancelled(message):
    if "/cancel" in message.text:
        await message.reply_text(
            "✦ تم إلغاء استخراج الجلسة.", reply_markup=retry_key
        )
        return True
    elif "/restart" in message.text:
        await message.reply_text(
            "✦ تم الترسيـت .", reply_markup=retry_key
        )
        return True
    elif message.text.startswith("/"):
        await message.reply_text(
            "✦ تم إلغاء استخراج الجلسـة.", reply_markup=retry_key
        )
        return True
    else:
        return False
#تعريب_@PPF22