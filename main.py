import config
import asyncio
from aiogram import Bot, Dispatcher, executor, types
from parse import parse

bot = Bot(token=config.API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['test'])
async def echo(message: types.Message):
	await message.answer("This is just a test. []", message)

 
async def check_news(cooldown):
	while True:
		print("I'm parsing news...")
		link = parse()
		if link:
			await bot.send_message(-475034432, link)
			
		else:
			print("Have no news")
		await asyncio.sleep(cooldown)

if __name__ == "__main__":
	dp.loop.create_task(check_news(600))
	executor.start_polling(dp, skip_updates=True)
