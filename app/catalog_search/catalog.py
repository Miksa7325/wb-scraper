from typing import Dict
import requests


def get_catalog() -> Dict:
    '''
    structure: nested dicts
    max_depth: 3
    key: name of category
    value: url
    '''
    categories_dict = {}
    url_prefix = "https://www.wildberries.by/catalog?category="

    params = {
        'lang': 'ru',
        'locale': 'by',
        'location': 'by',
    }
    response = requests.get('https://catalog.wb.ru/menu/v10/api', params=params)

    for items in response.json().get('data'):
        if not items.get('nodes'):
            continue

        nodes_dict = {}
        for nodes in items.get('nodes'):
            if not nodes.get('childrenOnly'):
                children = f"{url_prefix}{nodes.get('id')}"
                nodes_dict[nodes.get('name')] = children
                continue

            children = {}
            for ch in nodes.get('nodes'):
                children[ch.get('name')] = f"{url_prefix}{ch.get('id')}"
            nodes_dict[nodes.get('name')] = children

        categories_dict[items.get('name')] = nodes_dict

    return categories_dict
