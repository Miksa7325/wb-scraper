import json
from catalog_search.catalog import get_catalog


def write_json_categories(file, data):
    with open(file, 'w', encoding='utf-8') as f:
        json_text = json.dumps(data, indent=4, ensure_ascii=False)
        f.writelines(json_text)


if __name__ == '__main__':
    write_json_categories('catalog.json', get_catalog())
