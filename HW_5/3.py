'''
Пример 1:
Введите искомый ключ: head
Хотите ввести максимальную глубину? Y/N: n
Значение ключа: {'title': 'Мой сайт'}
'''

site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


def search_with_depth(site: dict, key: str, depth: int | None = None):
    if isinstance(site, dict):
        if key in site:
            return site.get(key)
        if depth is not None and depth == 0:
            return None
        for value in site.values():
            if (result := search_with_depth(
                value,
                key,
                (depth-1 if depth is not None else None)
            )) is not None:
                break
        else:
            result = None
        return result
    else:
        return None


while True:
    the_key = input('Введите искомый ключ: ')
    string_ = input('Хотите ввести максимальную глубину? Y/N: ').lower()
    if string_ == 'n':
        print(search_with_depth(site, the_key))
        break
    elif string_ == 'y':
        print(search_with_depth(site, the_key, int(input('Введите глубину: '))))
        break
    else:
        print('yes or no')
