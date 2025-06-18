
import os
import textwrap
from PIL import Image, ImageDraw, ImageFont
from pyrogram import filters
from pyrogram.types import Message
from AnieXEricaMusic import app


@app.on_message(filters.command("mmf"))
async def mmf(_, message: Message):
    chat_id = message.chat.id
    reply_message = message.reply_to_message

    if len(message.text.split(maxsplit=1)) < 2:
        return await message.reply_text("Please provide some text.\nUsage: /mmf Top Text;Bottom Text")

    if not reply_message or not (reply_message.photo or reply_message.document):
        return await message.reply_text("Rᴇᴘʟʏ Tᴏ A Iᴍᴀɢᴇ Mʏ Dᴜᴍʙ Cᴜᴛɪᴇ Pɪᴇ 🤧")

    msg = await message.reply_text("I Aᴍ Cʀᴇᴀᴛɪɴɢ Uɴᴛɪʟ Tʜᴇɴ U Pʟᴢ Dɪᴇ 🤨 ")

    text = message.text.split(None, 1)[1]
    file_path = await app.download_media(reply_message)

    meme = await drawText(file_path, text)

    if isinstance(meme, str) and meme.endswith(".webp") and os.path.exists(meme):
        await app.send_document(chat_id, document=meme)
        os.remove(meme)
    else:
        await message.reply_text(f"❌ Error: {meme}")

    await msg.delete()


async def drawText(image_path, text):
    try:
        img = Image.open(image_path).convert("RGB")
    except Exception:
        return "❌ Couldn't open the image."

    # Remove the original image to save space
    if os.path.exists(image_path):
        os.remove(image_path)

    i_width, i_height = img.size

    # Font path (update it to actual path if different)
    if os.name == "nt":
        fnt_path = "font.ttf"
    else:
        fnt_path = "./AnieXEricaMusic/assets/font.ttf"

    try:
        m_font = ImageFont.truetype(fnt_path, int((70 / 640) * i_width))
    except OSError:
        return "⚠️ Font file not found! Please check the font path."

    # Split text into top and bottom
    if ";" in text:
        upper_text, lower_text = text.split(";", 1)
    else:
        upper_text = text
        lower_text = ""

    draw = ImageDraw.Draw(img)
    current_h, pad = 10, 5
    wrap_width = max(20, i_width // 40)

    def draw_outline_text(draw, position, text, font):
        x, y = position
        for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2), (-2, -2), (2, -2), (-2, 2), (2, 2)]:
            draw.text((x + dx, y + dy), text, font=font, fill="black")
        draw.text((x, y), text, font=font, fill="white")

    # Top text
    if upper_text:
        for line in textwrap.wrap(upper_text.strip(), width=wrap_width):
            bbox = m_font.getbbox(line)
            u_width, u_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
            draw_outline_text(
                draw,
                ((i_width - u_width) / 2, current_h),
                line,
                m_font
            )
            current_h += u_height + pad

    # Bottom text
    if lower_text:
        for line in textwrap.wrap(lower_text.strip(), width=wrap_width):
            bbox = m_font.getbbox(line)
            u_width, u_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
            draw_outline_text(
                draw,
                ((i_width - u_width) / 2, i_height - u_height - 20),
                line,
                m_font
            )

    output_file = "memify.webp"
    img.save(output_file, "webp")

    return output_file


mod_name = "mmf"
