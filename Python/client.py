from socket import socket

PORT = 33333

def main():
    with socket() as client:
        client.connect(('127.0.0.1', PORT))
        print('Установлено соединение с сервером')
        while True:
            text = input('Введите сообщение: ')
            client.sendall(text.encode())


if __name__ == "__main__":
    main()