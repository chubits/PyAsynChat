# Программа сервера
from socket import *
import time


def main():
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(('localhost', 8888))
    s.listen(5)

    client, addr = s.accept()
    print('Получаем запрос на соеденение: ', addr)

    while True:             
        data = client.recv(10000)
        print('Было получено сообщение: ', data.decode('utf-8'))
        msg = 'Ваше сообщение получено'
        client.send(msg.encode('utf-8'))


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
