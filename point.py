from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

bot = Client("point", api_id=13429252, api_hash="33d94e2daae5c7777f0d9b59a72ab0a6",
             bot_token="5588598438:AAGG344SZ2_uP7z9QNwNGY_gf6r932YYNrs")

channel = -1001235149288


@bot.on_message(filters.command('start'))
async def command1(_, message):
    await bot.send_message(message.chat.id, "مرحبا بك في بوت point")


def get_keyboard(mid):
    button = [
        [InlineKeyboardButton('-', f'm-{mid}'),
         InlineKeyboardButton('+', f'p-{mid}')],
        [InlineKeyboardButton('-5', f'm5-{mid}'),
         InlineKeyboardButton('+5', f'p5-{mid}')],
        [InlineKeyboardButton('-10', f'm10-{mid}'),
         InlineKeyboardButton('+10', f'p10-{mid}')],
        [InlineKeyboardButton('zero', f'z-{mid}')]
    ]
    return button


@bot.on_message()
async def command2(_, message):
    text = message.text + '\nرصيدك هو :  0'
    msg = await bot.send_message(channel, text)
    buttons = get_keyboard(msg.id)
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )


@bot.on_callback_query()
async def callback(_, cb: CallbackQuery):
    await cb.answer()
    data = cb.message.text.split(':')
    name = data[0].strip()
    score = int(data[1].strip())
    mode, mid = cb.data.split("-")
    if mode == 'm' and score > 0:
        score -= 1
    elif mode == 'p':
        score += 1
    elif mode == 'm5' and score > 5:
        score -= 5
    elif mode == 'p5':
        score += 5
    elif mode == 'm10' and score > 10:
        score -= 10
    elif mode == 'p10':
        score += 10
    elif mode == 'z':
        score = 0
    else:
        return
    text = name + ':  ' + str(score)
    await bot.edit_message_text(channel, int(mid), text)
    await cb.message.edit_text(text, reply_markup=cb.message.reply_markup)


bot.run()
