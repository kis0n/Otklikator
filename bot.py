import asyncio
import logging

from glob import glob
from aiogram import Bot
from aiogram import F
from aiogram import Dispatcher
from aiogram import types
from aiogram.methods import SendAudio
from aiogram.types import Message
from aiogram.types import (
	ReplyKeyboardMarkup,
	KeyboardButton,
	InlineKeyboardMarkup,
	InlineKeyboardButton
	)


BOT_TOKEN = "6503877334:AAFIzBBB2vs6uGc0XWOcrCy4zw2XiOvN5gE"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
otkl = 0
otkaz = 0
test = 0
sobes = 0
audio_file_id = 'CQACAgIAAxkBAAEX8IZlinGlrhwDaN35lX7ZCS-jIpucbgACTzkAAru0WEh6V6ctd9-2azME'
# @dp.message(F.text == "/start") #реагирует на /start и отвечает
# async def start(message: Message):
				# await message.answer(f"Привет, <b>{message.from_user.first_name} </b>", reply_markup=main_kb) # вот это



main_kb = ReplyKeyboardMarkup(
	keyboard=[
		[
			KeyboardButton(text="➕ Отклик"),
			KeyboardButton(text="❌ Отказ"),
			KeyboardButton(text="🛠 Тестовое")
		],
		[
			KeyboardButton(text="⚔️ Собес"),
			KeyboardButton(text="📈 Статистика")
		],
		[
			KeyboardButton(text="🎉 ОФФЕР!!! 🎉"),
		]
	],
	resize_keyboard=True,
	# one_time_keyboard=True, #скрывает клавиатуру после первого использования
	input_field_placeholder="Выберите действие из меню",
	selective=True
	)


@dp.message(F.text == "Обнулить")
async def obnul(message: Message):
	global otkl
	otkl = 0
	global otkaz
	otkaz = 0
	global test
	test = 0
	global sobes
	sobes = 0
	audio_file_id = 'CQACAgIAAxkBAAEX8IZlinGlrhwDaN35lX7ZCS-jIpucbgACTzkAAru0WEh6V6ctd9-2azME'
	# print(otkl, otkaz, test, sobes)
	await message.answer(text= "Всё обнулил! 🤙")

@dp.message(F.text == "обнулить")
async def obnul(message: Message):
	global otkl
	otkl = 0
	global otkaz
	otkaz = 0
	global test
	test = 0
	global sobes
	sobes = 0
	audio_file_id = 'CQACAgIAAxkBAAEX8IZlinGlrhwDaN35lX7ZCS-jIpucbgACTzkAAru0WEh6V6ctd9-2azME'
	# print(otkl, otkaz, test, sobes)
	await message.answer(text= "Всё обнулил! 🤙")


@dp.message()
async def echo_message(message: types.Message):
	#await message.answer(text= "погоди-ка")        #функция шлет сообщение после любого сообщения в чате


	if message.text.startswith("➕"):
		global otkl
		otkl += 1
		print(otkl)
		await message.answer(text= "Отлично! Чем больше откликов, тем больше шансов найти работу!🙂" )
	

		# await message.reply(text="кайфуем!").  #функция, которая шлет ответ на предыдущее сообщение с подписью
	elif message.text.startswith("❌"):
		if otkl > 0:
			global otkaz
			otkaz += 1
			await message.answer(text= "Тааак, отказ. Ну ничего страшного! \n Без них никак, особенно в начале! 🙂")
		else:
		 await message.answer(text= "Какой отказ, если еще откликов не было? 🙂")
		
		

	elif message.text.startswith("🛠"):
		if otkl > 0:
			global test
			test += 1
			await message.answer(text= "О, тестовое задание! Давай-давай, распиши всё четко и не затягивай со сдачей!")
		else:
		 await message.answer(text= "Какое тестовое, если еще откликов нет? 🙂")



	elif message.text.startswith("⚔️"):
		if otkl > 0:
			global sobes
			sobes += 1
			await message.answer(text= "УФ, собес... Подготовься получше! Буду держать за тебя кулачки!👊")
		else:
		 await message.answer(text= "На собес без откликов? Не верю 🙂")


	elif message.text.startswith("📈"):
		if otkl > otkaz and sobes > 0:
			global stat
			global ignor
			ignor = otkl - otkaz
			stat = 100 / otkl * sobes

			await message.answer(f'Количество откликов {str(otkl)} \n' \
			f'Количество отказов {str(otkaz)} \n'
			f'Количество игноров {str(ignor)} \n'
			f'Переходы из откликов в собес равно {str(stat)} %\n'
			)
		else:
			if otkl > otkaz and sobes == 0:
				ignor = otkl - otkaz
				await message.answer(f'Количество откликов {str(otkl)} \n' \
				f'Количество отказов {str(otkaz)} \n'
				f'Количество игноров {str(ignor)} \n'
				f'Жаль собеседований пока нет!\n'
			)
			elif otkl == 0:
				await message.answer(text= "Чтобы была статистика, давай откликаться на вакансии 🙂")
			elif otkl == otkaz:
				await message.answer(f'Количество откликов {str(otkl)} \n' \
				f'Количество отказов {str(otkaz)} \n'
				f'Жаль собеседований пока нет!\n'
			)
			else:
				await message.answer(text= "Отказов больше чем откликов? Интересно 🙂")

		# print (otkl)
		# print (sobes) 
		# stat == otkl * 0.01 * sobes
		# print (str(stat))
		
			
	elif message.text.startswith("🎉"):
		if otkl > 0:
			await message.answer(f'Ебоииииии, ты получил ОФФЕР!!! Поздравляю!!! 🥳🥳🥳 \n' \
				f'https://www.youtube.com/watch?v=Sagg08DrO5U&t=12s \n'
			) 
		else:
		 await message.answer(text= "Оффер без откликов? Ты или сеньор-помидор, которого все хотят видеть у себя в команде, или тестировщик, что тычет везде подряд 🙂")

		
		# await bot.send_video(message.chat.id, 'https://media.giphy.com/media/TcdpZwYDPlWXC/giphy.gif')
		# audio = open('1.mp3', 'rb')
		
        # await bot.send_audio(message.from_user.id, audio=audio_file_id)

	elif message.text.startswith("/"):	
		await message.answer(f'Привет, {message.from_user.first_name}  \n' \
			f'Я помогу тебе вести статистику откликов, отказов и собеседований при трудоустройстве. \n' \
			f'Если вдруг тебе нужно обнулить все показатели - напиши мне "Обнулить"\n' \
			f'Я желаю тебе поскоре найти работу и не тратить моё время попусту!\n',
		reply_markup=main_kb)


	elif message.sticker:
		await message.answer_sticker(sticker=message.sticker.file_id) #ответ стикером на стикер
	else:
		await message.reply(text="Прости, но1 я не понимаю 😅")











async def main():
	logging.basicConfig(level=logging.INFO)
	await dp.start_polling(bot)

if __name__ == "__main__":
	asyncio.run(main())