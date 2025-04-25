from django.core.management.base import BaseCommand
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command as AiogramCommand

from asgiref.sync import sync_to_async

from .parser import get_category, get_product
from Product import models

url = 'https://new.technodom.kg'

logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="7694700320:AAG_B66bIxp3GIMjnGpUnwBzHN07LaBS0cQ")
# Диспетчер
dp = Dispatcher()


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        @dp.message(AiogramCommand("start"))
        async def cmd_start(message: types.Message):
            await message.answer("Parser started!")

            saves_category = []

            category_link, category_name = get_category(url)

            for i in category_name:
                new_cat = models.Category(name=i)
                saves_category.append(new_cat)

            await sync_to_async(models.Category.objects.bulk_create)(saves_category)

            for i in range(len(category_link)):
                products = get_product(category_link[i])
                saves_product = []

                for j in products:
                    cat = await sync_to_async(models.Category.objects.get)(name=category_name[i]) 
                    new_prod = models.Product(name=j['name'],
                                              link=j['link'],
                                              img_link=j['img_link'],
                                              price=j['price'],
                                              category=cat)
                    saves_product.append(new_prod)

                await sync_to_async(models.Product.objects.bulk_create)(saves_product)

            await message.answer("Parser finished!")

        # Запуск процесса поллинга новых апдейтов
        async def main():
            await dp.start_polling(bot)
        
        try:
            asyncio.run(main())

        except KeyboardInterrupt:
            print('Exit code')