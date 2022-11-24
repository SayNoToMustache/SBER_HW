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

def search_with_depth(key, depth = 'n'):
    if depth == 'n':
        if key in site.keys():
            return site.items[1]
        

the_key = input('Введите искомый ключ: ')
if input('Хотите ввести максимальную глубину? Y/N: ').lower() == 'n':
    search_with_depth(the_key)
else:
    pass