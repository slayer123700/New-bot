import os
from datetime import datetime, timedelta, timezone

from PIL import Image, ImageDraw, ImageFont
from pyrogram import enums, filters
from pyrogram.types import (
    Message, ChatMemberUpdated,
    InlineKeyboardMarkup, InlineKeyboardButton
)

from AnieXEricaMusic import app

# ─────────────────────────────
# CONFIG
# ─────────────────────────────
FONT_PATH    = "AnieXEricaMusic/assets/annie/ArialReg.ttf"
BTN_VIEW     = "๏ ᴠɪᴇᴡ ɴᴇᴡ ᴍᴇᴍʙᴇʀ ๏"
BTN_ADD      = "๏ ᴋɪᴅɴᴀᴘ ᴍᴇ ๏"

CAPTION_TXT = """
ʜᴇʏ ᴡᴇʟᴄᴏᴍᴇ To {chat_title} ᴛᴏ ʜᴏᴘᴇ ʏᴏᴜ ᴡɪʟʟ ʜᴀᴅ ᴀ ɢᴏᴏᴅ ᴅᴀʏ 🥺🙂
"""

JOIN_THRESHOLD = 10
TIME_WINDOW    = 8
COOL_MINUTES   = 10
WELCOME_LIMIT  = 10

# ─────────────────────────────
# DATABASE
# ─────────────────────────────
class _WelDB:
    def __init__(self):
        self.state = {}
        self.join_cnt = {}
        self.last_ts = {}
        self.cool_until = {}

    async def is_on(self, cid): return self.state.get(cid, "on") == "on"
    async def set(self, cid, flag): self.state[cid] = flag

    async def bump(self, cid):
        now = datetime.now(timezone.utc)
        last = self.last_ts.get(cid, now - timedelta(seconds=TIME_WINDOW + 1))
        cnt = 1 if (now - last).total_seconds() > TIME_WINDOW else self.join_cnt.get(cid, 0) + 1
        self.join_cnt[cid] = cnt
        self.last_ts[cid] = now
        return cnt

    async def cool(self, cid):
        await self.set(cid, "off")
        self.cool_until[cid] = datetime.now(timezone.utc) + timedelta(minutes=COOL_MINUTES)

    async def auto_on(self, cid):
        ts = self.cool_until.get(cid)
        if ts and datetime.now(timezone.utc) >= ts:
            await self.set(cid, "on")
            self.cool_until.pop(cid, None)
            return True
        return False

db = _WelDB()
last_messages: dict[int, list] = {}



# ─────────────────────────────
# TOGGLE COMMAND
# ─────────────────────────────
@app.on_message(filters.command("welcome") & filters.group)
async def toggle(client, m: Message):
    usage = "**Usage:**\n⦿/welcome [on|off]\n➤ Annie Special Welcome....."
    if len(m.command) != 2:
        return await m.reply_text(usage)

    u = await client.get_chat_member(m.chat.id, m.from_user.id)
    if u.status not in (enums.ChatMemberStatus.ADMINISTRATOR, enums.ChatMemberStatus.OWNER):
        return await m.reply_text("**sᴏʀʀʏ ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴄʜᴀɴɢᴇ ᴡᴇʟᴄᴏᴍᴇ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ sᴛᴀᴛᴜs!**")

    flag = m.command[1].lower()
    if flag not in ("on", "off"):
        return await m.reply_text(usage)

    cur = await db.is_on(m.chat.id)
    if flag == "off" and not cur:
        return await m.reply_text("**ᴡᴇʟᴄᴏᴍᴇ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ ᴀʟʀᴇᴀᴅʏ ᴅɪsᴀʙʟᴇᴅ!**")
    if flag == "on" and cur:
        return await m.reply_text("**ᴡᴇʟᴄᴏᴍᴇ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ ᴀʟʀᴇᴀᴅʏ ᴇɴᴀʙʟᴇᴅ!**")

    await db.set(m.chat.id, flag)
    await m.reply_text(f"**{'ᴇɴᴀʙʟᴇᴅ' if flag == 'on' else 'ᴅɪsᴀʙʟᴇᴅ'} ᴡᴇʟᴄᴏᴍᴇ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ ɪɴ {m.chat.title}**")

# ─────────────────────────────
# WELCOME HANDLER
# ─────────────────────────────
@app.on_chat_member_updated(filters.group, group=-3)
async def welcome(client, update: ChatMemberUpdated):
    old, new, cid = update.old_chat_member, update.new_chat_member, update.chat.id
    if not (new and new.status == enums.ChatMemberStatus.MEMBER):
        return
    if old and old.status in (
        enums.ChatMemberStatus.MEMBER,
        enums.ChatMemberStatus.ADMINISTRATOR,
        enums.ChatMemberStatus.OWNER,
    ):
        return

    if not await db.is_on(cid):
        if await db.auto_on(cid):
            await client.send_message(cid, "**ᴡᴇʟᴄᴏᴍᴇ ᴍᴇssᴀɢᴇs ʜᴀᴠᴇ ʙᴇᴇɴ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ʀᴇ-ᴇɴᴀʙʟᴇᴅ.**")
        else:
            return

    if await db.bump(cid) >= JOIN_THRESHOLD:
        await db.cool(cid)
        return await client.send_message(
            cid, "**ᴍᴀssɪᴠᴇ ᴊᴏɪɴ ᴅᴇᴛᴇᴄᴛᴇᴅ. ᴡᴇʟᴄᴏᴍᴇ ᴍᴇssᴀɢᴇs ᴀʀᴇ ᴛᴇᴍᴘᴏʀᴀʀɪʟʏ ᴅɪsᴀʙʟᴇᴅ ғᴏʀ 10 ᴍɪɴᴜᴛᴇs.**"
        )

    user = new.user
    avatar = img = None
    try:
        avatar = await client.download_media(user.photo.big_file_id, file_name=f"downloads/pp_{user.id}.png") if user.photo else FALLBACK_PIC
        img = build_pic(avatar, user.first_name, user.id, user.username or "No Username")

        members = await client.get_chat_members_count(cid)
        caption = CAPTION_TXT.format(
            chat_title=update.chat.title,
            mention=user.mention,
            uid=user.id,
            uname=user.username or "No Username",
            count=members
        )

        sent = await client.send_photo(
            cid,
            img,
            caption=caption,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(BTN_VIEW, url=f"tg://openmessage?user_id={user.id}")],
                [InlineKeyboardButton(BTN_ADD,  url=f"https://t.me/{client.username}?startgroup=true")],
            ])
        )

        last_messages.setdefault(cid, []).append(sent)
        if len(last_messages[cid]) > WELCOME_LIMIT:
            old_msg = last_messages[cid].pop(0)
            try: await old_msg.delete()
            except: pass

    except Exception:
        await client.send_message(cid, f"🎉 Welcome, {user.mention}!")
    finally:
        for f in (avatar, img):
            if f and os.path.exists(f) and "ANNIEMUSIC/assets" not in f:
                try: os.remove(f)
                except: pass
