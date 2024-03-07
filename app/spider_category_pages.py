import re
from aiohttp import ClientResponseError
from scrapy import Selector

from models import Product
from product_discription import get_product_description


class CategorySpider():

    def __init__(self):
        self.main_url = 'https://www.wildberries'

    async def start_spider(self, html):
        page_source = Selector(text=html)
        for a in page_source.xpath('//*[@id="route-content"]/div/div[2]/div[2]/div[2]/div[2]/div/div/a'):

            product_brand = a.xpath('div[2]/div[3]/div[2]/span[1]/text()').get()
            product_name = a.xpath('div[2]/div[3]/div[2]/span[2]/text()').get()
            product_price = a.xpath('div[2]/div[1]/span/span[2]/text()').get()
            if product_price:
                product_price = float(product_price.replace(',', '.'))
            price_currency = a.xpath('div[2]/div[1]/span/span[2]/text()').get()
            product_href = a.xpath('./@href').get()
            product_img = a.xpath('div[1]/div[1]/div/div[1]/div[1]/picture/img/@src').get()
            product_rating = a.xpath('div[2]/div[4]/span[1]/span/text()').get()
            try:
                product_rating = float(product_rating)
            except Exception:
                product_rating = 0
            product_reviews = a.xpath('div[2]/div[4]/span[2]/span/text()').get()
            try:
                product_reviews = product_reviews.replace('\u2009', '')
                product_reviews = int(product_reviews)
            except Exception:
                product_reviews = 0

            pattern = r"(\S+)(images\S+)"
            match = re.search(pattern, product_img)

            try:
                href_pages = f'{match[1]}info/ru/card.json'
                product_description = await get_product_description(href_pages)
            except ClientResponseError:
                continue

            item = Product(
                brand=product_brand,
                name=product_name,
                price=product_price,
                currency=price_currency,
                url=f'{self.main_url}{product_href}',
                img_link=product_img,
                description=product_description,
                rating=product_rating,
                reviews=product_reviews,
            )

            await item.save()
