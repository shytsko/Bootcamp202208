from socket import socket
from threading import Thread

PORT = 33333

def main():
    with socket() as server:
        server.bind(('', PORT))
        server.listen()
        print(f"Сервер запущен. Порт для подключения {PORT}")
        while True:
            client, addressClient = server.accept()
            clientHandle = Thread(target=ClientHandle, args=(client, addressClient), daemon=True)
            clientHandle.start()



def ClientHandle(client, address):
    print(f'Установлено соединение с клиентом {address}')
    while True:
        data = client.recv(1024)
        print(f'Получено сообщение от клиента с адресом {address}: {data.decode()}')


if __name__ == "__main__":
    main()