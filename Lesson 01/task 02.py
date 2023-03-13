# 2. Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность кодов (не используя методы encode и decode) и определить тип, 
# содержимое и длину соответствующих переменных.

import binascii

_str = [b'class', b'function', b'method']

for value in _str:
    print(type(value), binascii.hexlify(value), len(value))
