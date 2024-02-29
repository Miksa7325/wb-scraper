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

        while True:
            category = input('Input the category or exit\n')
            if category.isdigit() and int(category) < len(names_list):
                result_dict[names_list[int(category)]] = urls_list[int(category)]
            else:
                break

        if len(result_dict) == 0:
            raise Exception('No categories found')

        return result_dict




# def get_categories() -> Dict[str,str]:
#     '''
#     return:
#     key: category name
#     value: url
#     '''
#     with io.open('../catalog_search/catalog.json', 'r', encoding='utf-8') as json_file:
#         data = json.load(json_file)
#         result_categories_dict = {}
#
#         while True:
#             i = 0
#             k = 0
#             m = 0
#
#             for el in data:
#                 print(f'{i}: {el}')
#                 i += 1
#
#             key_list = list(data.keys())
#             main_categories = input('Enter the category or exit\n')
#
#             if main_categories.isdigit() and int(main_categories) < i:
#                 next_categories = key_list[int(main_categories)]
#             else:
#                 break
#
#             for el in data.get(next_categories):
#                 print(f'{k}: {el}')
#                 k += 1
#
#             key_list_second_page = list(data.get(next_categories).keys())
#             second_page_categories = input('Enter the second layer\n')
#
#             if second_page_categories.isdigit() and int(second_page_categories) < k:
#                 next_categories_second_page = key_list_second_page[int(second_page_categories)]
#             else:
#                 break
#
#             result_dict = data.get(next_categories).get(next_categories_second_page)
#             if isinstance(result_dict, dict):
#                 for el in result_dict:
#                     print(f'{m}: {el}')
#                     m += 1
#
#                 result_list = list(result_dict.keys())
#                 result_category = input('Enter the third layer\n')
#
#                 if result_category.isdigit() and int(result_category) < m:
#                     next_categories_result = result_list[int(result_category)]
#                 else:
#                     break
#
#                 result_categories_dict[next_categories_result] = result_dict.get(next_categories_result)
#             else:
#                 result_categories_dict[next_categories_second_page] = result_dict
#
#         return result_categories_dict
