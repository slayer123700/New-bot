import asyncio
from pyrogram import Client, filters
from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import UserNotParticipant, FloodWait
from pyrogram.types import Message

from AnieXEricaMusic import app
from AnieXEricaMusic.utils.admin_filters import admin_filter

spam_chats = set()


@app.on_message(filters.command(["utag", "all", "mention"]) & filters.group & admin_filter)
async def tag_all_users(client: Client, message: Message):
    replied = message.reply_to_message
    text = message.text.split(None, 1)[1] if len(message.command) > 1 else ""

    if not replied and not text:
        return await message.reply(
            "<b>Reply to a message or give some text to tag all.</b>",
            parse_mode="HTML"
        )

    spam_chats.add(message.chat.id)
    usernum, usertxt, total_tagged = 0, "", 0

    try:
        async for member in client.get_chat_members(message.chat.id):
            if message.chat.id not in spam_chats:
                break

            if not member.user or member.user.is_bot:
                continue

            usernum += 1
            total_tagged += 1
            usertxt += f"⊚ <a href='tg://user?id={member.user.id}'>{member.user.first_name}</a>\n"

            if usernum == 5:
                try:
                    if replied:
                        await replied.reply_text(
                            f"{text}\n{usertxt}\n📢 Tagging {total_tagged} users done...",
                            parse_mode="HTML"
                        )
                    else:
                        await message.reply_text(
                            f"{text}\n{usertxt}\n📢 Tagging {total_tagged} users done...",
                            parse_mode="HTML"
                        )
                except FloodWait as e:
                    await asyncio.sleep(e.value)
                except Exception:
                    pass

                await asyncio.sleep(3)
                usernum, usertxt = 0, ""

        if usertxt:
            try:
                if replied:
                    await replied.reply_text(
                        f"{text}\n{usertxt}\n📢 Tagging {total_tagged} users done...",
                        parse_mode="HTML"
                    )
                else:
                    await message.reply_text(
                        f"{text}\n{usertxt}\n📢 Tagging {total_tagged} users done...",
                        parse_mode="HTML"
                    )
            except Exception:
                pass

        await message.reply(
            f"✅ <b>Tagging completed.</b><br>Total: <code>{total_tagged}</code> users.",
            parse_mode="HTML"
        )

    finally:
        spam_chats.discard(message.chat.id)


@app.on_message(filters.command(["cancel", "ustop"]))
async def cancel_spam(client: Client, message: Message):
    chat_id = message.chat.id

    if chat_id not in spam_chats:
        return await message.reply(
            "<b>I'm not tagging anyone right now.</b>",
            parse_mode="HTML"
        )

    try:
        member = await client.get_chat_member(chat_id, message.from_user.id)
        if member.status not in (ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER):
            return await message.reply(
                "<b>Only admins can cancel tagging.</b>",
                parse_mode="HTML"
            )
    except UserNotParticipant:
        return await message.reply(
            "<b>You are not a participant of this chat.</b>",
            parse_mode="HTML"
        )
    except Exception:
        return await message.reply(
            "<b>Error checking admin status.</b>",
            parse_mode="HTML"
        )

    spam_chats.discard(chat_id)
    return await message.reply(
        "🚫 <b>Tagging cancelled successfully.</b>",
        parse_mode="HTML"
    )
