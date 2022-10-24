from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

bot = Client(
    "point", api_id=13429252, api_hash="33d94e2daae5c7777f0d9b59a72ab0a6",
    bot_token="5588598438:AAGG344SZ2_uP7z9QNwNGY_gf6r932YYNrs")


@bot.on_message(filters.command('start'))
def command1(_, message):
    bot.send_message(message.chat.id, "مرحبا بك في بوت point")


botton = [
    [InlineKeyboardButton('-', 'm'),
     InlineKeyboardButton('+', 'p')]
]



@bot.on_message()
def command2(_, message):
    text = message.text + '\nرصيدك هو :  0'
    reply_markup = InlineKeyboardMarkup(botton)
    message.reply(
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
	if cb.data == 'm' and score > 0:
		score -= 1
	elif cb.data == 'p':
		score += 1
	else:
		return 
	text = name + ':  ' + str(score)
	await cb.message.edit_text(text, reply_markup=cb.message.reply_markup)
		
	

bot.run()
