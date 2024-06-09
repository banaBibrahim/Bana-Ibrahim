import socket
import threading

# قائمة الحسابات المصرفية مع الأرصدة المبدئية
bank_accounts = {
    '2826': 1000,
    '5678': 2000,
    # ... يمكنك إضافة المزيد من الحسابات هنا
}


def handle_client(client_socket, client_address):
    """
    يُعالج اتصال العميل ويُنفذ الأوامر المطلوبة.
    :param client_socket: مأخذ العميل
    :param client_address: عنوان العميل
    """
    try:
        # استقبال تفاصيل الحساب من العميل
        account_number = client_socket.recv(1024).decode()
        password = client_socket.recv(1024).decode()

        # التحقق من صحة تفاصيل الحساب
        if account_number in bank_accounts and password == 'password':
            client_socket.send(b'Authentication successful!')
            while True:
                # استقبال الأمر من العميل (مثل "check_balance" أو "deposit")
                command = client_socket.recv(1024).decode()
                if command == 'check_balance':
                    balance = bank_accounts[account_number]
                    client_socket.send(f'Your balance: {balance}'.encode())
                elif command == 'deposit':
                    amount = float(client_socket.recv(1024).decode())
                    bank_accounts[account_number] += amount
                    client_socket.send(b'Deposit successful!')
                # ... يمكنك إضافة المزيد من الأوامر هنا
        else:
            client_socket.send(b'Authentication failed!')
    except Exception as e:
        print(f"Error handling client {client_address}: {e}")
    finally:
        client_socket.close()


def main():
    server_ip = '127.0.0.1'
    server_port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
    server_socket.listen(5)
    print(f"Listening on {server_ip}:{server_port}...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()


if __name__ == "__main__":
    main()
