# Программа клиент
from socket import *

def main():
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(('localhost', 8888))
    
    while True:
        msg = str(input(('Введите сообщение, серверу: ')))
        msg_encode = msg.encode('utf-8')
        s.send(msg_encode)
        data = s.recv(1024)
        print('Сервер: ', data.decode('utf-8'))


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
