import io
import json
from typing import Dict


def get_categories() -> Dict[str,str]:
    '''
    return:
    key: category name
    value: url
    '''
    with io.open('./catalog_search/catalog.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        urls_list = []
        names_list = []
        result_dict = {}
        m = 0

        for k, el in data.items():
            for key, elem in el.items():
                if isinstance(elem, dict):
                    for keys, element in elem.items():
                        print(f'{m}: {keys} {element}')
                        names_list.append(keys)
                        urls_list.append(element)
                        m += 1
                else:
                    print(f'{m}: {key} {elem}')
                    names_list.append(key)
                    urls_list.append(elem)
                    m += 1

        category = 123
        result_dict[names_list[category]] = urls_list[category]

        if len(result_dict) == 0:
            raise Exception('No categories found')

        return result_dict
