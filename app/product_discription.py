import aiohttp


async def get_product_description(href_pages: str) -> str:
    '''
    Get product discription from json
    :param href_pages:
    :return:
    '''
    async with aiohttp.ClientSession() as session:
        async with session.get(href_pages) as response_aio:
            response_aio.raise_for_status()
            response_product_json = await response_aio.json()
            if response_product_json.get('description'):
                product_descr = response_product_json.get('description').strip().replace('\n', '')
            else:
                product_descr = ''

            return product_descr
