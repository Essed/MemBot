from config import TOKEN, CHANNEL_ID

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
from keyboards.keyboard import queue_keyboard


from llapi.post import Post, PostQueue
from llapi.cache import CollectorsCache

bot = Bot(TOKEN)
dp = Dispatcher(bot)
channel_id = CHANNEL_ID


storage = CollectorsCache()
posts = PostQueue()

post1 =  Post("*Тест предложки*", "Мем 1")
post2 =  Post("*Тест предложки*", "Мем 2")

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("bot started")
    
    await storage.add_many([post1, post2])

    await posts.make(await storage.read_cache())

    first_post = await posts.get_post()

    await message.answer(f"{await first_post.post_text()}", reply_markup=queue_keyboard)


@dp.callback_query_handler(Text(equals="Принять", ignore_case=True))
async def accept_post(callback: types.CallbackQuery):

    if await posts.count > 0:

        await callback.message.answer("Пост успешно обупликован")
        
        next_post = await posts.get_post()

        post = await posts.get_post()

        await bot.send_message(channel_id, await post.post_text())

        await posts.accept()

        if await posts.empty == True:

            next_post = await posts.get_post()
            post = await next_post.get_post()

            await callback.message.answer(await post.post_text(), reply_markup=queue_keyboard)
        
        else:
            await callback.message.answer("Посты в предложке закончились")

    else:
        await callback.message.answer("Посты в предложке закончились")


@dp.callback_query_handler(Text(equals="Отклонить", ignore_case=True))
async def reject_post(callback: types.CallbackQuery):

    if await posts.count > 0:

        await callback.message.answer("Пост отклонен")
        
        next_post = await posts.get_post()
        post = await posts.get_post()

        await posts.accept()

        if await posts.empty == True:

            next_post = await posts.get_post()
            post = await next_post.get_post()

            await callback.message.answer(await post.post_text(), reply_markup=queue_keyboard)
        
        else:
            await callback.message.answer("Посты в предложке закончились")

    else:
        await callback.message.answer("Посты в предложке закончились")


executor.start_polling(dp, skip_updates=True)