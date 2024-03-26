import io
import json


def check_enclosure(el, urls_list, names_list, category_counter) -> int:
    for key, elem in el.items():
        if not isinstance(elem, dict):
            print(f'{category_counter}: {key} {elem}')
            names_list.append(key)
            urls_list.append(elem)
            category_counter += 1
            continue

        for keys, element in elem.items():
            print(f'{category_counter}: {keys} {element}')
            names_list.append(keys)
            urls_list.append(element)
            category_counter += 1

    return category_counter


def get_categories() -> dict[str,str]:
    '''
    return:
    key: category name
    value: url
    '''
    with io.open('./catalog_search/catalog.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        result_dict = {}
        urls_list = []
        names_list = []
        category_counter = 0

        for k, el in data.items():
            category_counter = check_enclosure(el, urls_list, names_list, category_counter)

        for counter in range(category_counter):
            result_dict[f'{counter}: {names_list[counter]}'] = urls_list[counter]

        if not result_dict:
            raise Exception('No categories found')

        return result_dict


if __name__ == '__main__':
    get_categories()
