import asyncio
from pyrogram import Client, filters
from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import UserNotParticipant, FloodWait
from pyrogram.types import Message

from AnieXEricaMusic import app
from AnieXEricaMusic.utils.admin_filters import admin_filter

spam_chats = set()


def escape_markdown(text: str) -> str:
    escape_chars = r'\_*[]()~`>#+-=|{}.!'
    for char in escape_chars:
        text = text.replace(char, f"\\{char}")
    return text


@app.on_message(filters.command(["utag", "all", "mention"]) & filters.group & admin_filter)
async def tag_all_users(client: Client, message: Message):
    replied = message.reply_to_message
    raw_text = message.text.split(None, 1)[1] if len(message.command) > 1 else ""
    text = escape_markdown(raw_text)

    if not replied and not text:
        return await message.reply(
            "*Reply to a message or provide text to tag all users\\.*",
            parse_mode="MarkdownV2"
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
            name = escape_markdown(member.user.first_name)
            usertxt += f"⊚ [{name}](tg://user?id={member.user.id})\n"

            if usernum == 5:
                try:
                    if replied:
                        await replied.reply_text(
                            f"{text}\n{usertxt}\n📢 *Tagging {total_tagged} users done\\.*",
                            parse_mode="MarkdownV2"
                        )
                    else:
                        await message.reply_text(
                            f"{text}\n{usertxt}\n📢 *Tagging {total_tagged} users done\\.*",
                            parse_mode="MarkdownV2"
                        )
                except FloodWait as e:
                    await asyncio.sleep(e.value)
                except Exception:
                    pass

                await asyncio.sleep(2)
                usernum, usertxt = 0, ""

        if usertxt:
            try:
                if replied:
                    await replied.reply_text(
                        f"{text}\n{usertxt}\n📢 *Tagging {total_tagged} users done\\.*",
                        parse_mode="MarkdownV2"
                    )
                else:
                    await message.reply_text(
                        f"{text}\n{usertxt}\n📢 *Tagging {total_tagged} users done\\.*",
                        parse_mode="MarkdownV2"
                    )
            except Exception:
                pass

        await message.reply(
            f"✅ *Tagging completed\\. Total:* `{total_tagged}` *users\\.*",
            parse_mode="MarkdownV2"
        )

    finally:
        spam_chats.discard(message.chat.id)


@app.on_message(filters.command(["cancel", "ustop"]) & filters.group)
async def cancel_spam(client: Client, message: Message):
    chat_id = message.chat.id

    if chat_id not in spam_chats:
        return await message.reply(
            "*I’m not tagging anyone right now\\.*",
            parse_mode="MarkdownV2"
        )

    try:
        member = await client.get_chat_member(chat_id, message.from_user.id)
        if member.status not in (ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER):
            return await message.reply(
                "*Only admins can cancel tagging\\.*",
                parse_mode="MarkdownV2"
            )
    except UserNotParticipant:
        return await message.reply(
            "*You are not a participant of this chat\\.*",
            parse_mode="MarkdownV2"
        )
    except Exception:
        return await message.reply(
            "*Error checking admin status\\.*",
            parse_mode="MarkdownV2"
        )

    spam_chats.discard(chat_id)
    return await message.reply(
        "🚫 *Tagging cancelled successfully\\.*",
        parse_mode="MarkdownV2"
    )
