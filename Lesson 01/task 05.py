# 5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в строковый тип на кириллице.

import subprocess


_ping_url = [['ping', 'yandex.ru'],['ping', 'youtube.com']]

for ping_vol in _ping_url:

    _ping = subprocess.Popen(ping_vol, stdout=subprocess.PIPE)

    i = 0

    for vol_line in _ping.stdout:

        if i < 10:
            print(vol_line)
            vol_line = vol_line.decode('cp866').encode('utf-8')
            print(vol_line.decode('utf-8'))
            i += 1
        else:
            break
