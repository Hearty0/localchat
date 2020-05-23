import sys
import socket

def main():

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', 11111))
        s.listen(1)

        while True:
            (conn, addr) = s.accept() 

            while True:
                received = conn.recv(1024)
                if received == '':
                    break
                else:
                    print(received.decode())

                send_msg = input().replace('b', '').encode()
                if send_msg == ' ':
                    break
                else:
                    conn.sendall(send_msg)
                    print("sent")

if __name__ == '__main__':
    main()
