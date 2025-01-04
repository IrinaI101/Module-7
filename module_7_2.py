def custom_write(file_name, strings: list):
    strings_positions = {}
    file = open(file_name, 'w', encoding= 'utf-8')
    for idx, string in enumerate(strings, start= 1):
        b_str = file.tell()
        file.write(f'{string}\n')
        strings_positions.update({(idx, b_str) : string})
    file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)