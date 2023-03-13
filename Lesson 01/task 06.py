# 6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор». 
# Проверить кодировку файла по умолчанию. 
# Принудительно открыть файл в формате Unicode и вывести его содержимое.

import locale

_str = ['сетевое программирование', 'сокет', 'декоратор']

with open('./lesson 01/test_file.txt', 'w+') as f:
    for vol in _str:
        f.write(vol + '\n')
    f.seek(0)
print(f)

_file_coding = locale.getpreferredencoding()

with open('./lesson 01/test_file.txt', 'r', encoding=_file_coding) as f:
    for vol in f:
        print(vol)
    f.seek(0)
   