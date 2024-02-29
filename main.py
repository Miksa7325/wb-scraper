import asyncio
from aiohttp import ClientConnectorError

from products_data.category import get_categories
from products_data.mongo_db import MongoDB
from products_data.selenium_connect import SeleniumPage
from products_data.spider_category_pages import CategorySpider


async def start_request():
    urls = get_categories()
    async with MongoDB():
        with SeleniumPage() as selenium_connect:
            for key, url in urls.items():
                while True:
                    try:
                        html_page = selenium_connect.process_request(url)
                    except ClientConnectorError:
                        pass
                    if html_page is not None:
                        break
                await CategorySpider().start_spider(html_page)


if __name__ == '__main__':
    asyncio.run(start_request())

# for products_data in await CategorySpider().start_spider(html_page):
#     # products_data = await CategorySpider().start_spider(html_page)
#     await db.add_document(collection_name, products_data)
# for products_data in await CategorySpider().start_spider(html_page):
#
#     # await db.add_document(collection_name, products_data)