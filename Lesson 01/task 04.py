# 4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в байтовое
# и выполнить обратное преобразование (используя методы encode и decode).

_str = ['разработка', 'администрирование', 'protocol', 'standar']

for vol in _str:
    vol_enc = vol.encode('utf=8')
    print(type(vol_enc), vol_enc)
    vol_dec = bytes.decode(vol_enc, 'utf=8')
    print(type(vol_dec), vol_dec)
