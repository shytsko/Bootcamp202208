from socket import socket

PORT = 55555

def main():
    with socket() as client:
        client.connect(('84.201.139.158', PORT))
        print('Установлено соединение с сервером')
        while True:
            text = input('Введите сообщение: ')
            client.sendall(text.encode())


if __name__ == "__main__":
    main()