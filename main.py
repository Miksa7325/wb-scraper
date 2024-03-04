import asyncio
from aiohttp import ClientConnectorError

from products_data.category import get_categories
from products_data.mongo_db import MongoDB
from products_data.selenium_connect import SeleniumPage
from products_data.spider_category_pages import CategorySpider

def check_request(selenium_connect, url):
    while True:
        try:
            html = selenium_connect.process_request(url)
        except ClientConnectorError:
            pass
        if html is not None:
            break
    return html


async def start_request():
    urls = get_categories()
    async with MongoDB():
        with SeleniumPage() as selenium_connect:
            for key, url in urls.items():
                html_page = check_request(selenium_connect, url)
                await CategorySpider().start_spider(html_page)


if __name__ == '__main__':
    asyncio.run(start_request())
