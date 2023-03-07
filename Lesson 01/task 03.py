# 3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.

value1 = b'attribute'
value2 = b'класс'
value3 = b'функция'
value4 = b'type'

# на строки записанные на кириллице вылетает исключение: SyntaxError: bytes can only contain ASCII literal characters
