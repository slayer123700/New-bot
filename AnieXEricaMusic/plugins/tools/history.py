import asyncio
import random
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.raw.functions.messages import DeleteHistory

from AnieXEricaMusic import app
from AnieXEricaMusic.core.userbot import assistants
from AnieXEricaMusic.utils.database import get_client


@app.on_message(filters.command(["sg", "History"]))
async def sg(client: Client, message: Message):

    if len(message.text.split()) < 2 and not message.reply_to_message:
        return await message.reply("ꜱɢ ᴜꜱᴇʀɴᴀᴍᴇ/ɪᴅ/ʀᴇᴘʟʏ")
    if message.reply_to_message:
        args = message.reply_to_message.from_user.id
    else:
        args = message.text.split()[1:]
        if not args:
            return await message.reply(
                "ᴘʟᴇᴀꜱᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ ᴜꜱᴇʀɴᴀᴍᴇ, ɪᴅ, ᴏʀ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇꜱꜱᴀɢᴇ"
            )
        args = args[0]
    lol = await message.reply("<code>...</code>")
    if args:
        try:
            user = await client.get_users(f"{args}")
        except Exception:
            return await lol.edit("<code>ᴘʟᴇᴀꜱᴇ ꜱᴘᴇᴄɪꜰʏ ᴀ ᴠᴀʟɪᴅ ᴜꜱᴇʀ!</code>")
    sgbot = ["sangmata_bot", "sangmata_beta_bot"]
    sg = random.choice(sgbot)
    RISHU = random.choice(assistants)
    ubot = await get_client(RISHU)

    try:
        a = await ubot.send_message(sg, f"{user.id}")
        await a.delete()
    except Exception as e:
        return await lol.edit(str(e))
    await asyncio.sleep(1)

    async for stalk in ubot.search_messages(a.chat.id):
        if stalk.text is None:
            continue
        if not stalk:
            await message.reply("botnya ngambek")
        elif stalk:
            await message.reply(f"{stalk.text}")
            break

    try:
        user_info = await ubot.resolve_peer(sg)
        await ubot.send(DeleteHistory(peer=user_info, max_id=0, revoke=True))
    except Exception:
        pass

    await lol.delete()
