from io import BytesIO
from httpx import AsyncClient, Timeout
from pyrogram import filters
from pyrogram.types import Message
from AnieXEricaMusic import app

fetch = AsyncClient(
    http2=True,
    verify=False,
    headers={
        "Accept-Language": "id-ID",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    },
    timeout=Timeout(20),
)


class QuotlyException(Exception):
    pass


async def get_text_or_caption(ctx: Message):
    return ctx.text or ctx.caption or ""


async def get_message_sender_name(ctx: Message):
    if ctx.forward_date and ctx.forward_sender_name:
        return ctx.forward_sender_name
    elif ctx.from_user:
        return f"{ctx.from_user.first_name} {ctx.from_user.last_name or ''}".strip()
    elif ctx.sender_chat:
        return ctx.sender_chat.title
    return "Anonymous"


async def get_message_sender_id(ctx: Message):
    return ctx.from_user.id if ctx.from_user else 1


async def get_message_sender_username(ctx: Message):
    return ctx.from_user.username if ctx.from_user else ""


async def get_message_sender_photo(ctx: Message):
    user = ctx.from_user
    if user and user.photo:
        return {
            "small_file_id": user.photo.small_file_id,
            "small_photo_unique_id": user.photo.small_photo_unique_id,
            "big_file_id": user.photo.big_file_id,
            "big_photo_unique_id": user.photo.big_photo_unique_id,
        }
    return ""


async def pyrogram_to_quotly(messages, is_reply):
    if not isinstance(messages, list):
        messages = [messages]

    payload = {
        "type": "quote",
        "format": "png",
        "backgroundColor": "#1b1429",
        "messages": [],
    }

    for message in messages:
        msg_data = {
            "chatId": await get_message_sender_id(message),
            "text": await get_text_or_caption(message),
            "avatar": True,
            "entities": [
                {
                    "type": entity.type.name.lower(),
                    "offset": entity.offset,
                    "length": entity.length,
                }
                for entity in (message.entities or message.caption_entities or [])
            ],
            "from": {
                "id": await get_message_sender_id(message),
                "name": await get_message_sender_name(message),
                "username": await get_message_sender_username(message),
                "type": message.chat.type.name.lower(),
                "photo": await get_message_sender_photo(message),
            },
        }

        if message.reply_to_message and is_reply:
            msg_data["replyMessage"] = {
                "name": await get_message_sender_name(message.reply_to_message),
                "text": await get_text_or_caption(message.reply_to_message),
                "chatId": await get_message_sender_id(message.reply_to_message),
            }
        else:
            msg_data["replyMessage"] = {}

        payload["messages"].append(msg_data)

    response = await fetch.post("https://bot.lyo.su/quote/generate.png", json=payload)
    if not response.is_error:
        return response.read()
    raise QuotlyException(response.json())


def isArgInt(txt) -> list:
    try:
        count = int(txt)
        return [True, count]
    except ValueError:
        return [False, 0]


@app.on_message(filters.command(["q", "r"]) & filters.reply)
async def quote_command(_, message: Message):
    waiting = await message.reply("Generating quote...")
    is_reply = message.command[0] == "r"

    if len(message.command) > 1:
        check_arg = isArgInt(message.command[1])
        if check_arg[0]:
            count = check_arg[1]
            if not 2 <= count <= 10:
                await waiting.delete()
                return await message.reply("Use a range between 2 and 10.")

            try:
                messages = [
                    m
                    for m in await app.get_messages(
                        chat_id=message.chat.id,
                        message_ids=range(
                            message.reply_to_message.id,
                            message.reply_to_message.id + count,
                        ),
                    )
                    if not m.empty and not m.media
                ]
                quotly_data = await pyrogram_to_quotly(messages, is_reply)
                bio_sticker = BytesIO(quotly_data)
                bio_sticker.name = "quote.webp"
                await waiting.delete()
                return await message.reply_sticker(bio_sticker)
            except Exception:
                await waiting.delete()
                return await message.reply("Error while processing.")
    else:
        try:
            quoted = await app.get_messages(
                chat_id=message.chat.id, message_ids=message.reply_to_message.id
            )
            quotly_data = await pyrogram_to_quotly([quoted], is_reply)
            bio_sticker = BytesIO(quotly_data)
            bio_sticker.name = "quote.webp"
            await waiting.delete()
            return await message.reply_sticker(bio_sticker)
        except Exception as e:
            await waiting.delete()
            return await message.reply(f"Error: {e}")
